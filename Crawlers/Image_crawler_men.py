from bs4 import BeautifulSoup
import scrapy
import re
import json
import uuid
import requests

class AsosSpider(scrapy.Spider):
    name = "Asos"
    def start_requests(self):
#         start_urls = [
# 'http://us.asos.com/river-island/river-island-buckle-faux-leather-pencil-skirt/prd/9088138?clr=black&cid=2623&pgesize=36&pge=0&totalstyles=933&gridsize=4&gridrow=1&gridcolumn=1',
#             'http://us.asos.com/asos/asos-knight-wide-fit-stretch-over-the-knee-boots/prd/8329922?clr=black&cid=4172&pgesize=36&pge=0&totalstyles=2828&gridsize=4&gridrow=1&gridcolumn=2'
#         ]
        start_urls=['http://us.asos.com/men/new-in/new-in-clothing/cat/?cid=6993&pgesize=204',
                    'http://us.asos.com/men/new-in/new-in-clothing/cat/?cid=6993&pge=1&pgesize=204',
                    'http://us.asos.com/men/new-in/new-in-clothing/cat/?cid=6993&pge=2&pgesize=204',
                    'http://us.asos.com/men/new-in/new-in-clothing/cat/?cid=6993&pge=3&pgesize=204',
                    'http://us.asos.com/men/new-in/new-in-clothing/cat/?cid=6993&pge=4&pgesize=204'
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=1&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=2&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=3&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=4&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=5&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=6&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=7&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=8&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=9&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=10&pgesize=204'
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=11&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=12&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=13&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=14&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=15&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=16&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=17&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=18&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=19&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=20&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=21&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=22&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=23&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=24&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=25&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=26&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=27&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=28&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=29&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=30&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=10&pgesize=204'
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=11&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=12&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=13&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=14&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=15&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=16&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=17&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=18&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=19&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=20&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=21&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=22&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=23&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=24&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=25&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=26&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=27&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=28&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=29&pgesize=204',
                    # 'http://us.asos.com/women/dresses/cat/?cid=8799&pge=30&pgesize=204'

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
        #prod_details=response.xpath('//script[contains(., "variants")]/text()')
        #price_pattern = re.compile(r"price\":?\{([^}]*)", re.MULTILINE | re.DOTALL)
        #pattern = re.compile(r"variants\":?\[([^]]*)", re.MULTILINE | re.DOTALL)
        #color_pattern=re.compile(r"colourImageMap\":?\{([^}]*)",re.MULTILINE|re.DOTALL)
        #colr_dicts= prod_details.re(color_pattern)[0].split(":")[0].strip('"')
        #size_dicts=json.loads('[' + prod_details.re(pattern)[0] + ']')
        #price_dicts=json.loads('{'+prod_details.re(price_pattern)[0]+'}')
        #size_array = [variant['size'] for variant in size_dicts]

        #print(size_array)
        img_urls=[i.split('?')[0] for i in response.css('.thumbnails').xpath('.//img/@src').extract()]
        for url in img_urls:
            id= uuid.uuid4()
            # URL of the image to be downloaded
            r = requests.get(url)  # create HTTP response object


            with open("./data/men/"+str(id)+".png", 'wb') as f:
                # Saving received content as a png file in
                # binary format

                # write the contents of the response (r.content)
                # to a new file in binary mode.
                f.write(r.content)
            yield{

                    'image_id': str(id),
                    'gender': 'male'

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