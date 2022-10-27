def log_and_count(key=None, counts=None):
    key_in_function = key
    if counts is None:
        raise TypeError('Missing 1 argument: \'counts\'')

    def outer(func):
        def inner(*args, **kwargs):
            print('called ' + func.__name__ + ' with {} and {}'.format(args, kwargs))
            ret = func(*args, **kwargs)
            counts[key_arg] += 1
            return ret
        if key_in_function is None:
            key_arg = func.__name__
        else:
            key_arg = key_in_function
        return inner
        
    return outer