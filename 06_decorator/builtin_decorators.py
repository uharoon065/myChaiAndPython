#  there are 2 ways that you can  use  decorators  on classes.
# the first one is using decorators   on  methods in classes.It could be builtin decorators as well as your own defined  decorators.
#  in this lecture  we will first use  builtin decorators for quick revision.
class Circle:
    def __init__(self,radious):
        self._radious = radious

    @property
    def radious(self):
        """ get the value of the radious"""
        return self._radious
    @radious.setter
    def  radious(self,value):
        """ settting the value for radious"""
        if self._radious  > 0:
            self._radious = value
        else:
            raise ValueError(" radious must be non negative")
        
    @property
    def area(self):
        """ calculate the area of circle"""
        print(self.py())
        return  self.py() * self._radious**2
    def volume_cylender(self,h):
        """ calculates the volume of cylender as area its base"""    
        return self.area*h
#  the static methods doesnt take any  object or class.
#  static methods are callable by both  instance and class itself.
    @staticmethod
    def py():
        """Value of π, could use math.pi instead though"""
        return 3.1415926535
    #   class methods  takes a class as its arguement  , it is usually use to as factory functions.
    @classmethod
    def unit_circle(cls):
        """creating a instance with radious 1"""
        return cls(1)

c1= Circle(619)
