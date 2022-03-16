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
        # Extract data using css selectors

        # words = response.css('li.category-item')
        for link in response.css('li.category-item a::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_categories, priority=1)

        # for word in words:
        #     yield {
        #         'word': word.css('a::text').get().strip(),
        #     }

    def parse_categories(self, response):
        definitions = response.css('div.dictionary__mean')
        explains = response.css('div.dictionary__explain')

        if definitions:
            for definition in definitions:
                yield {
                    'definition': definition.css('span::text').get()
                }
        else:
            for explain in explains:
                yield {
                    'definition': explain.css('p::text').get()
                }
