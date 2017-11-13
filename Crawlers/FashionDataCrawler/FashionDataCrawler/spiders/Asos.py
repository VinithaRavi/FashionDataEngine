from bs4 import BeautifulSoup
import scrapy
import re
import json

class AsosSpider(scrapy.Spider):
    name = "Asos"
    def start_requests(self):
#         start_urls = [
# 'http://us.asos.com/river-island/river-island-buckle-faux-leather-pencil-skirt/prd/9088138?clr=black&cid=2623&pgesize=36&pge=0&totalstyles=933&gridsize=4&gridrow=1&gridcolumn=1',
#             'http://us.asos.com/asos/asos-knight-wide-fit-stretch-over-the-knee-boots/prd/8329922?clr=black&cid=4172&pgesize=36&pge=0&totalstyles=2828&gridsize=4&gridrow=1&gridcolumn=2'
#         ]
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
            print(url)


    def parse(self,response):
        product_urls=response.css('.product.product-link').xpath('@href').extract()
        for product in product_urls:
            yield scrapy.Request(url=product, callback=self.parse_product)


    def parse_product(self, response):
        prod_details=response.xpath('//script[contains(., "variants")]/text()')
        price_pattern = re.compile(r"price\":?\{([^}]*)", re.MULTILINE | re.DOTALL)
        pattern = re.compile(r"variants\":?\[([^]]*)", re.MULTILINE | re.DOTALL)
        color_pattern=re.compile(r"colourImageMap\":?\{([^}]*)",re.MULTILINE|re.DOTALL)
        colr_dicts= prod_details.re(color_pattern)[0].split(":")[0]
        size_dicts=json.loads('[' + prod_details.re(pattern)[0] + ']')
        price_dicts=json.loads('{'+prod_details.re(price_pattern)[0]+'}')
        size_array = [variant['size'] for variant in size_dicts]
        #print(size_array)
        yield{
            'name':response.css('title::text').extract_first(),
            'description':''.join(response.css('.product-description').xpath('.//li/text()').extract() )     ,
             'url':response.url,
             'price':'$'+str(price_dicts['current']),
             'size':size_array,
             'color':colr_dicts,
             'details':str(response.xpath('//span/text()').extract()) ,
             'designer': response.css('.brand-description').xpath('.//strong/text()').extract_first(),
             'image_urls': [i.split('?')[0] for i in response.css('.thumbnails').xpath('.//img/@src').extract()],
            'gender':'women'

        }
        #print(product_name, url)


        # for brand_block in response.css('div.az-block__items'):
        #     for brand in brand_block.css('a::text').extract():
        #         yield {
        #             'text': brand.css('a::text').extract_first(),
        #
        #         }
        # for brand in response.css('a'):
        #     yield {
        #                     "brand": brand.css('a::text').extract_first(),
        #
        #                 }
        #
        # next_page = response.css('li.next a::attr("href")').extract_first()
        # if next_page is not None:#\(.*?data: ({.*?}),\W+adPriceRanges data = response.xpath("//script[contains(., 'Pages/FullProduct')]/text()").re(pattern)[0]
        #     pattern = re.compile(
        #         r"Pages/FullProduct",
        #         re.MULTILINE | re.DOTALL)
        #     yield response.follow(next_page, self.parse)