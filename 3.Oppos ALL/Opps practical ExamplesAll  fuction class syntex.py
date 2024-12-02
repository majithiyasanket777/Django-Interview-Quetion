"""what is Attributes :- variable in class basicaly its Attributes
Ex :- name : str = str()
Ex :- university : str = str()

what is methods :-
in side the class funtion are non as methods 
Ex  :- def pass_fail():
           for  element in marks:
                if element <50:
                print("fail") """
                
# what is instance (constorctore ke under jo variable ata hai )           

# f = open("c:/Users/sanke/OneDrive/Desktop/python practice/python core practice/chapeter 9/file.txt")
# data = f.read()
# print(data)
# f.close()

    
# st = "hey sanket how are you brother"

# f = open("my file.txt", "w")

# f.write(st)

# f.close()    

# try:
#     result = 10 / 2
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# else:
#     print(f"Division successful, result is {result}")


# 1. constructor
# Example 2 pro*fasinal
class Fruite:
    def __init__(self):
        print('object has been created')
        
    def show_type(self,fruite_type):
        print(f'This is a{fruite_type}.')
        
        
my_fruite = Fruite()
my_fruite.show_type('Apple')     

# 2. constructor
class Fruite:
    def __init__(self,name,python,English) -> None:
        self.name = name
        self.marks = python,English
        
obj = Fruite("sanket",80,95)
print(obj.__dict__) 

obj2 = Fruite("yes",90,80)
print(obj2.__dict__)       
        
# 2. Inharitance (Single)

# class Animal:
#     def speak(self): # kuhd ko hi object banalega 
#         pass
    
# class Dog(Animal):
#     def speak(self):
#         print("woolf!")  
              
# my_dog = Dog()
# my_dog.speak()

#--------------------------------------------#

# (Multiple - Inharitance)

# class Animal:
#     def speack(self):
#         print("Animal can speek")
    
# class Dog:
#     def walk(self):
#         print("BOWW!!")
        
# class Cat(Animal,Dog):
#     def speack(self):
#         print("Meow!!")        
        
# myAnimal = Cat() # Cat ke under sab Ajyega Animal and Dog

# myAnimal.speack()       
# myAnimal.walk()       
    
# 3. Polymorphism 
# in python method overriding is possibal and supported
# and method overloading are not supported

class Animal:
    def sound(self):
        print('animal sounds ')
        
class Dog(Animal):
    def sound(self):
        print("BOWW!!") 
         
class Cat(Animal):
    def sound(self):
        print("Miowww!!")
          
def make_sound(animal):
     animal.sound()
     
dog = Dog()
cat = Cat() 

make_sound(dog)   
make_sound(cat)

#------------------#--------------------#
# second method while calling Polymorphism
# myAnimal = Dog()                      
# make_sound(myAnimal)

# myAnimal = Cat()                      
# make_sound(myAnimal)

#-----------------method Overloading---------------#
# 1 class me multiple function honge yaa Ek hi function ko hum multiple time call karenge Alag Alag value ke through..
class A:
    def show(self):
        print("Welcome")
        
    def show(self,Firstname=''):
        print("Welcome",Firstname) 
        
    def show(self,Firstname='',Laststname=''):
        print("Welcome",Firstname,Laststname) 
        
obj =A()
obj.show()   
obj.show('Ankush')         
obj.show('Ankush','majithiya')         
   
#-----------------methodOverriding---------------#        

class A: # parent
    def Disp(self):
        print("This is parant class method..!! ")

    
class B(A):    
    def Disp(self):
        super().Disp() # paranet class ko inhar
        print("This is child class method")
        
obj =B()
obj.Disp()                
        
#---------------#----------------#----------------#

# Abstractioin abc(abstract base classes)
# Action common ho lekin immplimtation diffrent 
# Abstract method ka koi bhi body nahi hota
# car hamara Abstract class bana uska object createnahi.hoga

from abc import ABC,abstractmethod

class Car(ABC):
    def show(self):
        print("Every car has 4 wheels")
    @abstractmethod # decorater
    def Speed(self):
        pass
    
