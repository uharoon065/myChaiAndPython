# generators are functions   that allows you to create iterators in functional style.
#  the function that yield something is called generator .
#  the generator returns a generator_iterator.which allows you to yield  value one at a time.
# the generator  automatically implements iterator protocole.
def g1():
    yield 1

gen_iter1= g1()

# print(type(g1)) -> func
# print(type(gen_iter1)) generator object
# sequence generator equvelent to our custom made  class based  squence iterator.
def gen_squence(sq):
    for i  in sq:
        yield i

# g_s1= gen_squence([ x for  x in "mango"])
# print(type(g_s1))
# for x in g_s1:
#     print(x)
#  generator expressions 
# syntax -> (  val for var in iterable)
# gen_expresson = ( [x,y] for x,y in enumerate("usman"))-> gen expression
# print(type(gen_expresson))
# for x in gen_expresson:
#     print(x)
# feb generator 
def feb_gen(stop=5):
    (current_number , next_number)=(0,1)
    for i in range(0,stop):
        feb_number = current_number +   next_number
        current_number,next_number = (next_number, feb_number)
        yield feb_number

# for f in feb_gen(10):
    # print(f)
    #  this will  implicitHHly consume   iterator.
    # print(list(feb_gen()))
    

# for f in feb_gen(10):
    # print(f)
    #  this will  implicitHHly consume   iterator.
    # print(list(feb_gen()))
# you can also terminate a generator function by using return statement in a generator function which will automatically raise StopIteration exception.

def feb_gen2(stop=5):
    (current_number , next_number)=(0,1)
    index = 0
    while True:
        if index == stop:
            return
        feb_number = current_number +   next_number
        current_number,next_number = (next_number, feb_number)
        yield feb_number
        index +=1

gen_obj= feb_gen2()
# print(next(gen_obj)) when the iterator is consumed it will throw StopIteration exception
