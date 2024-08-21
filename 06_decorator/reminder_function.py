#  functions as first class objects  shall be treated as  any other objects in python. they can be passed around as argument , stored in a variable , returned from another function etc.
def hello(name):
    return f" hello { name}"
#  pass as argument
def greet(greeting_func):
    return greeting_func("usman")

#  hello("ben")
#  you can pass hello function inside the greet since it takes  a function as its argument.
#  greet(hello) -> "hello usman"


#  inner  functions
#  returnin a function
#  a function can define inner function  and can   call that function locally without exposing them to global scope. A function can return a inner function which allows yu to access that inner function in global scope. it is very important to remember that the parrent function is just returning the  reference or definition to that function  and the inner function return value will be avalible when it is called.
def parrent(num):
    print(" from parrent")
    def child1():
        print(f"from {child1.__name__}")
        return f" hello MR. spungbob"

    def child2():
        print(f"from {child2.__name__}")
        return f" hello mr. Crap"
    # child1()
    # child2()
    if num ==1:
        return child1
    else:
        return child2