class Maruti(Car):
    def Speed(self):
        print("speed is 100km/h")
        
class Suzuki(Car):
    def Speed(self):
        print("speed is 70km/h")
                
car = Maruti()
car.Speed()   # iske niche(speed)likhenge to same name ka 
car.show()   #  function hoga to easily samz jaayega 2 noo me.

car = Suzuki()
car.Speed()
car.show()
#---------------#----------------#----------------#

# Encapsulation 
# (function public rahega or variable hamara private rahega)
# 1. _single under(protected[class ka  function or class kaa object use kar paayega])
# 2. __double (private[class ka function hi sirf uss variable ko access kar sakta hai. object* bhi nahi kar sakta ])
# python me har class Encapsulation ka Example hai   
        
class A:
    _a =10 # protected
    __b=20 # private
    def show(self):
        print("a =",self._a)
        print("b =",self.__b)
        
obj=A()
obj.show()
print("outside of class",A._a)
print("outside of class",obj._A__b)
    
#---------------#----------------#----------------#
# syntax :- 
# def decorator(func):
#     def wrapper(): # wrape karna gift box ko wrap karna
#         print('Transaction intiated')
#         func()
#         print('Transaction completed') 
#     return wrapper
# @decorator
# def hello(): # ye hamara original function
#     print('...Excuting all steps of Transaction...')
# hello()   # call kara vo hamare original function ko 

#---------------#----------------#----------------#
# Decorater
def my_decorater(fx):
    def wrapper():
        print("good morning")
        fx()
        print("Thanks for using This function")
    return wrapper
        
@my_decorater
def greet():
    print('hello world')

greet()
#---------------#----------------#----------------#-------
# getter syntaxt:-@property laga di to woh getter ban gaya.[in python are methods that are used to access the values of an object's properties.] New Method baan rahe jo behave kar raha hai like a property.
#**Actualy use :- kisi function ki return value ko Ek object ki property ki Tarah istmaal kar sakte hai And usko set bhi kar sakte hai 

class Myclass:
    def __init__(self,value):
         self._value = value
    def show(self):
        print(f"value is {self._value}")     
        
    @property # getter ye decorator hai hamara
    def ten_value(self):
        return 10* self._value
    
    @ten_value.setter # setter Decorater 
    def ten_value(self,new_value):
        self._value = new_value/10
        # return 10* self._value
    
obj = Myclass(10)
obj.ten_value = 67
print(obj.ten_value)
obj.show()

#setter syntax:- @(property-name).setter 
# @ten_value.setter       

#---------------#----------------#----------------#-------
# @my_decorator
# def my_function():
#     pass
# my_function()  # my_function() function ko modify kar dega my_decorator function


# # Demonstrating polymorphism
# make_sound(dog)  # Output: Bark
# make_sound(cat)  # Output: Meow

# Duck method on Polymorphism
# my_list = [1,2,3,4,5]
# my_list = "hello world"
# print(len(my_list))



# class Book:
#     def __init__(self,price,totalpages):
#         self.price = price
#         self.totalpages = totalpages
    
#     def __len__(self): # Ager len likha hoga to woh hoga access karega 
#         return self.totalpages    
        
# book = Book(200,400)
# print(len(book))



""" 
HTML 1 week 
css  2 weeks 
properties ....
 padding 
 marging
 widhth 
 highet 
 flex
 
 LIST :- []
 Dict :- {}
 tuple:- ()
 set  :- {}
 
loops :-

for i in range(1, n+1):
print(i)
 
accessing dict 
""" 

#Adding dict
# accesing = {'name':'sanket', 'age':25}
# name = accesing["email"] ="sanketmajithiya@gmail.com"
# print(accesing)
 


# conctoructor

# class Fruite:
#     def __init__(self):
#         print("object has been created")
    
#     def __init__(self,Applyed_fruite):
#         print(f"The fruite is{Applyed_fruite}.")
        
# my_fruite = Fruite()
# my_fruite.self('Apple')        
        
# class ATM:
#     def __init__(self,pin):
#         self.__pin = pin
        
# a = ATM("1234")
# print(a.pin)



