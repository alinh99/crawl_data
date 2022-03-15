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
        # url_words = 'https://www.dictionary4it.com/term/'

        for page_definition in range(1, 64):
            self.start_urls.append(url_definition + str(page_definition))

        # for page_words in range(1, 64):
        #     self.start_urls.append(url_definition + str(page_words))

    def parse(self, response):

        print("procesing:"+response.url)
        # Extract data using css selectors
        # words = response.xpath(
        #     "//ul/li[@class='category-item']/a/text()").get.strip()
        # words = response.css('li.category-item')
        for link in response.css('li.category-item a::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_categories, priority=1)

        # for word in words:
        #     yield {
        #         'word': word.css('a::text').get().strip(),
        #     }
        #     NEXT_PAGE_SELECTOR = '.page-link + a::attr(href)'
        #     next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        #     if next_page:
        #         yield scrapy.Request(
        #             response.urljoin(next_page),
        #             callback=self.parse)

    def parse_categories(self, response):
        definitions = response.css('div.dictionary__mean')
        explains = response.css('div.dictionary__explain')
        # definitions.css('span::text').get().strip()
        if definitions:
            for definition in definitions:
                yield{
                        'definition': definition.css('span::text').get().strip()
                    }
        else:
            for explain in explains:
                yield{
                    'definition': ''
                }