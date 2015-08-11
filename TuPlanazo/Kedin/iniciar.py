import os

f = open('lista.txt','w')
f.close()
f = open('maxpaginacion.txt','w')
f.close()

os.system('scrapy crawl maxpaginacion')
os.system('scrapy crawl detalleSpider')
os.system('scrapy crawl cogefotos -o kedin.xml -t xml')



