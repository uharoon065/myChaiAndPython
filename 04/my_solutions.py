from typing import Union, Dict
from math import pi
# challenge 1
def square(n: int)-> int:
    return n*n

# challenge 2
def  add(n: int,m: int)-> int:
    return n+m

# challenge 3
def multiply(x: Union[int,str],y: Union[int,str])-> Union[str,int]:
    return x*y

# challenge 4
def  area_circumference(r: int)-> Dict[str,int]:
    area = pi*r**2
    circumference = 2*pi*r
    return { "area" : float(f"{area:.2f}") , "circumference": float(f"{circumference:.2f}") } 


# challenge 5
def greeting(msg: str="user")-> str:
    return f"welcome  {msg} to chai and code "
"""
# Challenge 1: square
print(square(5))  # Output: 25
print(square(-3))  # Output: 9

# Challenge 2: add
print(add(5, 3))  # Output: 8
print(add(-2, 7))  # Output: 5

# Challenge 3: multiply
print(multiply(4, 5))  # Output: 20
print(multiply('hello ', 3))  # Output: 'hello hello hello '

# Challenge 4: area_circumference
print(area_circumference(4))  # Output: {'area': 50.27, 'circumference': 25.13}
print(area_circumference(2))  # Output: {'area': 12.57, 'circumference': 12.57}

# Challenge 5: greeting
print(greeting())  # Output: 'welcome user to chai and code '
print(greeting('John'))  # Output: 'welcome John to chai and code '
"""


# challenge 6
simple_cube= lambda x: x**3
def square(func,x):
    # do some operations on x and pas it to func
    return func(x)

print(square(lambda x:x**2,5))
# challenge 7
def sum_all(*args):
    print(args)
    return sum(args)

# print(sum_all(1,3,6,124))
# challenge 8
def my_kwargs(**kwargs):
    # print(kwargs)
    for k,v in kwargs.items():
        print(f"{k} : {v}")

my_kwargs(name="usman",age=23)
# my_kwargs({"name":"ben", "age": 10}) passing dict like this is considered as a positional argument not a keyword arguement 
my_kwargs(**{"name":"ben", "age": 10})
# challenge 9
def my_generator(n):
    # even_nums = []
    for i in range(2,n+1):
        if i%2==0:
            # this will return only first even number  and exit the function 
            # return i 
            # this will return the number  as well as  keep the state of the function  
            yield i
            # even_nums.append(i)
    # return even_nums
    # return even_nums.__iter__()

# print(my_generator(10))
# for i in  my_generator(10):
    # print(i)    
# challenge 10
def  my_factorial(n: int)-> int:
    if n == 1:
        return n
    return n *  my_factorial(n-1)

print(my_factorial(5))