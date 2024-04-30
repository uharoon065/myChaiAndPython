#  https://realpython.com/python-iterators-iterables/#:~:text=Python%27s%20iterators%20and%20iterables%20are,one%20value%20at%20a%20time.excelent 
# clasic iterator 
class Sequence_iterator :
    def __init__(self,sequence) -> None:
        self.__sequence = sequence
        self.__index = 0
#  must define iter method in order to make the object iterator and work for loops
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__index < len(self.__sequence):
            item = self.__sequence[self.__index]
            self.__index += 1
            return item
        else:
            raise StopIteration

sq_ittr = Sequence_iterator([ x**x  for x in range(1,11)])
start = sq_ittr.__iter__()
# print(type(sq_ittr),type(start))
# print(sq_ittr.__next__())
print(sq_ittr is start)
# calls the sq_iter.__iter__() to initiate the iterator 
# for i in sq_ittr:
# for i in start:
    # print(i)
# print(sq_ittr.__next__())
# print(sq_ittr.__next__())
# print(sq_ittr.__next__())
# print(sq_ittr.__next__())
# print(sq_ittr.__next__())
# print(sq_ittr.__next__())
# print(sq_ittr.__next__())
# print(sq_ittr.__next__())
# print(sq_ittr.__next__())
# print(sq_ittr.__next__())
# print(sq_ittr.__next__())# simulating how for loop works
# initiate the iterator 
i = sq_ittr.__iter__()
while True:
    try:
        item = i.__next__()
        print("inside try")
    except StopIteration:
        print("inside except")
        break
    else:
        print("inside else")
        print(item)