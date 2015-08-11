import re

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from detalle.items import DetalleItem

filename = 'maxpaginacion.txt'

class MaxpaginacionSpider(CrawlSpider):
    name = 'maxpaginacion'
    allowed_domains = ['kedin.es']
    start_urls = ["http://kedin.es/search?_=1337269937792&category_id=&date=&kind=event&location_id=&page=1&price=&query=&utf8="]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        it = DetalleItem()
        
        # Extraemos la lista de links
        it['enlaces'] = hxs.select("//div[@class='pagination']/a/text()").extract()
            
        #Agregamos cada link al archivo
        f = open(filename,'w')
        f.write(it['enlaces'][len(it['enlaces'])-2])

MaxpaginacionSpider()