import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import colorama

URL = "https://fpt.com.vn"

colorama.init()
INTERNAL_LINK = colorama.Fore.CYAN
EXTERNAL_LINK = colorama.Fore.MAGENTA
RESET = colorama.Fore.RESET
CRAWLING_LINK = colorama.Fore.YELLOW

# initialize the set of links (unique links)
internal_urls = set()
external_urls = set()

def is_valid(url):
    # check if url is valid
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def get_all_website_links(url):
    # all URLs of `url`
    urls = set()
    # domain name of the URL without the protocol
    domain_name = urlparse(url).netloc
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None or href.startswith("http") == 0:
            # href empty tag
            continue
        # join the URL if it's relative (not absolute link)
        href = urljoin(url, href)
        parsed_href = urlparse(href)
        # remove URL GET parameters, URL fragments, etc.
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if not is_valid(href):
            # not a valid URL
            continue
        if href in internal_urls:
            # already in the set
            continue
        if domain_name not in href:
            # external link
            if href not in external_urls:
                print(f"{EXTERNAL_LINK}External link: {href}{RESET}")
                external_urls.add(href)
            continue
        print(f"{INTERNAL_LINK}Internal link: {href}{RESET}")
        urls.add(href)
        internal_urls.add(href)
    return urls

# number of urls visited
total_urls_visited = 0
max_urls = 100

def crawl(url, max_urls=100):
    # crawl a web page and get all links with limited urls crawled
    global total_urls_visited
    total_urls_visited += 1
    print(f"{CRAWLING_LINK}Crawling: {url}{RESET}")
    links = get_all_website_links(url)
    for link in links:
        if total_urls_visited > max_urls:
            break
        crawl(link, max_urls=max_urls)


if __name__ == "__main__":
    crawl(URL)
    print("Total Internal links:", len(internal_urls))
    print("Total External links:", len(external_urls))
    print("Total URLs:", len(external_urls) + len(internal_urls))
    print("Total crawled URLs:", max_urls)
