from functools import wraps
import math
import time
#  timer  decorator
def timer(func):
    @wraps(func)
    def  wrapper_timer(*args,**kwargs):
        start_time = time.perf_counter()
        value = func(*args,**kwargs)
        end_time = time.perf_counter()
        print(f"it took {func.__name__}()  { end_time-start_time:.2f} seconds to execute")
        return value
    return wrapper_timer

@timer
def waste_time(number_loops):
    for i in range(number_loops +1):
        sum(num**2 for num in range(10_000))

#  example 2
def debug(func):
    """prints the function signature and its return value"""
    @wraps(func)
    def wrapper_debug(*args,**kwargs):
        repr_args  = [repr(a)  for a in args ]
        repr_kwargs = [f"{k} = {v}"  for k,v in kwargs.items()]
        signature =  ",".join(repr_args + repr_kwargs)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args,**kwargs)
        print(f"the function {func.__name__}()   returns {value}")
        return value
    return wrapper_debug


@debug
def make_greeting(name,age=None):
    if not age:
        return f"hello {name }"
    else:
        return f"hello {name} your  have grown up {age}"
    
# make_greeting("gwen ")
# make_greeting("ben", 10)
#  using a debug decorator with predefine functions.
#  note that you cant use    syntactic sugar "@" with pre defined functions you have to manually   decorate them.
# note that you  cant use  this decorator with readonly functions 
#  The following example calculates an approximation of themathematical constant e:

math.factorial = debug(math.factorial)
def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))

# approximate_e()
# approximate_e(7)
# approximate_e(10)

#  example 3
#  decorator to slow down code
def slow_down(func):
    @wraps(func)
    def wrapper_slow_down(*args,**kwargs):
        time.sleep(3)
        return func(*args,**kwargs)
    return  wrapper_slow_down

@slow_down
def count_down(n=0):
    if n <= 0:
        print("lift off")
        return
    else:
        print(f"the count down is at {n}")
    count_down(n-1)

count_down(5)