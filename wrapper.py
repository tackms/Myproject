#coding=utf-8

import functools


def log(text):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                    print('%s %s():' % (text, func.__name__))
                    return func(*args, **kw)
            return wrapper
        return decorator


def log(func):
    def wrapper(*args, **kw):
        print ('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log('execute')
def now():
    print('2222')

print (now.__name__)


