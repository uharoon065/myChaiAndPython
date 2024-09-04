#  in this section we will learn  how can we decorate a function with multiple decorators.
# we can apply multiple decorators on one funcion  by stacking them on top of one another.
# the decorators are applied  in the sequence they are listed.
from realWorldExamples import debug,timer
from decorators_module import  do_twice
# @debug
# @do_twice
# def greet(name):
#     print(f"hello {name} how you been!!!")
"""
 debug = debug(do_twice(greet))
the debug decorator calls the do_twice()whhich takes greet function as an  arguement. remember that the do_twice returns a do_twice_wrapper and that wrapper is called inside the debug decorator.
"""
# greet("usman")
# switching the order of decorators and abserving the result.
@do_twice
@debug
def greet(name):
    print(f"hello {name} how you been!!!")

# greet("apple")
# here  the debug returns a debug_wrapper which the do_twice is going to call twice as   defined inside the do_twice _wrapper  definition any function passed to it is going to be called twice.