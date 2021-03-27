import asyncio
import pytest
from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright
from get_pwbrowser import get_pwbrowser_async as get_pwbrowser
from get_pwbrowser import get_pwbrowser as get_pwbrowser_sync


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

    yield browser_
    await browser_.close()


@pytest.fixture  # hard way
def loop_browser(scope="module"):
    try:
        loop = asyncio.get_running_loop()
    except Exception:
        loop = asyncio.get_event_loop()
        # logger.error(exc)
    finally:
        # loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    browser = loop.run_until_complete(get_pwbrowser())
    yield loop, browser

    print("closing up")
    loop.run_until_complete(browser.close())

    print(" is loop closed: %s" % loop.is_closed())

    loop.close()


@pytest.fixture  # sync
def pwbrowser(scope="session"):
    browser_ = get_pwbrowser_sync()

    yield browser_

    browser_.close()
