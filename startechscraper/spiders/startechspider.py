import scrapy

class StartechSpider(scrapy.Spider):
    name = 'startech'
    start_urls = ['https://www.startech.com.bd/laptop-notebook?filter_status=7']

    def parse(self, response):
        for products in response.css('div.p-item-details'):
            yield {
                'name': products.css('div.p-item-details h4.p-item-name a::text').get(),
                'price': products.css('div.p-item-price span::text').get().replace('৳',''),
                'link': products.css('div.p-item-details h4.p-item-name a').attrib['href'],
            }

        next_page = response.css('ul.pagination li a:contains("NEXT")::attr(href)').get()
        if next_page is not None: #If a next page exists then follow it
            yield response.follow(next_page, callback=self.parse)
