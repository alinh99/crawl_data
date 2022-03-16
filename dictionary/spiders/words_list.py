import scrapy


class WordsListSpider(scrapy.Spider):
    name = 'words_list'
    allowed_domains = ['www.dictionary4it.com']

    start_urls = []
    custom_settings = {'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
                       'DEPTH_PRIORITY': 1,
                       }

    def __init__(self):
        url_definition = 'https://www.dictionary4it.com/term/page/'
        for page in range(1, 65):
            self.start_urls.append(url_definition + str(page))

    def parse(self, response):
        print("procesing:" + response.url)
        for link in response.css('li.category-item a::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_category, priority=1)


    def parse_category(self, response):
        words_list = response.css('div#dictionary__left')
        definitions = response.css('div.dictionary__mean')
        explains = response.css('div.dictionary__explain')
        for w_l in words_list:
            if definitions:
                for definition in definitions:
                    yield {
                        'words': w_l.css('span.dictionary__word::text').get().strip(),
                        'definition': definition.css('span').get().strip()
                    }
            else:
                for explain in explains:
                    yield {
                        'words': w_l.css('span.dictionary__word::text').get().strip(),
                        'definition': explain.css('p').get()
                    }