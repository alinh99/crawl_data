import scrapy

num = 0
class WordsLstSpider(scrapy.Spider):
    
    name = 'words_lst'
    allowed_domains = ['https://www.dictionary4it.com/']
    for i in range(num+1, 64):
        start_urls = ['https://www.dictionary4it.com/term/page/' + str(i),
        'https://www.dictionary4it.com/term/']
    def parse(self, response):
        print("procesing:"+response.url)
        word_name = response.xpath("//div[@id='dictionary__category']/ul/li[@class='category-item']/a/text()").extract()
        # definition = (response.xpath("//div[@id='dictionary__category']/ul/li[@class='category-item']/a/@href") + word_name).extract()
        row_data=zip(word_name,definition)
        for item in row_data:
            scraped_info = {
            'word': item[0],
            'definition': item[1]
            }
        yield scraped_info

