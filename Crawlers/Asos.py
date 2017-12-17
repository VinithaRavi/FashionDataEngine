import scrapy
import re
import json
#define spider as class
class AsosSpider(scrapy.Spider):
    #Naming the spider helps in logging
    name = "Asos"
    def start_requests(self):
    #The list of URLs for starting to crawl. These are pages that have multiple products
        start_urls=['http://us.asos.com/women/new-in/new-in-clothing/cat/?cid=2623&pgesize=204',
                    'http://us.asos.com/women/new-in/new-in-clothing/cat/?cid=2623&pge=1&pgesize=204',
                    'http://us.asos.com/women/new-in/new-in-clothing/cat/?cid=2623&pge=2&pgesize=204',
                    'http://us.asos.com/women/new-in/new-in-clothing/cat/?cid=2623&pge=3&pgesize=204',
                    'http://us.asos.com/women/new-in/new-in-clothing/cat/?cid=2623&pge=4&pgesize=204'
                    ]
        try:
            for url in start_urls:
                yield scrapy.Request(url=url, callback=self.parse)
        except:
            #Helps in knowing if any of the URLs throw an error
            print(url)


    def parse(self,response):
        #identify each product and spawn a separate thread to parse the product page
        #This will have to be changed depending on the website
        product_urls=response.css('.product.product-link').xpath('@href').extract()
        for product in product_urls:
            #Crawl each product
            yield scrapy.Request(url=product, callback=self.parse_product)


    def parse_product(self, response):
        #Identify each key
        prod_details=response.xpath('//script[contains(., "variants")]/text()')
        price_pattern = re.compile(r"price\":?\{([^}]*)", re.MULTILINE | re.DOTALL)
        pattern = re.compile(r"variants\":?\[([^]]*)", re.MULTILINE | re.DOTALL)
        color_pattern=re.compile(r"colourImageMap\":?\{([^}]*)",re.MULTILINE|re.DOTALL)
        colr_dicts= prod_details.re(color_pattern)[0].split(":")[0].strip('"')
        size_dicts=json.loads('[' + prod_details.re(pattern)[0] + ']')
        price_dicts=json.loads('{'+prod_details.re(price_pattern)[0]+'}')
        size_array = [variant['size'] for variant in size_dicts]
        #helps the
        yield{
            'name':response.css('title::text').extract_first(),
            'description':''.join(response.css('.product-description').xpath('.//li/text()').extract()),
             'url':response.url,
             'price':'$'+str(price_dicts['current']),
             'size':size_array,
             'color':colr_dicts,
             'details':str(response.xpath('//span/text()').extract()) ,
             'designer': response.css('.brand-description').xpath('.//strong/text()').extract_first(),
             'image_urls': [i.split('?')[0] for i in response.css('.thumbnails').xpath('.//img/@src').extract()],
             'gender':'women'

        }


