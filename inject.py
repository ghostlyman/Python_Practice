写一个


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