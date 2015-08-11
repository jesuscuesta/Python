import os

f = open('lista.txt','w')
f.close()

os.system('scrapy crawl detalleSpider')
os.system('scrapy crawl cogefotos -o tucamon.xml -t xml')



