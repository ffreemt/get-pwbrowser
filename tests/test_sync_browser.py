"""Test sync pwbrowser."""
from get_pwbrowser import get_pwbrowser


def test_sync_browser(pwbrowser):
    """ sync pwbrowser."""
    page = pwbrowser.new_page()
    page.goto("http://www.baidu.com")
    assert "百度" in page.title()
    # print(page.title())
    # '百度一下，你就知道'
