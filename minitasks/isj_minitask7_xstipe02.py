#minitask 7

#@deprecated
#def some_old_function(x, y):
  #  return x + y

#some_old_function(1,2)

# should write:
# Call to deprecated function: some_old_function
# 3
def deprecated(func):
    def new_func(*args, **kwargs):
        print("Call to deprecated function: " + func.__name__)
        print(func(*args, **kwargs))
        return func(*args, **kwargs)
    return new_func

@deprecated
def some_old_function(x,y):
    return x + y

some_old_function(1,2)