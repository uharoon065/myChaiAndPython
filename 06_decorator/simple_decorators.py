from datetime import datetime
#  simple decorator
def  decorator(func):
    print("inside decorator")
    def wrapper():
        print("before the function is called")
        func(datetime.now().hour)
        print("after the function is called")
    return wrapper

def say_cow():
    print(" say moo moo")

#  this is the  point where decoration happened
say_cow= decorator(say_cow)
#  the  decorator function is decorating the say_cow function.
#   infact if  you check the say_cow now points to the wrapper function, however the wrapper has reference to original say_cow() as "func" and is being called   between print statements.
#  in simple words a decorator is a function that wrapps another function modifying its behavior.
#  in our case wrapper is wrapping the function say_cow() and modifying its  its original behavior which was "print('moo moo')" by printing "print('before the function')" and "print('after function')' "

#  note that the decorator can modify the function dynamically. Look at our second example
def dont_disturb_night(func):
    def wrapper():
        if 7<=  datetime.now().hour< 22:
            func()
        else:
            pass
    return wrapper

def   say_greet():
    print("hello, are you up")

say_greet=  dont_disturb_night(say_greet)
say_greet()
#  decorators syntax sugar
#  the python provides a more pythonish way of  decorating functions. Use  "@" symbol  to decorate a unction.
#   look at the above decorator,  now  i am creating a simple function decorating it using "@" symbol.
@decorator
def say_morning(t=None):
    if t < 9 >4:
        print("good morning)")

    else:
        print("hello ")

say_morning()
#    when you use "@" syntax the python takes care of couple of things, like calling of decorator () ,  passing the defined function  and assigning it back to it ".
# if you even dont call the defined function  lets say  havent called say_morning function just had defined and have used decorator on it you will notice that the decorator will be called  and if you chekc say_morning.__name__ it will be pointing back to wrapper."