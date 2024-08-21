#  the decorators are simple python funcions and  have the power of reusibility just like normal functions.
def do_twice(func):
    # def wrapper_do_twice(): for case 1
    # def wrapper_do_twice(name):
    def wrapper_do_twice(*args,**kwargs):
        # func(name)
        # func(name)
        func(*args,**kwargs)
        func(*args,**kwargs)
    return wrapper_do_twice

#  passing   arguements to decorators. 
#  you can pass arguements to  decorated functions  look at the example 2.
#  in your first case  when you  try  to pass  a arguement to evening("usman")  it ends up in an error because although your definition says your function does accept an arguement but as we discuss  your decorator function is now pointing to wrapper and the wrapper doesnot accept any arguement thats why we get an error., so to solve this add a parameter to wrapper and pass it as an argument to our func().
#  in second case  our fairwell  throws an error() because say_fairwell() does not takes any arguement  and we   passing (name) to it.
#  so if we pass an arguement  we broke our say_fairwell() and if  we dont we broke say_evening().
#  to fix it we use  "*args" and "**kwargs"  because passing unpacking empty tuple and dict  to func(*args,**kwargs) wouldnt means passing nothing for our functions that doesnot take any arguements and for functions that does take arguements  simply taking args and kwargs from wrapper and pssing them.