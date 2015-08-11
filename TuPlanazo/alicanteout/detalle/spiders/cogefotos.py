import re

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from detalle.items import DetalleItem

import urllib

filename = 'lista.txt'

class CogefotosSpider(CrawlSpider):
    name = 'cogefotos'
    allowed_domains = ['alicanteout.com']

    start_urls = []

    # Leemos nuestro archivo que contiene las urls listadas

    f = open(filename).read()
    for linea in f.split('\n'):
        if linea != '':
            # Agregamos cada link a las urls a examinar
            start_urls.append("http://www.alicanteout.com" + linea)

    def parse(self, response):
       hxs = HtmlXPathSelector(response)
       sites = hxs.select('//html')
       items = []
       for site in sites:
           item = DetalleItem()
           item['titulo'] = site.select("//div/div/h2[@class='itemTitle']/text()").extract()
           item['foto'] = site.select("//span[@class='itemImage']/a[@class='modal']/img/@src").extract()        
           item['fecha'] = site.select("//div[@class='itemIntroText']/p/text()").extract()
           item['descripcion'] = site.select("//div[@class='itemFullText']/p").extract()
           item['hora'] = item['fecha'][1]
           item['lugar'] = item['fecha'][2]
           item['precio'] = item['fecha'][3]
           item['fecha'] = item['fecha'][0]
           item['categoria'] = site.select("//head/base/@href").extract()
           item['categoria'] = item['categoria'][0].split('/')
           item['categoria'] = item['categoria'][3]
           items.append(item)
       return items

CogefotosSpider()

