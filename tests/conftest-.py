import pytest
from playwright.sync_api import sync_playwright

from get_pwbrowser import get_pwbrowser


@pytest.fixture
def input_value():
    input = 39
    return input


@pytest.fixture
def page1():
    # with sync_playwright() as p:
    playwright = sync_playwright().start()

    browser = playwright.chromium.launch()
    # context = browser.new_context()
    page_ = browser.new_page()

    # page.goto("http://playwright.dev")
    # print(page.title())

    # return page_
    yeield page_

    browser.close()


_ = """
@pytest.fixture
@pytest.mark.asyncio
async def browser(scope="module"):  # session
    browser_ = await get_pwbrowser()
    # return browser_
    yield browser_
    await browser_.close()
# """