# challenge one , two
class Car:
    def __init__(self,brand,model,fule) -> None:
        # self.model =model 
        self.__model =model 
        # self.brand = brand 
        self.__brand = brand 
        self.fule=fule
    def fullname(self):
        return f"{self.brand} { self.__model}"
    def get__brand(self):
        return self.__brand
    
    def fule_type(self):
        return self.fule
    
    def set__brand(self,name):
        self.__brand_brand=name
#  static methods are avalible both for instance and class itself but they dont have access to instance (self)
    @staticmethod
    def describe():
        # print(self.__model)
        return "cars are really good means of transport"
#  this property dcorator turns  the  model func into attr  and it will act like a getter 
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self,value):
        self.__model=value

# alto=  Car("suzuki","alto")
# print(alto)
# print(
#     alto.fullname()
# )
# challenge 3
class ElectricCar(Car):
    def __init__(self, brand, model, fule ,battery_size) -> None:
        super().__init__(brand, model,fule)
        self.battery_size=battery_size
        self.fule= fule

    def fule_type(self):
        return self.fule

# tessla   =  ElectricCar("tessala","model x","100kwv")
# print(tessla.battery_size)
# challenge 4
# swift = Car("suzuki","swift")
# print(swift.__brand) the attrbute has been made private
# print(swift.get__brand())
# chalenge 5
korala = Car("hondai","korila","petroal ")
tesla = ElectricCar("tesla","X","electricity","100kvw")
# print(korala.fule_type())
# print(tesla.fule_type())
# challenge 7
# print( korala.describe())
# print(Car.describe())
# challenge 8
# print(korala.__model)
# print(korala.model)
# korala.model="GLI"
# print(korala.model)
# challenge 9
# print(isinstance(tesla,ElectricCar))
# print(isinstance(tesla,Car))

# challenge 10
class Battery:
    def battery_info(self):
        print(" my battery is super charge")

class engine:
    def engine_info(self):
        print("my engine is really powerful")
class ElectricCar2(Battery,engine,Car):
    pass

new_tesla= ElectricCar2("phonix")
new_tesla.battery_info()
new_tesla.engine_info()