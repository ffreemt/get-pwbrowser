# get-pwbrowser
<!--- get-pwbrowser  get_pwbrowser  get_pwbrowser get_pwbrowser --->
[![tests](https://github.com/ffreemt/get-pwbrowser/actions/workflows/routine-tests.yml/badge.svg)][![python](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/get_pwbrowser.svg)](https://badge.fury.io/py/get_pwbrowser)

instantiate a playwright chromium browser

## Installation
```bash
pip install git+https://github.com/ffreemt/get-pwbrowser.git
```
or
```bash
poetry add git+https://github.com/ffreemt/get-pwbrowser.git
```

## Usage

```python
from get_pwbrowser import get_pwbrowser

browser = await get_pwbrowser()
page = await browser.new_page()
await page.goto("http://www.baidu.com")
print(await page.title())
# '百度一下，你就知道'

await browser.close()
```

## `.env` and `os.environ`

`HEADFUL`, `DEBUG` and `PROXY` can be set in shell environ or in .env with prefix `PWBROWSER_`.

e.g., `set PWBROWSER_HEADFUL=1` in Windows or `export PWBROWSER_HEADFUL=1` in Linux and freinds)

or in `.env`
```bash
# .env
PWBROWSER_HEADFUL=1
```
