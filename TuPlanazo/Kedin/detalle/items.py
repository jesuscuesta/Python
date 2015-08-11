# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class DetalleItem(Item):
    titulo = Field()
    subtitulo = Field()
    foto = Field()
    fecha = Field()
    hora = Field()
    horados = Field()
    lugar = Field()
    descripcion = Field()
    precio = Field()
    enlaces = Field()
    categoria = Field()
    subcategoria = Field()
    ciudad = Field()
    ubicacion = Field()