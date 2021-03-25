# pack_name
<!--- repo_name  pack_name  mod_name func_name --->
[![tests](https://github.com/ffreemt/repo_name/actions/workflows/routine-tests.yml/badge.svg)][![python](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/pack_name.svg)](https://badge.fury.io/py/pack_name)

scrape deepl using pyppeteer

## Usage

```python
from pack_name.mod_name import func_name

res = await func_name("test me")
print(res)
# '考我 试探我 测试我 试探'

print(await func_name("test me", to_lang="de"))