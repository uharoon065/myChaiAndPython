# all iterators objects are iterable but all iterable object are not iterator object . 
# iterator  and iterable objects must have dunder method iter , but the iter object must define __next__() method which is to say iter protocole.
# the loops automatically calls the  iter()  method to make an iterator object if the object is iterable it will return iterator object but if it already is an iterator it iwll return itself 
""" https://realpython.com/python-iterators-iterables/#:~:text=Python%27s%20iterators%20and%20iterables%20are,one%20value%20at%20a%20time.excelent article to learn about iterators and generators nad iterators types """
# clasic iterator 
class Sequence_iterator :
    def __init__(self,sequence) -> None:
        self._sequence = sequence
        self._index = 0
#  must define iter method in order to make the object iterable and work for loops
    def __iter__(self):
        return self
    #  must define __next__() method to make the  object an iterator object
    def __next__(self):
        if self._index < len(self._sequence):
            item = self._sequence[self._index]
            self._index += 1
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