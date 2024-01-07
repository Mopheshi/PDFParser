import scrapy


class CustomSpider(scrapy.Spider):
    name = 'spider'

    def start_requests(self):
        url = 'https://hbb.global.bible/bible/d16d2d28eeeb9953-01/MAT.1'
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        for content in response.css('#current-chapter-col'):
            name = content.css('#current-chapter-col > div.sc-qYiqT.eFjzzg::text').get()
            newText = '\n'.join(content.css('#scripture > p:nth-child(2) > span:nth-child(2)::text').getall())

            yield {
                'name': name,
                'newText': newText
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
