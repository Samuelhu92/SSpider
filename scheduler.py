
class Scheduler(Object):
    def __init__(self,queue_size=1024):
        self._requests_queue = Queue(queue_size)
        self._responses_queue = Queue(queue_size)
        self.request_filter = RequestFilter()

    def _enqueue_request(self,request,spider):
        """
        put request and correponding spider into queue
        """
        if request:
            if not request.dont_filter and self.request_filter.request_seen(request):
                logger.debug('[{}] Ignore duplicated request {}'.format(spider.name,reuqest))
                return
            self._requests_queue.put((request,spider))
    def _enqueue_response(self,response,spider):
        if response:
            self._responses_queue.put((response))
    def _next_response(self):
        if self._responses_queue.empty():
            return None
        return self._responses_queue.get()
    def _next_request(self):
        """
        get next request
        """
        if self._requests_queue.empty():
            return None
        return self._requests_queue.get()

    def __len__(self):
        return self._requests_queue.qsize()



