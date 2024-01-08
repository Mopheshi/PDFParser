import scrapy


class CustomSpider(scrapy.Spider):
    name = 'spider'
    url = ['https://hbb.global.bible/bible/d16d2d28eeeb9953-01/MAT.1']

    def parse(self, response):
        data = {
            "name": response.css('.sc-qYiqT.eFjzzg::text').get(),
            "newText": "\n".join(response.css('.sc-fzomME.glcNSq .verse-span::text').getall())
        }
        yield data

        next_page = response('.next a::attr("href")').extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), )
