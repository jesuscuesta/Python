# Scrapy settings for detalle project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'detalle'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['detalle.spiders']
NEWSPIDER_MODULE = 'detalle.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)


DOWNLOAD_DELAY = 0.25
DUPEFILTER=True
COOKIES_ENABLED=False
RANDOMIZE_DOWNLOAD_DELAY=True
SCHEDULER_ORDER='BFO'

http_proxy = "http://localhost:8118"