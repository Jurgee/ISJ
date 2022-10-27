def return_key(key):
    return lambda item: key(item)

def first_with_given_key(iterable, key=repr):
    UsedKeys = {}
    get_key = return_key(key)
    for item in iterable:
        item_key = get_key(item)
        if item_key in UsedKeys.keys():
            continue
        try:
            UsedKeys[hash(item_key)] = repr(item)
        except TypeError:
            UsedKeys[repr(item_key)] = repr(item)
        yield item
