"""Test httpbin."""
import asyncio
import re
import pytest
from get_pwbrowser import get_pwbrowser


@pytest.fixture
@pytest.mark.asyncio
# async def browser(scope="module"):  # session
async def browser():  # session
    browser_ = await get_pwbrowser()
    # return browser_
    yield browser_
    await browser_.close()


@pytest.mark.skip("need to fix 'event closed'")
@pytest.mark.asyncio
async def test_httpbin_(browser):
    """Test httpbin."""
    assert True
    # assert False

    page = await browser.new_page()
    await page.goto("http://httpbin.org/ip")
    content = await page.text_content("text=/origin/")
    assert re.findall(r"\d+", content)

    # temp fix: prbbaly need to do something in conftext.py
    # or use playwright's pytest plugin
    # TODO
    await browser.close()

# @pytest.mark.skip("need a fix")
@pytest.mark.asyncio
async def test_httpbin(browser):
    """Test httpbin."""

    # browser = await get_pwbrowser()

    page = await browser.new_page()
    await page.goto("http://httpbin.org/ip")
    content = await page.text_content("text=/origin/")

    assert re.findall(r"\d+", content)

    await page.close()
    await browser.close()


@pytest.mark.skip("still event closed problem")
def test_httpbin_():
    """Test httpbin."""
    async def test_():
        browser = await get_pwbrowser()

        page = await browser.new_page()
        await page.goto("http://httpbin.org/ip")
        content = await page.text_content("text=/origin/")

        assert re.findall(r"\d+", content)

        await page.close()
        await browser.close()

    asyncio.run(test_())

    _ = """
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(test_())
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()
    # """
