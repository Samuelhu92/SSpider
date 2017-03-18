import requests
from middleware import DownloadMiddlewareManager, DownloadHandler
class DownloadHandler(object):
    def __init__(self,spider,keep_alive=True,**kwargs):
        self.keep_alive = keep_alive
        self.settings = spider.settings
        self.session_map = {}
        self.spider=spider
        self.kwargs = kwargs


    def _get_session(self,url):
        netloc = urlparse(url).netloc
        if self.keep_alive:
            if url not in self.session_map:
                self.session_map[netloc]=request.Session()
            return self.session_map[netloc]
        return requests.Session()
    def fetch(self,request):
        proxy = request.meta.get("proxy")
        kwargs = {
            "headers":request.headers
            "timeout": self.settings["TIMEOUT"]
        }
        if proxy:
            kwargs["proxy"] = {
                "http:": proxy,
                "https:":proxy
                }
            logger.info("user proxy %s",proxy)
        kwargs.update(self.kwargs)
        url = request.url
        method = request.method.upper()
        session = self._get_session(url)
        logger.info("processing %s",url)
        if method == 'GET':
            response = session.get(url,**kwargs)
        elif method == 'POST':
            response = session.post(url,requests.data,**kwargs)
        return Response(response.url,response.status_code,response.headers,response.content)


class Downloader(object):
    def __init__(self,spider):
        self.handler = DownloadHandler(spider)
        self.middleware = DownloadMiddlewareManager(spider)

    def fetch(self.request,spider):
        return self.middleware.download(self._download,request)

    def _download(self,request):
        return self.handler.fetch(request)
