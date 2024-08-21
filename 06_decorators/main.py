#  challenge 1
import time
def timer(func):
    def rapper(*args,**kwargs):
        print("from rapper")
        start_time= time.time()
        result  = func(*args,**kwargs)
        end_time= time.time()
        execution_time =end_time-start_time
        print(f"it took {func.__name__}  {execution_time:.2f} seconds to execute")
        return result
    return rapper


@timer
def   how_time():
    time.sleep(3)
# how_time()

#  challenge 2
def debug_func(fn):
    def wrapper(*args,**kwargs):
        print(f"the function name is {fn.__name__}")
        if len(args) > 0:
            print("its positional arguments are ")
            print(*args,sep=" , ")
        if len(kwargs):
            print("its named arguements are ")
            for  k in kwargs:
                print(f" {k} = {kwargs.get(k)}",end=" , ")
        kwargs.setdefault("greetings","add something here")
        result = fn(*args,**kwargs)
        return result
    return wrapper

@debug_func
def  func1(*args,**kwargs):
    pass

# func1(*"usman",name="mango",flavor="sweet")
@debug_func
def func2(*args,**kwargs):
    print("")
    print(kwargs.get('greetings'))
    print(kwargs.get('name'))

# func2(name="usman",greetings="hello")

#  challenge 3
db_stor ={} 

def  cacher(func):
    def wrapp(*args,**kwargs):
        #  cache func_args  if func_arg.call  func.arg = func.value  return func.value  else return func().
        #  checking if the func exists already
        if not  db_stor.get(func.__name__):
            #  since this is the first time the function is called so settin up  its values in db
            print("first time func is called")
            db_stor.update({ func.__name__: { "args" : args, "kwargs" : kwargs, "count":1}})
            return func(*args,**kwargs)
        else:
            #  since the function is inside else clause it means this is not the first time the function is called.
            print("not first time")
            #  first check if the given arguemnets matches existing  arguements for that function
            if  db_stor.get(func.__name__).get('args') == args and db_stor.get(func.__name__).get('kwargs'):
                print("arguements already exists")
                db_stor.get(func.__name__)['count'] += 1
                return db_stor.get(func.__name__)
            else:
                #  this is not  the first time function is called but  its arguements are different.
                return func(*args,**kwargs)
    return wrapp

@cacher
def test(*args,**kwargs):
    time.sleep(1)
    

# print(test("mango",flavor="sweet"))
# print(test("mango",flavor="sweet"))
print(test(2,3))


