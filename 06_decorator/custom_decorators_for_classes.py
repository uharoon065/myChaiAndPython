# using custom decorators on classes 
#  note that the the wrapping of e mmethods happens at the time of class definition you can see that by uncommenting the print statements inside the  timer and debug decorators respectively.
from realWorldExamples import debug,timer
class waste_timer:
    @debug
    def __init__(self,mmax_num):
        self._mmax_num = mmax_num

    @timer
    def wasted_time(self,num_times):
        for  n in range(num_times):
            sum([num**2 for num in range(self._mmax_num)])


# tw = waste_timer(1000)