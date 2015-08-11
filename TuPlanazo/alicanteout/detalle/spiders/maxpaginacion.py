import re

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from detalle.items import DetalleItem

filename = 'maxpaginacion.txt'

class MaxpaginacionSpider(CrawlSpider):
    name = 'maxpaginacion'
    allowed_domains = ['alicanteout.es']
    categorias = ["musica-y-conciertos-alicante","teatro-y-espectaculos-alicante","arte-museos-y-exposiciones-alicante","turismo-y-aire-libre-alicante","alicante-con-ninos","restaurantes-y-tapas-alicante","bares-de-copas-y-cafes-alicante","tiendas-y-compras-en-alicante","cursos-alicante-formacion"]
    
    start_urls = []
    for pos in range (0, 9):
            start_urls.append("http://www.alicanteout.com/" + categorias[pos])

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        it = DetalleItem()
        
        # Extraemos la lista de links
        it['enlaces'] = hxs.select("//li[@class='pagination-end']/a/@href").extract()
            
        #Agregamos cada link al archivo
        for i in it['enlaces']:
            #Agregamos cada link al archivo
            open(filename,'a+').write(i+'\n')

MaxpaginacionSpider()
