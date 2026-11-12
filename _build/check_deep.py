import asyncio, json, sys
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/local/bin/chromium")
        page = await b.new_page(viewport={"width":1440,"height":1000})
        errors=[]
        page.on("console", lambda m: errors.append(m.text) if m.type=="error" else None)
        await page.goto("file:///home/user/Doubao/chats/38453413604796930/HelloAI学习系统/index.html")
        await page.wait_for_timeout(1200)
        # concept c11
        await page.evaluate("location.hash='#/book/hello-ai/concept/c11'")
        await page.wait_for_timeout(1000)
        n = await page.eval_on_selector_all("details.depth-fragment", "els=>els.length")
        print("depth details:", n)
        if n:
            await page.click("details.depth-fragment > summary")
            await page.wait_for_timeout(400)
            opened = await page.eval_on_selector("details.depth-fragment", "el=>el.open")
            txt = await page.inner_text("details.depth-fragment")
            print("depth open:", opened, "chars:", len(txt), "has 梯度:", "梯度" in txt)
        katex = await page.eval_on_selector_all(".katex", "els=>els.length")
        print("katex elements:", katex)
        # concept c21
        await page.evaluate("location.hash='#/book/hello-ai/concept/c21'")
        await page.wait_for_timeout(800)
        print("c21 depth:", await page.eval_on_selector_all("details.depth-fragment","els=>els.length"))
        # mermaid on chapter
        await page.evaluate("location.hash='#/book/hello-ai/chapter/ch01'")
        await page.wait_for_timeout(3500)
        print("mermaid svg:", await page.eval_on_selector_all(".mermaid svg","els=>els.length"),
              "mermaid raw:", await page.eval_on_selector_all(".mermaid","els=>els.length"))
        # desktop main padding
        box = await page.eval_on_selector(".main", "el=>{const r=el.getBoundingClientRect();return {x:r.x,w:r.width,padL:getComputedStyle(el).paddingLeft,padR:getComputedStyle(el).paddingRight}}")
        print("desktop main:", box)
        print("desktop body scroll:", await page.evaluate("document.documentElement.scrollWidth"), "vw:", await page.evaluate("innerWidth"))
        # mobile
        await page.set_viewport_size({"width":390,"height":844})
        await page.evaluate("location.hash='#/book/hello-ai/chapter/ch08'")
        await page.wait_for_timeout(1200)
        box2 = await page.eval_on_selector(".main", "el=>{const r=el.getBoundingClientRect();return {x:r.x,right:r.x+r.width,padL:getComputedStyle(el).paddingLeft,padR:getComputedStyle(el).paddingRight}}")
        print("mobile main:", box2)
        print("mobile body scroll:", await page.evaluate("document.documentElement.scrollWidth"), "vw:", await page.evaluate("innerWidth"))
        tables = await page.eval_on_selector_all("table", "els=>els.map(e=>({sw:e.scrollWidth,cw:e.clientWidth}))")
        print("mobile tables overflow:", [t for t in tables if t['sw']>t['cw']+2])
        # screenshot
        await page.screenshot(path="_build/mobile.png")
        await page.set_viewport_size({"width":1440,"height":1000})
        await page.evaluate("location.hash='#/book/hello-ai/concept/c11'")
        await page.wait_for_timeout(800)
        if await page.eval_on_selector_all("details.depth-fragment","els=>els.length"):
            await page.click("details.depth-fragment > summary")
            await page.wait_for_timeout(300)
        await page.screenshot(path="_build/desktop-depth.png")
        print("console errors:", errors[:5], "count:", len(errors))
        await b.close()

asyncio.run(main())
