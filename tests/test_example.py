"""Test example.

https://playwright.dev/python/docs/test-runners#usage
"""

def test_example(page1):
    """Test example."""
    page1.goto("https://httpbin.org/")
    content = page1.text_content("h2")
    assert "httpbin" in content

    # assert "httpbin" in page.innerText('h2')
    # page1.click("text=More information")
