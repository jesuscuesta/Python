import re

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from detalle.items import DetalleItem

filename = 'lista.txt'
filenameMax = 'maxpaginacion.txt'

class DetallespiderSpider(CrawlSpider):
    name = 'detalleSpider'
    allowed_domains = ['alicanteout.com']
    pos = 1
    pagi = 3
    maximo = 5
    enlace = "enlace para realizar scrapy"
    a = 0

    start_urls = []
    
    f = open(filenameMax).read()
    for linea in f.split('\n'):
        if linea != '':
            maximo = linea.split("?")
            enlace = maximo[0]
            maximo = maximo[1]
            maximo = maximo.split("=")
            maximo = maximo[1]
            for pagi in range (0, int(maximo)/10):
                    start_urls.append("http://www.alicanteout.com/" + enlace + "?start=" + str(pagi) + "0")

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        it = DetalleItem()
        
        # Extraemos la lista de links
        it['enlaces'] = hxs.select("//h3[@class='catItemTitle']/a/@href").extract()

        for a in range (0,len(it['enlaces'])):
                it['enlaces'][a] = it['enlaces'][a].encode('utf-8')

        for i in it['enlaces']:
            #Agregamos cada link al archivo
            open(filename,'a+').write(i+'\n')

DetallespiderSpider()
