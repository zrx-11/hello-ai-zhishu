# -*- coding: utf-8 -*-
import os, json, importlib.util, re, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W = os.path.join(BASE, "_work")

def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(W, name + ".py"))
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    for k in dir(mod):
        if k.isupper():
            return getattr(mod, k)

CHAPTERS = load("chapters_a") + load("chapters_b") + load("chapters_c") + load("chapters_d")
CONCEPTS = load("concepts_a") + load("concepts_b") + load("concepts_c")
DEPTH = {}
DEPTH.update(load("depth_a")); DEPTH.update(load("depth_b"))
QUIZZES = load("quizzes")
GLOSSARY = json.load(open(os.path.join(W, "glossary.json"), encoding="utf-8"))

PAGES = {
"ch01":"6–15","ch02":"16–26","ch03":"27–36","ch04":"37–48","ch05":"49–58",
"ch06":"59–70","ch07":"71–78","ch08":"79–86","ch09":"87–96","ch10":"97–104",
"ch11":"105–113","ch12":"114–129","ch13":"130–141","ch14":"142–150",
"t01":"151–156","t02":"157–160","t03":"161–173","t04":"174–182","t05":"183–193","t06":"194–199"}

CH_PREREQ = {
"ch01":[],"ch02":["ch01"],"ch03":["ch01"],"ch04":["ch01"],"ch05":["ch04"],
"ch06":["ch05"],"ch07":["ch06"],"ch08":["ch07"],"ch09":["ch08"],"ch10":["ch09"],
"ch11":["ch09"],"ch12":["ch11"],"ch13":["ch09"],"ch14":["ch12"],
"t01":["ch08"],"t02":["ch05"],"t03":["ch06"],"t04":["ch05"],"t05":["ch09"],"t06":["ch09"]}

CH_TITLE = {}
for c in CHAPTERS:
    if str(c["num"]).startswith("T"):
        CH_TITLE[c["id"]] = f"专题 {c['num'][1:]}：{c['title']}"
    else:
        CH_TITLE[c["id"]] = f"第 {c['num']} 章：{c['title']}"

def md_escape_table(s):
    return str(s).replace("|", "／").replace("\n", " ")

def render_chapter(c):
    cid = c["id"]
    num = c["num"]
    head = f"# {CH_TITLE[cid]}\n\n"
    head += f"> {c['part']}　·　{c['subtitle']}\n\n"
    head += f"- **难度**：{'★'*int(c['difficulty'])}{'☆'*(3-int(c['difficulty']))} ｜ **预估学时**：{c['hours']} 小时 ｜ **前置**：{c['prereq']}\n\n"
    head += "## 学习目标\n\n学完本章，你能：\n\n"
    head += "\n".join(f"- {g}" for g in c["goal"]) + "\n\n"
    head += f"## 一句话核心\n\n{c['core']}\n\n"
    head += "## 零基础讲解\n\n" + c["body"].strip() + "\n\n"
    head += "## 图示\n\n```mermaid\n" + c["mermaid"].strip() + "\n```\n\n" + c["diagram_note"] + "\n\n"
    head += "## 类比与实例\n\n"
    head += f"- **类比**：{c['analogy']}\n"
    head += f"- **实例**：{c['example']}\n\n"
    head += "## 常见误解\n\n"
    for wrong, right in c["misconceptions"]:
        head += f"- 别以为 {wrong}——实际上 {right}\n"
    head += "\n## 自测题（答案）\n\n"
    for i, q in enumerate(c["selfcheck"], 1):
        head += f"{i}. {q['q']}（答案：{q['a']}；解析：{q['e']}）\n"
    head += "\n## 复习锚点\n\n"
    head += "\n".join(f"- {a}" for a in c["anchors"]) + "\n"
    return head

def render_concept(c):
    cid = c["id"]; ch = c["chapter"]
    head = f"# {c['title']}\n\n"
    head += f"- **难度**：{c['difficulty']} ｜ **涉及章节**：{CH_TITLE[ch]}\n\n"
    head += f"## 一句话定义\n\n{c['short']}\n\n"
    head += f"## 为什么重要\n\n{c['why']}\n\n"
    head += "## 详解\n\n" + c["detail"].strip() + "\n\n"
    mis = c.get("mis", [])
    if mis:
        head += "## 常见误解\n\n"
        for m in mis:
            head += f"- {m}\n"
        head += "\n"
    head += "## 在书中出现的脉络\n\n"
    head += "| 章节 | 语境 | 关键结论 |\n|---|---|---|\n"
    head += f"| {CH_TITLE[ch]} | 本章核心概念之一 | {md_escape_table(c['short'])} |\n\n"
    head += "## 相关概念\n\n" + f"- {c.get('related','—')}\n"
    return head

