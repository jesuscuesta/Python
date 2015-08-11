import re

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from detalle.items import DetalleItem

filename = 'maxpaginacion.txt'

class MaxpaginacionSpider(CrawlSpider):
    name = 'maxpaginacion'
    allowed_domains = ['yumping.com']
    categorias = []
    
    start_urls = []
    for pos in range (300, 800):
            start_urls.append("http://www.yumping.com/aventura--" + str(pos))

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        it = DetalleItem()
        
        # Extraemos la lista de links
        it['enlaces'] = hxs.select("//div[@class='col_left']/div[@class='nav']/a/text()").extract()
            

        open(filename,'w').write(it['enlaces'][len(it['enlaces'])-2])

MaxpaginacionSpider()
