import urllib2

proxy = urllib2.ProxyHandler({'http': '127.0.0.1:8118'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)


import re

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from detalle.items import DetalleItem

filename = 'lista.txt'
filenameMax = 'maxpaginacion.txt'

class DetallespiderSpider(CrawlSpider):
    name = 'detalleSpider'
    allowed_domains = ['kedin.es']

    start_urls = []
    paginacion = open(filenameMax,'r')
    maximo = paginacion.readline()
    for pos in range (1, int(maximo)):
                start_urls.append("http://kedin.es/search?_=1337269937792&category_id=&date=&kind=event&location_id=&page=" + str(pos) + "&price=&query=&utf8=")

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        it = DetalleItem()
        
        # Extraemos la lista de links
        it['enlaces'] = hxs.select("//section/p[@class='description']/a/@href").extract()

        for i in it['enlaces']:
            #Agregamos cada link al archivo
            open(filename,'a+').write(i+'\n')

DetallespiderSpider()
