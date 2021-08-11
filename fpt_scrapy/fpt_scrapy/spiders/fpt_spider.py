from w3lib.url import url_query_cleaner
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# clean duplicate URLs
def process_links(links):
  for link in links:
    link.url = url_query_cleaner(link.url)
    yield link

class FptSpider(CrawlSpider):
  name = 'fpt'
  allowed_domains = ['www.fpt.com.vn']
  start_urls = ['https://www.fpt.com.vn/']
  rules = (
    Rule(
      LinkExtractor(),
      process_links = process_links,
      callback = 'parse_item',
      follow = True
    ),
  )
  
  # output the traversed URLs
  def parse_item(self, response):
    return { 'url': response.url }