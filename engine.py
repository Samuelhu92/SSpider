from downloader import DownloadHandler
#Disable the log of requests lib.
ogging.getLogger('requests').setLevel(logging.CRITICAL)

class Engine:

    def __init__(self):
        self.maximumjobs = settings.maximumjobs
        self.scheduler=Scheduler()
        self.downloader={}
        self.logger = get_logger()
        self.poolsize = settings.POOLSIZE
        self.status = False
        self.fetchpool=Pool(size=self.poolsize)
        self._spiders = {}

    def start(self):
        """
        start the engine and send message to the sipder insatnce and call 
        spider_started method
        """
        self._engine_started()
        self.status = True
        self.excute() 

    def execute(self):
        self._init_seed_requests()
        for 

    def shutdown(self):
        self.status = False
        self._engine_stopped

    def submit(self,spider_cls,*args,**kwargs):
        #Submit a new crawling task
        spider = spider_cls(*args,crawler=self,**kwargs)
        if spider.name in self._spiders:
            raise Exception('Spider {} exists, choose a new name if you want to proceed.'.format(spider.name))
        self._spiders[spider.name]=spider
        self.downloader[spider.name]=DownloadHandler(spider)


    def _init_seed_requests(self):
        """
        initial requests
        """
        for spider in self._spiders.values():
            try:
                [self.crawl(request,spider) for request in self.__call_func_in_spider(spider,'start_requests')]
            except Exception as err:
                self.logger.error(err,exc_info=True)

    def crawl(self,item,spider):
        """
        crawl next request into queue
        """
        if isinstance(item,Request):
            self.scheduler._enqueue_request(request, spider)
        elif isinstance(item,Response):
            self.scheduler._enqueue_request(response, spider)
    def _engine_started(self):
        self.logger.info('Crawler engine started')
        self.__call_func_in_spiders('spider_started')
    def _engine_stopped(self):
        self.logger.info('Crawler engine stopped')
        self.__call_func_in_spiders('spider_stopped')
    def _engine_idle(self):
        self.logger.info('Crawler engine is in idle mode')
        self.__call_func_in_spiders('spider_idle')
    def _next_request_batch(self,spider):
        return self.scheduler._next_request()

    def _sch_download(self):
        self.downloads = []
        for i in xrange(self.maximumdownjobs):
            while self.status:
                try:
                    request = self.scheduler._next_request
                    download = fetchpool.spawn(self.download,request,spider)
                    downloads.append(download)
                except empty:
                    self._engine_idle()
        return downloads 
    def _process_queued_responses(self):
        self.parses = []
        while self.status:
            response = self.scheduler._next_response()
            parse = parsepool.spawn(self._process_response,response,spider)
            parses.append(parse)
        return parses

    def download(self,request,spider):
        response = self.downloader[spider.name].fetch(request)
        response.request = request
        self.crawl(response,spider)
        return response 

    def _process_requests(self,request,spider):
        self.logger.debug('[{}][{}] Processiong request:{}'.format(spider.name,))
        self.__call_func_in_spider(spider,'process_request',request)

    def __call_func_in_spider(self,spider,name=None,*args,**kwargs):
        try:
            if hasattr(spider,name):
                return getattr(spider,name)(*args,**kwargs)
        except Exception as err:
            self.logger.error()
    def __call_func_in_spiders(self,name,*args,**kwargs):
        for spider in self._spider.values():
            self.__call_func_in_spider(spider,name,*args,**kwargs)

