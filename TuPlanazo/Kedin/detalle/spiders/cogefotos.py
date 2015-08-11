import re

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from detalle.items import DetalleItem

import urllib

filename = 'lista.txt'

class CogefotosSpider(CrawlSpider):
    name = 'cogefotos'
    allowed_domains = ['kedin.es']

    start_urls = []

    # Leemos nuestro archivo que contiene las urls listadas

    f = open(filename).read()
    for linea in f.split('\n'):
        if linea != '':
            # Agregamos cada link a las urls a examinar
            start_urls.append("http://www.kedin.es" + linea)

    def parse(self, response):
       hxs = HtmlXPathSelector(response)
       sites = hxs.select('//html')
       items = []
       for site in sites:
           item = DetalleItem()
           item['titulo'] = site.select('//article/header/h1/text()').extract()
           item['subtitulo'] = site.select('//body/div/div/article/header/p/text()').extract()
           item['foto'] = site.select('///article/div/section/div/a/img/@src').extract()        
           item['fecha'] = site.select("//article/div/section/div/ul/li[@class='top']/strong/text()").extract()
           item['hora'] = site.select("//article/div/section/div/ul/li[@class='top']/div/strong/text()").extract()
           item['horados'] = site.select("//article/div/section/div/ul/li[@class='medium']/strong/text()").extract()
           item['lugar'] = site.select("//li[@class='bottom']/a/span/text()").extract()
           item['descripcion'] = site.select("//div[@class='description']/p").extract()
           item['precio'] = site.select("//li[@class='medium price']/span/strong/text()").extract()
           item['categoria'] = site.select("//meta[@name='keywords']/@content").extract()
           item['categoria'] = item['categoria'][0].split(',')
           item['subcategoria'] = item['categoria'][0]
           item['ubicacion'] = item['categoria'][3].split(',')
           item['categoria'] = item['categoria'][1]
           item['ciudad'] = site.select("//meta[@property='og:url']/@content").extract()
           item['ciudad'] = item['ciudad'][0].split('/')
           item['ciudad'] = item['ciudad'][3]

           items.append(item)
       return items

CogefotosSpider()

