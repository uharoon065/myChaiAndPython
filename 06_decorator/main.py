from  decorators_module import do_twice
# example 1
@do_twice
def  say_fairwell():
    print("bye")

#  example 2
@do_twice
def say_evening(name):
    print(f"hello {name} good evening!!!")
#  first case
# say_fairwell()
# say_evening("usman")

#  case 2
# say_fairwell()
# say_evening("usman")
