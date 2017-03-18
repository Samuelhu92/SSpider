import inspect
import logging
import urllib
import hashlib
from urlparse import urlparse,parse_qsl,urlunparse

def get_logger():

    default_logger = logging.getlogger(__name__)
    default_logger.setLevel(logging.DEBUG)
    stream = logging.StreamHandler()
    stream.setLevel(logging.DEBUG)
    formatter = logging.Formatter("[%(levelname)s] %(asctime)s-%(message)s")
    stream.setFormatter(formatter)
    default_logger.addHandler(stream)
    return default_logger

def call_func(func,errback=None,callback=None,*args,**kwargs):
    #execute a function and errback function once error incurs and call back 
    #function if it exists
    try:
        result = func(*args,**kwargs)
    except Exception as exc:
        if errback:
            errback(exc)
    else:
        if callback:
            result = callback(result)
        return result

def iter_children_class(values,clzz):
    for obj in values:
        if inspect.isclass(obj) and issubclass(obj,clzz) and obj is not clzz:
            yield obj



