import scrapy
import re
import json
import uuid
import requests
#define spider as class
class AsosSpider(scrapy.Spider):
    #Naming the spider helps in logging
    name = "Asos"
    def start_requests(self):
    #The list of URLs for starting to crawl. These are pages that have multiple products
        start_urls=['http://us.asos.com/women/swimwear-beachwear/cat/?cid=2238&refine=brand:3098,3029,589,105&currentpricerange=5-400&pgesize=204'
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
        id=uuid.uuid4()
        image_url = response.css('.thumbnails').xpath('.//img/@src').extract_first().split('?')[0]
        designer= response.css('.brand-description').xpath('.//strong/text()').extract_first()
        r = requests.get(image_url)  # create HTTP response object

        with open("./data/skin/"+designer+"_" + str(id) + ".png", 'wb') as f:
            # Saving received content as a png file in
            # binary format

            # write the contents of the response (r.content)
            # to a new file in binary mode.
            f.write(r.content)
        #helps the
        yield{

             'designer': response.css('.brand-description').xpath('.//strong/text()').extract_first(),
             'img_url': image_url,
             'id':str(id)

        }


