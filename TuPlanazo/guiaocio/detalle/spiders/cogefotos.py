import re

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from detalle.items import DetalleItem

import urllib

filename = 'paraextraer.txt'

class CogefotosSpider(CrawlSpider):
    name = 'cogefotos'
    start_urls = []

    # Leemos nuestro archivo que contiene las urls listadas

    f = open(filename).read()
    for linea in f.split('\n'):
        if linea != '':
                start_urls.append("http://www.guiadelocio.com" + linea)

    def parse(self, response):
       hxs = HtmlXPathSelector(response)
       sites = hxs.select('//html')
       items = []
       for site in sites:
           item = DetalleItem()
           item['titulo'] = site.select("//h1[@class='nobg']/text()").extract()
           item['categoria'] = site.select("//div/ul/li[@class='last']/text()").extract()
           item['lugar'] = site.select("//div/ul/li[@class='last']/text()").extract()
           item['foto'] = site.select("//div[@class='shadow ftl']/img/@src").extract()
           item['calle'] = site.select("//div[@class='content clear']/ul/li/text()").extract()
           item['descripcion'] = site.select("//div[@class='infoContent']/ul/li").extract()
           items.append(item)
       return items

CogefotosSpider()

