import re

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from detalle.items import DetalleItem

import urllib

filename = 'paraextraer.txt'

class CogefotosSpider(CrawlSpider):
    name = 'cogefotos'
    allowed_domains = ['yumping.es']

    start_urls = []

    # Leemos nuestro archivo que contiene las urls listadas

    f = open(filename).read()
    for linea in f.split('\n'):
        if linea != '':
            # Agregamos cada link a las urls a examinar
            start_urls.append(linea)


    def parse(self, response):
       hxs = HtmlXPathSelector(response)
       sites = hxs.select('//html')
       items = []
       for site in sites:
           item = DetalleItem()
           item['titulo'] = site.select("//div[@id='breadcrumb']/a[6]/text()").extract()
           item['categoria'] = site.select("//div[@id='breadcrumb']/a[1]/text()").extract()
           item['subcategoria'] = site.select("//div[@id='breadcrumb']/a[2]/text()").extract()
           item['subcategoria2'] = site.select("//div[@id='breadcrumb']/a[3]/text()").extract()
           item['subcategoria3'] = site.select("//div[@id='breadcrumb']/a[4]/text()").extract()
           item['subcategoria4'] = site.select("//div[@id='breadcrumb']/a[5]/text()").extract()
           item['foto'] = site.select("//ul/li[@class='gallery_thumb ']/a/img/@src").extract()        
           item['descripcion'] = site.select("//div[@id='description']/div[@id='text_user']").extract()
           item['lugar'] = site.select("//div[@id='empresa_info']/div/p/i/text()").extract()
           item['calle'] = site.select("//div[@id='empresa_info']/div/p/text()").extract()
           items.append(item)
       return items

CogefotosSpider()

