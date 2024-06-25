import scrapy
import json

class MarksAndSpencerSpider(scrapy.Spider):
    name = "marksandspencer"
    allowed_domains = ["marksandspencer.com"]
    start_urls = [
        'https://www.marksandspencer.com/bg/easy-iron-geometric-print-shirt/p/P60639302.html'
    ]

    def parse(self, response):
        product = {
            "name": response.xpath('//h1[@class="product-name"]/text()').get(default="Name not found").strip(),
            "price": float(response.xpath('//span[contains(@class, "price")]/text()').re_first(r'(\d+\.\d+)') or 0.0),
            "colour": response.xpath('//span[contains(@class, "colour")]/text()').get(default="Colour not found").strip(),
            "size": response.xpath('//ul[contains(@class, "sizes")]/li/text()').getall(),
            "reviews_count": int(response.xpath('//span[@class="reviews-count"]/text()').re_first(r'\d+') or 0),
            "reviews_score": float(response.xpath('//span[@class="reviews-score"]/text()').re_first(r'\d+\.\d+') or 0.0),
        }

        with open('product_data.json', 'w') as f:
            json.dump(product, f, indent=4)

        self.log("Saved file product_data.json")

