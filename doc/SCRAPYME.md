# Scrapy
*Original Github Repo: github.com/scrapy/scrapy*

## Requirements
- Python 3.6+
- Works on Linux, Windows, macOS, BSD

## Documents
https://docs.scrapy.org/en/latest/

## Installation

    pip install scrapy

## Start a project
    scrapy startproject new_project

## Scrapy Project Structure
    crawler/
    ├── crawler/              # project's Python module
    │   ├── spiders/          # a directory containing the spiders
    │   |   ├── __init__.py
    │   ├── __init__.py
    │   ├── items.py          # project items definition file
    │   ├── middlewares.py    # project middlewares file
    │   ├── pipelines.py      # project pipelines file
    │   ├── settings.py       # project settings file
    └── scrapy.cfg            # deploy configuration file
