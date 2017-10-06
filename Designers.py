import scrapy

class StoresSpider(scrapy.Spider):
    name = "stores"
    start_urls = [
        'https://www.lyst.com/sitemap/designers/',
    ]

    def parse(self, response):
        # for brand_block in response.css('div.az-block__items'):
        #     for brand in brand_block.css('a::text').extract():
        #         yield {
        #             'text': brand.css('a::text').extract_first(),
        #
        #         }
        for brand in response.css('a'):
            yield {
                            "designer": brand.css('a::text').extract_first(),

                        }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)


