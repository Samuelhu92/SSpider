
class Request(object):
    def __init__(self,url,method='GET',data=None,callback=None,headers=None,meta=None,don_filter=False):
        self.url=safe_url(url)


        self.method=method
        self.data=data
        self.callback=callback
        self.headers=headers or {}
        self.don_filter=don_filter
        self.meta=meta if meta else {}
    def copy(self,*args,**kwargs):
        for key in ["url","method","callback","headers","meta","data"]:
            kwargs.setdefault(key,getattr(self,key))
        cls = kwargs.pop('cls',self.__class__)
        return cls(*args,**kwargs)
    def __str__(self):
        return "<%s %s>" % (self.method, self.url)

    __repr__=__str__