import re

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from detalle.items import DetalleItem

filename = 'lista.txt'

class DetallespiderSpider(CrawlSpider):
    name = 'detalleSpider'
    allowed_domains = ['tucamon.es']
    pos = 1

    start_urls = []

    for pos in range (1, 5):
            start_urls.append("http://www.tucamon.es/agenda?page=" + str(pos))

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        it = DetalleItem()
        
        # Extraemos la lista de links
        it['enlaces'] = hxs.select("//div/div[@class='event_info']/a/@href").extract()

        for a in range (0,len(it['enlaces'])):
                it['enlaces'][a] = it['enlaces'][a].encode('utf-8')

        for i in it['enlaces']:
            #Agregamos cada link al archivo
            open(filename,'a+').write(i+'\n')

DetallespiderSpider()
