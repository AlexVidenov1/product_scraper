import scrapy
import json

class MarksAndSpencerSpider(scrapy.Spider):
    name = 'marksandspencer'
    allowed_domains = ['marksandspencer.com']
    start_urls = ['https://www.marksandspencer.com/bg/easy-iron-geometric-print-shirt/p/P60639302.html']

    def parse(self, response):
        product_data = {
            "name": response.xpath('//h1[@class="product-details-tile__title"]/text()').get(),
            "price": float(response.xpath('//span[@class="price"]/text()').re_first(r'[\d.]+')),
            "colour": response.xpath('//span[@class="product-colour"]/text()').get().strip(),
            "size": response.xpath('//li[@class="product-sizes__item"]/text()').getall(),
            "reviews_count": int(response.xpath('//span[@class="reviews-count"]/text()').re_first(r'\d+')),
            "reviews_score": float(response.xpath('//div[@class="product-reviews-summary__rating"]/text()').re_first(r'[\d.]+'))
        }

        with open('product_data.json', 'w') as json_file:
            json.dump(product_data, json_file)

        self.log('Saved file product_data.json')
