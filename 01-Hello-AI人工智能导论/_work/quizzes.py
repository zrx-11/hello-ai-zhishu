# -*- coding: utf-8 -*-
QUIZZES = [
# ch01
{"chapterId":"ch01","type":"single","question":"判断一个软件是不是 AI，本章建议先看什么？","options":["它用的是不是大模型","它做的任务是否需要通常由人承担的智能","它的代码是不是开源","它能不能自我意识"],"answer":1,"explain":"定义看任务，不看方法。大模型只是实现手段之一。","relatedConceptId":"c01"},
{"chapterId":"ch01","type":"single","question":"下列哪组包含关系是正确的？","options":["大模型 ⊃ 深度学习 ⊃ 机器学习 ⊃ AI","AI ⊃ 机器学习 ⊃ 深度学习 ⊃ 大模型","机器学习 ⊃ AI ⊃ 大模型 ⊃ 深度学习","AI ⊃ 大模型 ⊃ 机器学习 ⊃ 深度学习"],"answer":1,"explain":"AI 是最大的伞，逐层收窄到机器学习、深度学习、大模型。","relatedConceptId":"c02"},
{"chapterId":"ch01","type":"single","question":"手机相册搜索「猫」主要用到哪种能力？","options":["生成","决策","识别","强化学习"],"answer":2,"explain":"判断图像内容是不是猫，属于识别。","relatedConceptId":"c03"},
# ch02
{"chapterId":"ch02","type":"single","question":"两次 AI 寒冬的共同原因是什么？","options":["算法完全没有价值","承诺超过了当时数据与算力能兑现的能力","政府禁止研究","GPU 不够便宜"],"answer":1,"explain":"演示只在玩具问题上成立，却被说成通用智能，经费随后撤出。","relatedConceptId":"c04"},
{"chapterId":"ch02","type":"single","question":"2012 年 ImageNet 突破主要靠什么组合？","options":["数据、算力、算法三者同时到位","只有更聪明的算法","只有更多资金","只有更好的摄像头"],"answer":0,"explain":"大数据、GPU 算力、可训练的多层网络缺一不可。","relatedConceptId":"c06"},
{"chapterId":"ch02","type":"single","question":"规模定律说的是什么？","options":["模型越大越有意识","损失随参数、数据、计算增加按幂律可预测下降","数据越多一定越好","算法越复杂越省算力"],"answer":1,"explain":"在一定范围内，损失与规模呈幂律关系；它有边界。","relatedConceptId":"c05"},
# ch03
{"chapterId":"ch03","type":"single","question":"A* 中 f(n)=g(n)+h(n)，h(n) 是什么？","options":["从起点到 n 的实际代价","从 n 到终点的估计代价","n 的编号","随机噪声"],"answer":1,"explain":"g 是已走代价，h 是剩余代价的启发式估计。","relatedConceptId":"c07"},
{"chapterId":"ch03","type":"single","question":"规则系统最大的优点是？","options":["能自动学习所有规律","判断透明、可审计、可精确控制","不需要任何维护","能处理所有长尾"],"answer":1,"explain":"每条规则都能解释和关闭；缺点是写不完、难适应变化。","relatedConceptId":"c08"},
{"chapterId":"ch03","type":"single","question":"强化学习里的「探索」指的是？","options":["一直选当前最高奖励的动作","尝试未知动作以获取新信息","把奖励调大","把环境删掉"],"answer":1,"explain":"探索尝试未知，利用沿用已知有效动作，两者需要平衡。","relatedConceptId":"c09"},
# ch04
{"chapterId":"ch04","type":"single","question":"监督学习的关键特征是？","options":["数据带标签","数据完全无标签","模型必须很深","不需要损失函数"],"answer":0,"explain":"监督学习用带标签数据学从特征到标签的映射。","relatedConceptId":"c10"},
{"chapterId":"ch04","type":"single","question":"梯度下降更新参数的方向是？","options":["沿梯度上升方向","沿梯度下降方向","随机方向","固定向右"],"answer":1,"explain":"梯度指向上升最快方向，减去它是下降最快方向。","relatedConceptId":"c11"},
{"chapterId":"ch04","type":"single","question":"自监督学习怎样获得标签？","options":["请人逐条标注","从数据自身制造标签，如猜下一个词","完全不需要数据","用测试集当标签"],"answer":1,"explain":"遮词、续写等任务让数据自身成为监督信号。","relatedConceptId":"c12"},
# ch05
{"chapterId":"ch05","type":"single","question":"过拟合的典型表现是？","options":["训练和验证都差","训练好、验证差","训练差、验证好","训练和验证完全一样"],"answer":1,"explain":"模型背下了训练集噪声，换新数据就退化。","relatedConceptId":"c13"},
{"chapterId":"ch05","type":"single","question":"召回率回答的是哪一问？","options":["说有里的多少是真的","真的里的多少被找出","一共预测了多少","模型有多大"],"answer":1,"explain":"召回率 = TP/(TP+FN)，衡量漏报。","relatedConceptId":"c14"},
{"chapterId":"ch05","type":"single","question":"部署后数据分布变化导致性能下降，叫什么？","options":["过拟合","欠拟合","分布偏移","梯度消失"],"answer":2,"explain":"训练和部署数据不再来自同一个世界，叫分布偏移。","relatedConceptId":"c15"},
# ch06
{"chapterId":"ch06","type":"single","question":"神经网络为什么需要非线性激活函数？","options":["让模型更好看","没有它，多层网络会退化成线性变换","为了增加参数","为了省算力"],"answer":1,"explain":"线性层复合仍是线性，非线性才让深网络表达复杂函数。","relatedConceptId":"c16"},
{"chapterId":"ch06","type":"single","question":"卷积网络「权重共享」的作用是？","options":["让同一个探测器扫过所有位置，减少参数","让每个位置用不同参数","取消反向传播","增加图像分辨率"],"answer":0,"explain":"同一组权重在整张图上滑动，参数大幅减少并增强平移稳健性。","relatedConceptId":"c17"},
{"chapterId":"ch06","type":"single","question":"反向传播的核心数学工具是？","options":["傅里叶变换","链式法则","矩阵求逆","排序算法"],"answer":1,"explain":"链式法则把误差逐层乘回，一次算出全部梯度。","relatedConceptId":"c18"},
# ch07
{"chapterId":"ch07","type":"single","question":"BPE 分词的基本操作是？","options":["从整句开始不断切短","从字节开始反复合并高频相邻单元","随机切分","按标点切分"],"answer":1,"explain":"BPE 自底向上合并，得到词表。","relatedConceptId":"c19"},
{"chapterId":"ch07","type":"single","question":"词嵌入把 token 变成什么？","options":["一个整数编号","一个连续向量","一张图片","一条规则"],"answer":1,"explain":"嵌入是连续向量，用法相似的词向量靠近。","relatedConceptId":"c20"},
{"chapterId":"ch07","type":"single","question":"模型数不清 strawberry 里有几个 r，最直接的原因是？","options":["模型没有眼睛","它看到的是 token 编号，字母不是独立单位","训练数据没有这个词","模型太小"],"answer":1,"explain":"分词把词切成 token，字符级计数不是它的自然操作。","relatedConceptId":"c19"},
# ch08
{"chapterId":"ch08","type":"single","question":"自注意力里 Q、K、V 分别代表？","options":["查询、键、值","问题、知识、向量","质量、核、速度","队列、键、版本"],"answer":0,"explain":"Q 找信息，K 回答什么类型的问题，V 贡献内容。","relatedConceptId":"c21"},
{"chapterId":"ch08","type":"single","question":"Transformer 为什么需要位置编码？","options":["注意力本身不分词序","为了增加参数","为了压缩模型","为了让公式好看"],"answer":0,"explain":"没有位置信息，「猫追狗」和「狗追猫」会难以区分。","relatedConceptId":"c22"},
{"chapterId":"ch08","type":"single","question":"自回归生成的意思是？","options":["一次生成整段","每次预测一个 token，接回序列再预测下一个","随机抽一段训练文本","只生成标点"],"answer":1,"explain":"逐 token 生成，所以长回答要几百次前向计算。","relatedConceptId":"c23"},
# ch09
{"chapterId":"ch09","type":"single","question":"SFT 主要改变模型的什么？","options":["全部世界知识","对话格式与风格","分词表","硬件驱动"],"answer":1,"explain":"SFT 用示范对话教格式和风格，不擅长灌新知识。","relatedConceptId":"c24"},
{"chapterId":"ch09","type":"single","question":"DPO 相比 RLHF 的主要简化是？","options":["不需要任何数据","不需要奖励模型和 PPO，直接优化偏好对","不需要语言模型","不需要损失函数"],"answer":1,"explain":"DPO 把偏好对直接写成损失，训练更简单稳定。","relatedConceptId":"c25"},
{"chapterId":"ch09","type":"single","question":"思维链为什么能提高某些任务的表现？","options":["它让模型变小","它把中间步骤写进上下文，相当于给模型草稿纸","它删除了错误答案","它提高了温度"],"answer":1,"explain":"每步能看到前面的推理，减少一次性跳步。","relatedConceptId":"c26"},
# ch10
{"chapterId":"ch10","type":"single","question":"幻觉的根本来源是？","options":["训练目标只奖励「像下一个词」，不奖励「真」","模型内存太小","网络延迟","用户提问太长"],"answer":0,"explain":"最大似然目标匹配训练文本，不校验世界真实性。","relatedConceptId":"c27"},
{"chapterId":"ch10","type":"single","question":"RAG 为什么不能完全消除幻觉？","options":["检索可能漏、可能错，模型也可能误读","因为 RAG 需要付费","因为模型不支持中文","因为知识库一定正确"],"answer":0,"explain":"检索和阅读两步都可能出错，RAG 只降低概率。","relatedConceptId":"c28"},
{"chapterId":"ch10","type":"single","question":"「校准」指的是？","options":["模型输出的把握与实际正确率是否一致","模型有多少参数","模型跑得多快","模型支持多少语言"],"answer":0,"explain":"校准好，说 80% 把握时实际约 80% 正确。","relatedConceptId":"c29"},
# ch11
{"chapterId":"ch11","type":"single","question":"原生多模态模型怎样处理图像？","options":["先把图像转成一段文字描述","把图像切成 patch 向量，和文字 token 一起进 Transformer","只用图像分类器","把图像存进数据库"],"answer":1,"explain":"图像 patch 化后与文本共享注意力空间。","relatedConceptId":"c30"},
{"chapterId":"ch11","type":"single","question":"扩散模型训练时网络预测什么？","options":["清晰图像本身","被加进去的噪声","文字提示","下一张图"],"answer":1,"explain":"预测噪声，减去它就能逐步恢复清晰图。","relatedConceptId":"c31"},
{"chapterId":"ch11","type":"single","question":"工具调用让模型怎样？","options":["从「会说」扩展到「会做」","自动获得意识","不再需要训练","完全不会出错"],"answer":0,"explain":"模型输出特殊格式触发程序执行，结果回到上下文。","relatedConceptId":"c32"},
# ch12
{"chapterId":"ch12","type":"single","question":"智能体的可靠性主要取决于？","options":["模型参数量","驾具：上下文、权限、执行、验证、交付","用户打字速度","显卡品牌"],"answer":1,"explain":"长任务靠模型外的整套程序控制错误累积。","relatedConceptId":"c33"},
{"chapterId":"ch12","type":"single","question":"「最小权限」的意思是？","options":["只给完成任务必需的权限","给管理员权限最省事","完全不给权限","只给读权限永远不给写"],"answer":0,"explain":"权限越多，提示注入和误操作的损害越大。","relatedConceptId":"c34"},
{"chapterId":"ch12","type":"single","question":"模型说「已完成」但文件没写，属于哪种失败？","options":["假完成","过拟合","梯度消失","冷启动"],"answer":0,"explain":"必须独立验证产物，不能信模型自述。","relatedConceptId":"c33"},
# ch13
{"chapterId":"ch13","type":"single","question":"AlphaFold 属于哪种学习范式？","options":["监督学习","无监督学习","强化学习","规则系统"],"answer":0,"explain":"有实验结构作标签，有坐标误差作损失。","relatedConceptId":"c35"},
{"chapterId":"ch13","type":"single","question":"多序列比对（MSA）为什么有用？","options":["它提供进化保守和协同变化信息","它直接给出三维坐标","它替代实验","它压缩模型"],"answer":0,"explain":"同源序列里保守位点和协同变化位点携带结构线索。","relatedConceptId":"c35"},
{"chapterId":"ch13","type":"single","question":"AlphaFold 没有解决下列哪一项？","options":["单链蛋白静态结构","蛋白质动态构象与配体结合","序列到坐标的预测","残基置信度估计"],"answer":1,"explain":"它主要预测静态结构，动态、复合物、配体、功能仍待研究。","relatedConceptId":"c36"},
# ch14
{"chapterId":"ch14","type":"single","question":"提示词的本质是？","options":["咒语","给模型的全部上下文，塑造续写方向","模型参数","训练数据"],"answer":1,"explain":"提示词决定模型看到什么，不是神秘咒语。","relatedConceptId":"c37"},
{"chapterId":"ch14","type":"single","question":"AI 说一个事实，最稳妥的做法是？","options":["直接相信","查原始来源","看它语气自不自信","看回答长不长"],"answer":1,"explain":"语气自信不等于正确，关键事实必查。","relatedConceptId":"c38"},
{"chapterId":"ch14","type":"single","question":"数据最小化的核心是？","options":["只给任务必需的数据和权限","数据越多越好","把所有文件都上传","关闭所有安全设置"],"answer":0,"explain":"多给的每一份数据都是潜在风险。","relatedConceptId":"c39"},
# t01
{"chapterId":"t01","type":"single","question":"一次回答的流水线顺序是？","options":["分词→嵌入→层计算→概率→采样","采样→分词→训练→部署","嵌入→分词→采样→层计算","概率→分词→嵌入→采样"],"answer":0,"explain":"先切 token，再变向量，过几十层，算概率，采样。","relatedConceptId":"c40"},
{"chapterId":"t01","type":"single","question":"为什么回答的第一个字通常最慢？","options":["要处理完整提示并算完所有层","因为网络一定卡","因为第一个字最长","因为模型在休息"],"answer":0,"explain":"后续 token 可复用键值缓存，首 token 没有缓存。","relatedConceptId":"c40"},
{"chapterId":"t01","type":"single","question":"模型算错数字母类问题，最可能卡在哪个阶段？","options":["分词","采样","部署","UI 渲染"],"answer":0,"explain":"字母不是独立 token，模型看到的是编号。","relatedConceptId":"c40"},
# t02
{"chapterId":"t02","type":"single","question":"推荐系统最常优化的直接目标是？","options":["你的长期幸福","你对候选内容的互动概率","服务器温度","模型参数量"],"answer":1,"explain":"点击、停留等互动信号是训练目标，不等于长期满意。","relatedConceptId":"c41"},
{"chapterId":"t02","type":"single","question":"推荐系统「反馈循环」指什么？","options":["推荐改变行为，行为又变成训练数据","模型自动更新代码","用户手动标注","服务器定时重启"],"answer":0,"explain":"系统推荐什么，用户就可能点什么，点过的又进了训练集。","relatedConceptId":"c41"},
{"chapterId":"t02","type":"single","question":"冷启动的难点是？","options":["新用户/新内容没有历史数据","数据太多","模型太大","网速太慢"],"answer":0,"explain":"没有互动记录，只能靠内容特征和探索策略。","relatedConceptId":"c42"},
# t03
{"chapterId":"t03","type":"single","question":"自动驾驶的四个模块是？","options":["感知、预测、规划/决策、控制","训练、验证、部署、监控","分词、嵌入、注意力、采样","采集、标注、清洗、打包"],"answer":0,"explain":"四模块实时闭环，分别回答「看到什么、将发生什么、怎么走、怎么执行」。","relatedConceptId":"c43"},
{"chapterId":"t03","type":"single","question":"自动驾驶的长尾指的是？","options":["训练数据里极少出现却可能致命的罕见场景","车很长","路线很长","模型很老"],"answer":0,"explain":"穿玩偶服的人、掉落床垫等罕见场景，平均指标会掩盖。","relatedConceptId":"c44"},
{"chapterId":"t03","type":"single","question":"数据闭环的作用是？","options":["把车队遇到的新场景传回训练，再部署回车队","让车自动加油","关闭传感器","减少数据"],"answer":0,"explain":"部署不是终点，是下一轮数据的起点。","relatedConceptId":"c44"},
# t04
{"chapterId":"t04","type":"single","question":"科研机器学习的第一步是？","options":["选最深的模型","问清预测什么、错了代价是什么","先买 GPU","先写论文"],"answer":1,"explain":"从问题和代价开始，不是从模型开始。","relatedConceptId":"c45"},
{"chapterId":"t04","type":"single","question":"只有几百条科研数据时，优先考虑？","options":["从头训练千亿模型","树模型或预训练表示","放弃机器学习","只做可视化"],"answer":1,"explain":"小数据下树模型更稳、更省、更可解释。","relatedConceptId":"c45"},
{"chapterId":"t04","type":"single","question":"主动学习挑实验时优先选？","options":["模型最确定会好的样本","可能好且模型不确定的样本","最便宜的样本","最旧的样本"],"answer":1,"explain":"同时考虑「可能好」和「不知道」，一次实验获取最多信息。","relatedConceptId":"c46"},
# t05
{"chapterId":"t05","type":"single","question":"训练流水线中 SFT 之后通常是？","options":["分词器训练","偏好对齐/强化学习","数据抓取","部署"],"answer":1,"explain":"预训练→评测→SFT→偏好/RL→评测→部署。","relatedConceptId":"c47"},
{"chapterId":"t05","type":"single","question":"想给模型加本校规章，优先用什么？","options":["从头预训练","RAG 检索规章库","只调温度","换分词器"],"answer":1,"explain":"知识更新优先 RAG；微调主要改行为和格式。","relatedConceptId":"c48"},
{"chapterId":"t05","type":"single","question":"GRPO 适合什么任务？","options":["有可验证奖励的数学、代码","纯主观审美","无答案的闲聊","图像压缩"],"answer":0,"explain":"直接用答案对不对作奖励，绕过人类偏好模型。","relatedConceptId":"c47"},
# t06
{"chapterId":"t06","type":"single","question":"多数「开源模型」实际开放的是？","options":["代码、数据、权重全部","主要是权重和推理代码","只有论文","只有 Logo"],"answer":1,"explain":"训练数据和训练代码未必公开，准确说法是开放权重。","relatedConceptId":"c49"},
{"chapterId":"t06","type":"single","question":"开放权重最大的实际价值是？","options":["可微调、可审计、可离线部署","一定比闭源强","完全无版权限制","不需要算力"],"answer":0,"explain":"本领域数据微调成本远低于预训练。","relatedConceptId":"c49"},
{"chapterId":"t06","type":"single","question":"看到「开源模型」最该追问什么？","options":["开放的是代码、数据还是权重，许可证允许什么","模型图标好不好看","下载速度快不快","有没有中文名"],"answer":0,"explain":"「开源」标签不能代替许可证和数据来源。","relatedConceptId":"c50"}
]
