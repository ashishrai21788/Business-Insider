# -*- coding: utf-8 -*-
import scrapy


class BusinessSpider(scrapy.Spider):
    name = 'business'
    allowed_domains = ['www.businessinsider.in']
    start_urls = ['http://www.businessinsider.in/']

    def parse(self, response):
        for business_url in response.css("li > h3.story-headline > a ::attr(href)").extract():
            yield scrapy.Request(response.urljoin(business_url), callback=self.parse_detail_page)
    
    def parse_detail_page(self, response):
        headline = response.css("div.mobile_padding").extract_first()
        author = response.css("span.foreign_author").extract_first()
        item = {}
        item['headline'] = headline
        item['author'] = author
        item['url'] = response.url
        yield item
