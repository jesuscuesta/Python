import os


f = open('maxpaginacion.txt','w')
f.close()
f = open('paraextraer.txt','w')
f.close()
os.system('scrapy crawl detalleSpider')
os.system('scrapy crawl ultimospider')
os.system('scrapy crawl cogefotos -o guiaocio.xml -t xml')



