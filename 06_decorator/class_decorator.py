from realWorldExamples import  timer,debug
# you can apply decorators to  class itself the difference would be instead of passing a function to the decorator you would be passing a class .
#  your_class= decorator(your_class)
#  the decorator on class will only return  the time it took to instanciate  an object.
#  note that decorating the class does not mean you have  decorated its methods as welll.
#  @debug
@timer
class waste_timer:
    def __init__(self,mmax_num):
        self._mmax_num = mmax_num

    def wasted_time(self,num_times):
        for  n in range(num_times):
            sum([num**2 for num in range(self._mmax_num)])

tw = waste_timer(100)