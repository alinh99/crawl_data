import scrapy


class WordsListSpider(scrapy.Spider):
    name = 'words_list'
    allowed_domains = ['www.dictionary4it.com']

    start_urls = ['https://www.dictionary4it.com/term/']
    custom_settings = {'FEED_URI': "dictionary_%(time)s.csv",
                       'FEED_FORMAT': 'csv'}

    def parse(self, response):

        print("procesing:"+response.url)
        # Extract data using css selectors
        # words = response.xpath(
        #     "//ul/li[@class='category-item']/a/text()").get.strip()
        words = response.css('div.dictionary__mean')
        # for link in
        # for link in response.css('li.category-item a::attr(href)'):
        #     yield response.follow(link.get(), callback=self.parse_categories)
        # price_range=response.css('.value::text').extract()
        # Extract data using xpath
        #orders=response.xpath("//em[@title='Total Orders']/text()").extract()
        #company_name=response.xpath("//a[@class='store $p4pLog']/text()").extract()

        # row_data = zip(words)
        for word in words:
            yield {
                'word': word.css('a::text').get().strip()
            }
            NEXT_PAGE_SELECTOR = '.pagination + a::attr(href)'
            next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
            if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse)

    def parse_categories(self, response):
        definitions = response.css('div.dictionary__mean')
        # definitions.css('span::text').get().strip()
        for definition in definitions:
            yield{
                'definition': definition.css('span::text').get().strip()
            }
