"""Test with loop fixture.

https://playwright.dev/python/docs/test-runners#usage
# async def test_example2(page2):
    ’‘’Async example.

    playwright = await async_playwright().start()
    if 1:
    await playwright.stop()
    ‘’‘
"""
import asyncio
import pytest
from playwright.async_api import async_playwright

# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


@pytest.mark.asyncio
async def test_hardway(loop_browser):
    loop, browser = loop_browser
    asyncio.set_event_loop(loop)

    # browser = await playwright.chromium.launch()

    page = await browser.new_page()

    await page.goto("https://httpbin.org/", timeout=60 * 1000)
    content = await page.text_content("h2")
    assert "httpbin" in content
