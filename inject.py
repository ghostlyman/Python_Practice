写一个带一个default_user参数的装饰器,此装饰器检查传入函数的关键字参数。
如果没有名为User的参数,使用default_user 作为user参数传递给函数



from functools import wraps

def inject_user(default_user):
    def inject(fn):
        def wrap(*args, **kwargs):
            if 'user' not in kwargs.keys():
                kwargs['user'] = default_user
            return fn(*args, **kwargs)
        return wrap
    return inject

@inject_user('Rick')
def do_somethings(*args, **kwargs):
    print(kwargs.get('user'))

do_somethings()

do_somethings(user='ghostlyman')