# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class DetalleItem(Item):
    titulo = Field()
    foto = Field()
    fecha = Field()
    hora = Field()
    lugar = Field()
    calle = Field()
    descripcion = Field()
    precio = Field()
    categoria = Field()
    subcategoria = Field()
    subcategoria2 = Field()
    subcategoria3 = Field()
    subcategoria4 = Field()
    enlaces = Field()