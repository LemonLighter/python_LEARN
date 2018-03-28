# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ExampleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class CountrySpider(CrawlSpider):
    name = 'country'
    allowed_domains = ['example.webscraping.com']
    start_urls = ['http://example.webscraping.com/']

    rules = (
        Rule(LinkExtractor(allow='/places/default/view/'), 
             callback='parse_item', follow=True),
        Rule(LinkExtractor(allow='/places/default/index/'), 
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = ExampleItem()
        name_css='tr#places_country__row td.w2p_fw::text'
        item['name']=response.css(name_css).extract()
        pop_css='tr#places_population__row td.w2p_fw::text'
        item['population']=response.css(pop_css).extract()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return item
