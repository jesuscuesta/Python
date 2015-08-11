import os

f = open('lista.txt','w')
f.close()
f = open('listapaginacion.txt','w')
f.close()
os.system('scrapy crawl detalleSpider')
os.system('scrapy crawl paginspider')
os.system('scrapy crawl cogefotos -o yumping.xml -t xml')



