from typing import List,Dict
import time
# challenge 1
# Problem: Given a list of numbers, count how many are positive.
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
def count_positive_nums(nums: List[int])-> int:
    count = 0
    for c in nums:
        if c>0:
            count +=1
    return count
# print(count_positive_nums(numbers))
# challenge 2
def sum_even_numbers(n: int)-> int:
    n=int(n.strip())
    total=0
    for  x in range(2,n+1):
        if x%2==0:
            total += x
    return total

# print(sum_even_numbers("10"))
# challenge 3
def print_table(n: int)-> None:
    n=int(n.strip())
    for  x in range(1,11):
        if x!= 5:
            print(f"{n} * {x} = {n*x}")

# print(print_table("3"))
                        # challenge 4
def reverse_string(string: str)-> str:
    new_string=""
    for i in range(len(string),0,-1):
        c= string[i-1]
        new_string+= c
    return new_string
# print(reverse_string("usman"))
# print(reverse_string("one"))
# challenge 5
def first_repeat_character(string: str)-> str:
    repeat_character =""
    for c in string:
        if string.count(c) == 1:
            repeat_character = c
            break
    return repeat_character if repeat_character else "no non repeatative character found"
# challenge 7
def  my_factorial(n: int)-> int:
    n= int(n.strip())
    fac = 1
    while n > 0:
        fac *= n
        n -=1
    return fac


# challenge 8
def challenge_8()-> None:
    while True:
        n= int(input("enter your  number \n").strip())
        if n > 10 or  n < 1:
            break


# challenge 9
def  prime_number_chacker(n: int)-> str:
    n= int(n.strip())
    is_prime = True
    for i in range(2,n):
        if n%i ==0:
            is_prime= False
    return is_prime

# challenge 9
items = ["apple", "banana", "orange", "apple", "mango"]
def  unique_item(items: List[str])-> None:
    duplicate_item =""
    for i in items:
        if  items.count(i) > 1:
            duplicate_item = i
            break
    print( duplicate_item)
# while True:
    # print(prime_number_chacker(input("enter your number \n")))
    # print(first_repeat_character(input("enter your sentence  \n")))
    # print(my_factorial(input("enter your number \n")))
# challenge_8()
# unique_item(items)
# unique_item("usman haroon")
# challenge 10
def expo_backoff_strategy()-> None:
    attempts = 5
    delay_time = 1
    while attempts > 0:
        input("enter your password \n")
        time.sleep(delay_time)
        attempts -= 1
        delay_time= delay_time * 2
        print("you have {} remaining attempts ".format(attempts))

expo_backoff_strategy()