class Spider(object):
    custom_settings = None
    name = None
    def __init__(self, name=None,**kwargs):
        if name is not None:
            self.name = name
        self.__dict__.update(kwargs)
        if not hasattr(self, "start_urls"):
            self.start_urls = []

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, headers=getattr(self,'default_headers', None), callback=self.parse)

    def initialize(self):
        pass

    def spider_start(self):
        pass

    def parse(self,response):
        raise NotImplementedError
    def process_request(self,request):
        pass
    def process_response(self,response):
        pass
    def process_item(self,item):
        pass
    def spider_close(self):
        pass
    




