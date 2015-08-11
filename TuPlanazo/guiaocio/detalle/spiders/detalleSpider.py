import re

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from detalle.items import DetalleItem

filename = 'maxpaginacion.txt'


class DetallespiderSpider(CrawlSpider):
    name = 'detalleSpider'
    allowed_domains = ['guiadelocio.com']
    start_urls = ["http://www.guiadelocio.com/content/search/%28offset%29/00?SearchText=*"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        it = DetalleItem()
        
        # Extraemos la lista de links
        it['enlaces'] = hxs.select("//div/ul[@class='paginationContent']/li/a/text()").extract()

        for i in it['enlaces']:
            #Agregamos cada link al archivo
            open(filename,'w').write(i+'\n')


DetallespiderSpider()
