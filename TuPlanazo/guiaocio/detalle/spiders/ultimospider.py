import re

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from detalle.items import DetalleItem

filename = 'maxpaginacion.txt'
filename2 = 'paraextraer.txt'

class UltimospiderSpider(CrawlSpider):
    name = 'ultimospider'
    allowed_domains = ['guiadelocio.com']
    start_urls = []
    variable = []

    # Leemos nuestro archivo que contiene las urls listadas

    f = open(filename).read()
    for linea in f.split('\n'):
        if linea != '':
            # Agregamos cada link a las urls a examinar
            for pos in range(0,int(linea)):
                start_urls.append("http://www.guiadelocio.com/content/search/%28offset%29/" + str(pos) + "0?SearchText=*")


    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        it = DetalleItem()
        
        # Extraemos la lista de links
        it['enlaces'] = hxs.select("//div[@class='content']/ul[@class='content']/li/a/@href").extract()

        for i in it['enlaces']:
            #Agregamos cada link al archivo
            open(filename2,'a+').write(i+'\n')

UltimospiderSpider()