import re

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from detalle.items import DetalleItem

import urllib

filename = 'lista.txt'

class CogefotosSpider(CrawlSpider):
    name = 'cogefotos'
    allowed_domains = ['tucamon.es']

    start_urls = []

    # Leemos nuestro archivo que contiene las urls listadas

    f = open(filename).read()
    for linea in f.split('\n'):
        if linea != '':
            # Agregamos cada link a las urls a examinar
            start_urls.append("http://www.tucamon.es" + linea)

    def parse(self, response):
       hxs = HtmlXPathSelector(response)
       sites = hxs.select('//html')
       items = []
       for site in sites:
           item = DetalleItem()
           item['titulo'] = site.select("//head/title/text()").extract()
           item['foto'] = site.select("//div[@class='photo_container photo_align_center']/img[1]/@src").extract()
           item['descripcion'] = site.select("//div[@id='content']/p[2]").extract()
           item['fecha'] = site.select("//div[@id='content']/p[3]").extract()
           item['hora'] = site.select("//div[@id='content']/p[4]").extract()
           items.append(item)
       return items

CogefotosSpider()

