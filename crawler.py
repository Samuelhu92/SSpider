from engine import Engine

class CrawlerProcess(object):
    def __init__(self,settings=None):
        self.logger = get_logger()
        self._engine = Engine(**(settings or {}))

    def crawl(self,spider_cls,*args,**kwargs):
        self._engine.sumbit(spider_cls,*args,**kwargs)

    def start(self):
        self._engine.start()
        