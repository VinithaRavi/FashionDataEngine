#Template for crawling Brands (Ralph lauren)
#The  data is present in the javascript.


from bs4 import BeautifulSoup
import scrapy
import re
import json

class RalphLaurenSpider(scrapy.Spider):
    name = "RalphLauren"
    def start_requests(self):

        start_urls=['https://www.ralphlauren.com/women-clothing-shop-new-arrivals?webcat=women%7Cfeatured%7CNew%20Arrivals',
                    #'https://www.ralphlauren.com/men-clothing-shop-new-arrivals-cg?srule=new-arrivals&sz=60&start=0'

                    ]
        try:
            for url in start_urls:
                yield scrapy.Request(url=url, callback=self.parse)
        except:
            print(url)


    def parse(self,response):
        product_urls=response.css('.name-link').xpath('@href').extract()
        for product in product_urls:
        #product="https://www.ralphlauren.com/men-clothing-shop-new-arrivals-cg/paneled-merino-wool-sweater/421258.html?cgid=men-clothing-shop-new-arrivals-cg&dwvar421258_colorname=Blackwatch&webcat=men%2Ffeature%2FNew%20Arrivals#start=1&cgid=men-clothing-shop-new-arrivals-cg"
            yield scrapy.Request(url="https://www.ralphlauren.com/"+product, callback=self.parse_product)


    def parse_product(self, response):
        img_details=response.xpath('//script[contains(., "oldSet")]/text()')
        img_pattern = re.compile(r"http[s]?:\/\/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", re.MULTILINE | re.DOTALL)
        colr_dicts= img_details.re(img_pattern)[0]
        imgs=[]
        imgs.append(colr_dicts)
        yield{
            'name':response.css('title::text').extract_first(),
            'description':''.join(response.css('.product-content-section').xpath('.//li/text()').extract()),
             'url':response.css('span[itemprop="url"]::text').extract_first(),
             'price':response.css('span[class="price-sales no-promotion"]::text').extract_first(),
             'size':[i.strip()for i in set(response.css('.primarysize').xpath('.//li/a/text()').extract())],
             'color':response.css('.product-variations').xpath('.//img/@alt').extract(),
             'details':str(response.xpath('//span/text()').extract()) ,
             'designer': 'Ralph Lauren',
             'image_urls': imgs,
            'gender':'women'

        }
