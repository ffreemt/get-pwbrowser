import pytest
from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright
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
    yield page_

    browser.close()


@pytest.fixture
@pytest.mark.asyncio
async def page2():
    # with sync_playwright() as p:
    playwright = await async_playwright().start()

    browser = await playwright.chromium.launch()
    # context = browser.new_context()
    page_ = await browser.new_page()

    # page.goto("http://playwright.dev")
    # print(page.title())

    # return page_
    yield page_

    await browser.close()


@pytest.fixture
@pytest.mark.asyncio
async def browser1(scope="module"):  # session
    browser_ = await get_pwbrowser()
    # return browser_
    yield browser_
    await browser_.close()
