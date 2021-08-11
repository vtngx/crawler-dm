# Spidy
*Original Github Repo: github.com/rivermont/spidy*

## How it works
Spidy has two working lists, `TODO` and `DONE`.

- `TODO`: list of URLs hasn't yet visited.
- `DONE`: list of URLs has already been to.

The crawler visits each page in `TODO`, scrapes the DOM of the page for links, and adds those back into `TODO`. After scrapping all the links, the page is considered checked and add to `DONE`

## Installation
### From PyPI

    pip install spidy-web-crawler

### From Source

    git clone https://github.com/rivermont/spidy.git
    cd spidy/
    pip install -r requirements.txt

## Running

### Config
From the `config/` directory, select/make your suitable configuration.

### Launch

    cd spidy/
    python3 crawler.py
  
It then will ask you to select your configuration.

### Force Quit
Sample log after performing a `^C` to force quit the crawler.