def build():
    os.makedirs(os.path.join(BASE, "chapters"), exist_ok=True)
    os.makedirs(os.path.join(BASE, "concepts"), exist_ok=True)
    ch_manifest = []
    for c in CHAPTERS:
        cid = c["id"]
        fn = f"chapters/{cid}.md"
        open(os.path.join(BASE, fn), "w", encoding="utf-8").write(render_chapter(c))
        ch_manifest.append({
            "id": cid, "title": CH_TITLE[cid], "file": fn,
            "difficulty": int(c["difficulty"]),
            "source": {"file": "hello-ai.pdf", "page": PAGES[cid]},
            "prerequisites": CH_PREREQ[cid],
            "hours": c["hours"], "part": c["part"], "core": c["core"]
        })
    c_manifest = []
    for c in CONCEPTS:
        cid = c["id"]; fn = f"concepts/{cid}.md"
        open(os.path.join(BASE, fn), "w", encoding="utf-8").write(render_concept(c))
        item = {
            "id": cid, "title": c["title"], "file": fn,
            "chapterIds": [c["chapter"]], "difficulty": c["difficulty"],
            "source": {"file": "hello-ai.pdf", "page": PAGES[c["chapter"]].split("–")[0]},
            "prerequisites": c.get("prereq", []),
            "short": c["short"]
        }
        if cid in DEPTH:
            dfn = f"concepts/{cid}-depth.md"
            open(os.path.join(BASE, dfn), "w", encoding="utf-8").write(DEPTH[cid].strip() + "\n")
            item["depthFragment"] = dfn
        c_manifest.append(item)
    # glossary
    gl_manifest = []
    lines = ["# 术语表\n\n", "共 110 条，按原书章节顺序。定义经过零基础转译，英文对照保留。\n\n",
             "| 术语 | 英文 | 白话定义 | 章节 |\n|---|---|---|---|\n"]
    for g in GLOSSARY:
        ch = f"ch{g['chapter']:02d}" if int(g["chapter"]) <= 14 else ""
        lines.append(f"| {md_escape_table(g['term'])} | {md_escape_table(g['en'])} | {md_escape_table(g['def'])} | {md_escape_table(g['chapterTitle'])} |\n")
        gl_manifest.append({"term": g["term"], "def": g["def"], "chapterId": ch})
    open(os.path.join(BASE, "glossary.md"), "w", encoding="utf-8").write("".join(lines))
    # quiz md
    qlines = ["# 《Hello, AI · 人工智能导论》测验\n\n",
              "每章 5 道自测题，答案与解析附在题后；综合测验为 60 道单选题，可在学习伴侣中作答。\n"]
    qi = 0
    for c in CHAPTERS:
        qlines.append(f"\n## {CH_TITLE[c['id']]}\n\n")
        for i, q in enumerate(c["selfcheck"], 1):
            qlines.append(f"### Q{i}. {q['q']}\n- **答案**：{q['a']}\n- **解析**：{q['e']}\n\n")
    qlines.append("## 综合测验（60 题）\n\n")
    for q in QUIZZES:
        qi += 1
        qlines.append(f"### Q{qi}.（单选）{q['question']}\n")
        for oi, o in enumerate(q["options"]):
            qlines.append(f"- {'ABCD'[oi]}. {o}\n")
        qlines.append(f"**答案**：{'ABCD'[q['answer']]}  \n**解析**：{q['explain']}\n\n")
    qlines.append("## 最终检验\n\n选一个你熟悉的领域，写一份「AI 使用方案」：说明任务属于识别/预测/生成/决策哪一类，数据从哪来，怎样验证，哪里必须由人负责。评分要点：任务拆解清楚、验证方案可执行、责任边界明确。\n")
    open(os.path.join(BASE, "quiz.md"), "w", encoding="utf-8").write("".join(qlines))
    # flashcards
    fl = ["# 抽认卡\n\n", "正面只放问题，先自己回答再翻面。共 70 张：50 张概念卡 + 20 张章节锚点卡。\n"]
    f_manifest = []
    fi = 0
    for c in CONCEPTS:
        fi += 1
        fl.append(f"\n## {c['title']}\n### 卡片：用自己的话说，「{c['title']}」是什么、解决什么问题？\n- **背面**：{c['short']} {c['why']}\n- **标签**：{c['chapter']}, {c['difficulty']}\n- **章节**：{c['chapter']}\n")
        f_manifest.append({"id": f"f{fi:03d}", "chapterId": c["chapter"], "front": f"用自己的话说，「{c['title']}」是什么、解决什么问题？", "back": c["short"] + " " + c["why"], "tags": [c["chapter"], c["difficulty"]]})
    for c in CHAPTERS:
        fi += 1
        fl.append(f"\n## {CH_TITLE[c['id']]}\n### 卡片：{c['title']}这一章最该记住的一句话是什么？\n- **背面**：{c['core']}\n- **标签**：{c['id']}, 章节锚点\n- **章节**：{c['id']}\n")
        f_manifest.append({"id": f"f{fi:03d}", "chapterId": c["id"], "front": f"{c['title']}这一章最该记住的一句话是什么？", "back": c["core"], "tags": [c["id"], "章节锚点"]})
    open(os.path.join(BASE, "flashcards.md"), "w", encoding="utf-8").write("".join(fl))
    # quiz manifest
    qm = []
    for i, q in enumerate(QUIZZES, 1):
        item = {"id": f"q{i:02d}", "chapterId": q["chapterId"], "type": "single",
                "question": q["question"], "options": q["options"], "answer": q["answer"],
                "explain": q["explain"], "relatedConceptId": q["relatedConceptId"],
                "source": {"file": "hello-ai.pdf", "page": PAGES[q["chapterId"]]}}
        qm.append(item)
    # learning path
    path = [
      ("01","地图：AI 是什么、怎么走到今天","先建立判断框架，再看历史为什么起落。",["ch01","ch02"]),
      ("02","机器怎么学：搜索、规则、强化、监督","四种学习范式各有适用边界。",["ch03","ch04","ch05"]),
      ("03","神经网络：从神经元到表示学习","理解参数、梯度、反向传播和卷积。",["ch06"]),
      ("04","语言模型：token、注意力、Transformer","把「预测下一个词」拆到零件级。",["ch07","ch08"]),
      ("05","训练与对齐：预训练、SFT、RLHF","理解模型为什么会回答、会拒绝。",["ch09"]),
      ("06","可靠使用：幻觉、检索、校准","知道什么时候不能信它。",["ch10"]),
      ("07","多模态与智能体：从会说到会做","理解工具、循环、权限与责任。",["ch11","ch12"]),
      ("08","AI 做科学：AlphaFold 与边界","看 AI 能加速什么，不能替代什么。",["ch13"]),
      ("09","人的位置：提示、验证、责任","把 AI 放进工作流，而不是交给它。",["ch14"]),
      ("10","六个专题：应用现场与工程实操","把原理落到推荐、自动驾驶、科研与训练。",["t01","t02","t03","t04","t05","t06"]),
    ]
    lp = [{"step":s,"title":t,"chapterIds":ids,"checkpoint":f"完成 {'、'.join(ids)} 的自测题，正确率 ≥ 80%"} for s,t,_,ids in path]
    manifest = {
      "slug":"hello-ai","title":"Hello, AI · 人工智能导论","subtitle":"上海交通大学 AI+ 教育平台教材 · 零基础整书学习系统",
      "book":{"title":"Hello, AI · 人工智能导论","author":"上海交通大学 AI+ 教育平台","source":["hello-ai.pdf","219 页，14 章正文 + 6 篇专题 + 110 条术语"]},
      "audience":"零基础","goal":"把整本教材转译成可自学的路径：理解 AI 的基本概念、主流方法与真实应用，能判断何时可信、何时必须由人负责。",
      "learningPath":lp,"chapters":ch_manifest,"concepts":c_manifest,
      "glossary":gl_manifest,"patterns":{"file":"patterns.md"},"cheatsheet":{"file":"cheatsheet.md"},
      "quizzes":qm,"flashcards":f_manifest,"companion":"hello-ai学习伴侣.html"
    }
    json.dump(manifest, open(os.path.join(BASE,"manifest.json"),"w",encoding="utf-8"), ensure_ascii=False, indent=1)
    print("chapters",len(ch_manifest),"concepts",len(c_manifest),"depth",len([c for c in c_manifest if c.get("depthFragment")]),"quizzes",len(qm),"cards",len(f_manifest),"glossary",len(gl_manifest))

if __name__ == "__main__":
    build()
