import random
# the decorators doesnt have to wrap the decorated function,  it can simply return it.
plugins = dict()
def  register(func):
    """ register a func as plugin"""
    plugins[func.__name__]= func
    return  func

#  note that you dont have to  use @wraps decorator  since we are just  returning a function  reference without modifying it.
#  also the plugins dict contains the reference to the  the decorated function.
@register
def hello_greet(name):
    return f"hello {name }"
@register
def be_awesome(name):
    return f" hello { name} togather we are awesome!"

def random_greet(name):
    func_name,greet_func =   random.choice(list(plugins.items()))
    print(f"using { func_name!r} ")
    return  greet_func(name)

random_greet("ben")
# this simple plugins artitechure  is some what similar  to globals where all your global scope  objects exists.