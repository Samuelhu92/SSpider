class Middleware(object):

    pass

class DownloaderMiddlewareManager(object):

    def __init__(self,spider):
        self.settings = spider.settings
        self.methods = defaultdict(list)
        self.middlewares = self.load_middleware()
        for miw in self.middlewares:
            self._add_middleware(miw)

    def load_middleware(self):
        middlewares=[]
        for miw in iter_