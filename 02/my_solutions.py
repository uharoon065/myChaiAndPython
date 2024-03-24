from datetime import date
# challenge 1
def age_grouping(age):
    age = int(age.strip())
    if age<13:
        print("your are  child")
    elif age    >= 13 and age <= 19:
        print("your {} and catagorize as   teanager".format(age))
    elif age >= 20  and age <= 59:
        print("you areare {} and catigorized as adult".format(age))
    else:
        print("you are senior ")

# challenge 2
def movie_ticket(age):
    # pass
    today =  date.today().weekday()
    age = int(age.strip())
    if today ==2:
        print(f"your getting a discount of  $2 today")
    else:
        print("the price of movie ticket is ",sep="")

    if age >= 18:
        print(f"${12 - 2 if  today == 2 else 12}")
    else:
        print(f"${8 - 2 if  today == 2 else 8}")
# challenge 3
        
def student_grade(percentage):
    percentage = int( percentage.strip())
    if percentage > 100:
        print("your not a human ")
        exit()
    print("you got  ")

    if percentage >= 90:
        print("A ")
    elif percentage  >=  80:
        print("B")
    elif percentage  >= 70:
        print("c")
    elif percentage >= 60:
        print("D")
    else:
        print("F")

# challenge 4
def fruit_ripe(color):
    color =  color.strip().lower()
    if  color == "brown":
        print("Overriped")
    elif color == "green":
        print("Unriped")
    elif color == "yellow":
        print("Riped")
    else:
        print("unknown state")
# challenge 5
def weather_suggestion(weather):
    weather = weather.strip().lower()
    match weather:
        case "sunny":
            print("Go for a walk")
        case "rainy":
            print("Read a book")
        case "snow":
            print("Make a snowman")
        case _:
            print("Stay at home")
def transportation_mode(distance):
    distance = int(distance.strip())
    if distance  < 3:
        print("you should  walk")
    elif distance < 15:
        print("you should take a bike")
    else :
        print("you should drive a car")
def coffee_customization(order: str)-> str:
    order = order.lower().strip()
    extra_shot =  input("do you want extra shot ? Y/N").strip()
    if extra_shot == "y":
        extra_shot= "with"
    else:
        extra_shot="without"
    return f"here is your  {order} coffee { extra_shot} shot  of expresso"
def password_strength(password: str)-> None:
    password = password.strip()
    password = len(password)
    if password < 6:
        print("week")
    elif password < 10 :
        print("medium")
    else:
        print("strong")
def leapYear(year: int)-> None:
    year= int(year.strip())
    is_year_leap=True
    #  here parantheses  ensure that  and operator does not cause shortcircuting 
    if (year % 100 == 0 )and (year%400 != 0):
        is_year_leap=False
    elif year%4 == 0:
        is_year_leap=True
    else:
        is_year_leap = False
    print(is_year_leap)
    return f"{year  } is {"" if is_year_leap  else "not"}  a leap year"
# challenge 10
def   food_recommendation(specie: str,age: int)-> None:
    specie = specie.strip().lower()
    age= int(age.strip())
    match specie:
        case "dog":
            if age < 2:
                print("you are getting puppy food")
            else:
                print("your getting adult dog food")
        case "cat":
            if age > 5:
                print("you are getting senior cat food")
            else:
                print("you are getting kitty cat food ")
        case _:
            print("unknow specie type")


while True:
    food_recommendation(input("enter the specie"),input("enter the age"))
    # print(leapYear(input("enter the year ")))
    # password_strength(input("enter your password"))
    # print(coffee_customization(input("enter your order ")))
    # fruit_ripe(input("enter the fruit color") )
    # student_grade(input("enter the student percentage "))
    # weather_suggestion(input("enter the weather "))
    # transportation_mode(input("enter the prompt"))