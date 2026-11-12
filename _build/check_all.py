import asyncio, json
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/local/bin/chromium")
        page=await b.new_page(viewport={"width":1440,"height":1000})
        errs=[]; page.on("console", lambda m: errs.append(m.text) if m.type=="error" else None)
        await page.goto("file:///home/user/Doubao/chats/38453413604796930/HelloAI学习系统/index.html")
        await page.wait_for_timeout(1000)
        chapters=await page.evaluate("BOOKS['hello-ai'].manifest.chapters.map(c=>c.id)")
        bad=[]
        for cid in chapters:
            await page.evaluate(f"location.hash='#/book/hello-ai/chapter/{cid}'")
            await page.wait_for_timeout(2600)
            raw=await page.eval_on_selector_all(".mermaid","els=>els.length")
            svg=await page.eval_on_selector_all(".mermaid svg","els=>els.length")
            if raw and not svg: bad.append((cid,raw,svg))
        print("mermaid chapters:",len(chapters),"bad:",bad)
        concepts=await page.evaluate("BOOKS['hello-ai'].manifest.concepts.map(c=>[c.id,!!c.depthFragment])")
        dbad=[]; kbad=[]
        for cid,hasd in concepts:
            await page.evaluate(f"location.hash='#/book/hello-ai/concept/{cid}'")
            await page.wait_for_timeout(400)
            d=await page.eval_on_selector_all("details.depth-fragment","els=>els.length")
            k=await page.eval_on_selector_all(".katex","els=>els.length")
            if hasd and d!=1: dbad.append(cid)
            if hasd and k<10: kbad.append((cid,k))
        print("depth bad:",dbad,"low katex:",kbad)
        print("console errors:",len(errs),errs[:5])
        # companion check
        page2=await b.new_page(viewport={"width":390,"height":844})
        await page2.goto("file:///home/user/Doubao/chats/38453413604796930/HelloAI学习系统/01-Hello-AI人工智能导论/hello-ai学习伴侣.html")
        await page2.wait_for_timeout(1000)
        await page2.evaluate("location.hash='#/concept/c11'")
        await page2.wait_for_timeout(1200)
        print("companion depth:",await page2.eval_on_selector_all("details.depth-fragment","els=>els.length"),
              "katex:",await page2.eval_on_selector_all(".katex","els=>els.length"))
        box=await page2.eval_on_selector(".main","el=>{const r=el.getBoundingClientRect();return {x:r.x,right:r.x+r.width,padL:getComputedStyle(el).paddingLeft}}")
        print("companion mobile main:",box)
        print("companion body scroll:",await page2.evaluate("document.documentElement.scrollWidth"),"vw:",await page2.evaluate("innerWidth"))
        await b.close()

asyncio.run(main())
