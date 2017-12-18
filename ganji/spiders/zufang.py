#coding:utf-8
import scrapy
from ..items import GanjiItem

class ZufangSpider(scrapy.Spider):
    name = 'zufang'
    start_urls = ["http://hz.ganji.com/fang1/binjiang/"]

    def parse(self, response):
        print response
        zf = GanjiItem()
        title_list = response.xpath("//*[@class='f-list-item ershoufang-list']/dl/dd[1]/a/text()").extract()
        price_list = response.xpath("//*[@class='f-list-item ershoufang-list']/dl/dd[5]/div[1]/span[1]/text()").extract()
        for i,j in zip(title_list,price_list):
            zf['title']= i.encode('utf-8')
            zf['money']= j
            yield zf



