# class A:
#     _a =10 # protected
#     __b=20 # private
#     def show(self):
#         print("a =",self._a)
#         print("b =",self.__b)
        
        
# obj=A()
# obj.show()
# print("outside of class",A._a)
# print("outside of class",obj._A__b)

   
# class Car:
#     _a = 100
#     __b = 20
#     def show(self):
#         pass

# obj = Car()
# obj.show()

# print("the class is outside",Car._a)
# print("the class is outside",obj._Car__b)

#--------------------#-----------------#-----------------#
# l = []
# for a in range(1,101):
#     l.append(a)
#     print(l)
    

# n=[h for h in range(1,101) if h%2==0 ] # h for variable name same 
# print(n)

#--------------------#-----------------#-----------------#
# n = [s for s in range(1,201)]
# print(n)

# syntax [expresion for item in itrable]

# my_list = [i for i in range(0,11,2)]
# print(my_list)


# [function(item) for item in iterable]

# def double(x):
#     return x * 2

# double = [double(x) for x in range(10)]
# print(double)

#--------------------#-----------------#-----------------#

# marks = [20,30,40,50,60]
# new_marks =[x+2 for x in marks]
# #EX syntax [x+2(karna kya hai) for x (kiske liye karna hai) in marks(or kaha par karna hai) ]
# print(new_marks)

# multiple condition List comphrasions
# syntax [exprasion for itam in itable if condtions  and if condtion]
# my_cube = [n for n in range(20) if n%2 == 0 and n%3==0]
# print(my_cube)

# numbers = [x for x in range(20) if x % 2 == 0 and x % 3 == 0]
# print(numbers)
# Output: [0, 6, 12, 18]

#--------------------#-----------------#-----------------#

# # Encapsulation 

# class A:
#     _a =10 # protected
#     __b=20 # private
#     def show(self):
#         print("a =",self._a)
#         print("b =",self.__b)
        
# obj=A()
# obj.show()
# print("outside of class",A._a)
# print("outside of class",obj._A__b)

# A._a # protetecd
# obj._A__b # private

# Encapsulation 
# class A:
#     _a = 10 # protected
#     __b =20 # private
#     def show(self):
#         print("a =", self._a)
#         print("b =", self.__b)
        
# obj = A()
# obj.show()
# print("out side of class",A._a)        
# print("out side of class",obj._A__b)        


# Decorater in python (important Topic in interview...)

#  kisi function ko ek or  function ke under pass kar sakte hai As a Argumet 
# koi function  bana ke rakha hai usko modifyed karna chahte ho or behaviour ko change karna chahte ho to aap usi function ko kisi or function me pass karo And woh uss function ke behaviour ko update kar dega fir woh ek naya function return kar dega...

# def my_decorator(xy):
#     def wrapper():
#         print("Good morning")
#         xy()
#         print("Thank for messagesing ")
#     return wrapper

# @my_decorator
# def gretter():
#     print('Hello i am sanket')    
# gretter()      


# function  har function ke use karne se pehle  Good morning run hoo uske baad thank you for using this func run hoo..(function modfly)
  
# show('hello')          
    
# def my_decorater(fx):
#     def wrapper(*args, **kwargs):
#         print('Good morning') 
        
#         result = fx(*args, **kwargs)
#         return result
#     return wrapper

# @my_decorater    
# def greet(name):
#     print(f'hello {name}.')      
# greet('sanket')



# List Append and extend And All methods () 

# import copy

# a = [1,[2,3]4]


# Dict key value (example) And set default Example 
#--------------------#-----------------#-----------------#
# practice 

# constoctore :- 
# class Fruite:
#     def __init__ (self):
#             print('object has been created')

#     def show_type(self,fruite_type):
#         print(f'The fruite type is {fruite_type}')
        
# obj = Fruite()
# obj.show_type('Apple')             

#--------------------#-----------------#-----------------#   

# constoructore

# class Fruite:
#     def __init__(self,name,python,English) -> None:
#         self.name = name
#         self.marks = python,English
        
# obj = Fruite('sanket',90,80)
# print(obj.__dict__)
# obj2 = Fruite('Amit',80,80)
# print(obj2.__dict__)        
        
#--------------------#-----------------#-----------------#   
# inharitance 

# class Animal:
#     def speack(self):
#         print('Animal can make sound') 
        
# class Dog:
#     def walk(self):
#         print('Boww!!')
        
# class Cat(Animal,Dog):
#     def eat(self):
#         print('Mioww!!')
        
# my_animal = Cat()

# my_animal.walk()        
# my_animal.eat()        
                           
#--------------------#-----------------#-----------------# 
# polymorphrisum

# class Animal:
#     def sound(self):
#         print("The animal makes a sound")

# class Dog(Animal):
#     def sound(self):
#         print('Boww!!!')
        
# class Cat(Animal):
#     def sound(self):
#         print("Mioww")
        
# def make_sound(animal):
#     animal.sound()     
    
# obj1 = Animal()
# make_sound(obj1)    

# obj1 = Cat()
# make_sound(obj1)               
        
# obj2 = Dog()               
# make_sound(obj2)               

#--------------------#-----------------#-----------------#
# method overloading
# class A:
#     def show(self):
#         print('Welcome')
        
#     def show(self,firstname= ''):
#         print('Wlcome',firstname)
        
#     def show(self,firstname= '',Lastname=" "):
#         print('Wlcome',firstname,Lastname)

# obj = A()
# obj.show()
# obj.show('sanket')
# obj.show('sanket','majithiya')
        
#--------------------#-----------------#-----------------#   
# method overriding (possibal in python A-B me inharit)


# class A:
#     def show(self):
#         print('This is a parant class')
        
# class B(A):
#     def show(self):
#         print("This is child class") 
#         super().show()
        
# obj = B()
# obj.show()               
#--------------------#-----------------#-----------------#                  
# constoructore 

# class Fruite:
#     def __init__(self,name,python,English) -> None:
#         self.name = name
#         self.marks = python,English
        
# obj = Fruite('sanket',90,80)
# print(obj.__dict__)     
   
# obj2 = Fruite('Amit',90,88)
# print(obj2.__dict__)        
         
#--------------------#-----------------#-----------------#   
# Abstraction
# from abc import ABC,abstractmethod
# class Car(ABC):
#     def show(self):
#         print('the evry car has been 4 wheels')
        
#     @abstractmethod   # decorater     
#     def speed(self):
#         pass

# class Maruti(Car):
#     def speed(self):
#         print('Maruti speed is 100km/h')
                       
# class Suzuki(Car):
#     def speed(self):
#         print('Suzuki speed is 70km/h')               
             
# my_car = Maruti()
# my_car.speed()
# my_car.show()
           
# my_car = Suzuki()             
# my_car.speed()    
# my_car.show()
#--------------------#-----------------#-----------------#   
# Encapuslation
# class A:
#     _a = 10  # protected
#     __b = 20 # private
    
# def show(self):
#     print('A=',self._a)    
#     print('b =',self.__b) 
    
# obj = A()
# print('out side of class is A',A._a)       
# print('out side of class is ',obj._A__b)       
#--------------------#-----------------#-----------------#    
# decorater
# def my_decorater(fx):
#     def wrapper():
#         print('Good Morning')
#         fx()
#         print('Thanks for using this function')
#     return wrapper

# @my_decorater
# def greet():
#     print('hello sanket')
    
# greet()    
#--------------------#-----------------#-----------------#  

# List compharision
# syntax [expression for itam in itrable]
# my_List = [n for n in range(1,101)]
# print(my_List)
# #--------------------#-----------------#-----------------#  
# my_List = [n**2 for n in range(6) ]
# print(my_List)
#--------------------#-----------------#-----------------#  

# List compharshion with condtion
# syntax :- [expression for itam in itrable if condtion]

# my_list = [n for n in range(1,11) if n %2==0 ]
# print(my_list)

#--------------------#-----------------#-----------------#  
# List compharshion with multiple condtion
# # syntax :- [expression for itam in itrable if condtion  if contion ]

# my_list = [n for n in range(1,101) if n %2==0  if n%3==0]
# print(my_list)
#--------------------#-----------------#-----------------#  
# List compharsion with using function 
# syntax :- [function(itam) for itam in itrable]
# def cube(x):
#     return x**2

# my_list = [cube(x) for x in range(20)]
# print(my_list)


#--------------------#-----------------#-----------------#  
# Append-Extend
# my_list = [1,2,3]
# my_list.append(4)
# print(my_list)
#--------------------#-----------------#-----------------#  
# my_list1=[1,2,3]
# my_list1.extend(([4,5,6,7],[8,9]))
# print(my_list1) 

#--------------------#-----------------#-----------------#  
# 1.) how to remove Duplicate lis

# list = []

# if not list:
#     print("The list is empty")
# else: 
#     print("The list is not empty")
#--------------------#-----------------#-----------------#  

# 2.) how to remove Duplicate list    
# my_list = [1,2,1,2,4,4,5,60,60,40,40]
# remove_list = (list(set(my_list)))
# print(remove_list)  
#--------------------#-----------------#-----------------#  
# 3.) find the second smallest number in list .

# my_list = [20, 30, 40, 50, 60, 70, 90, 100]
# square = sorted(my_list)
# print(square[1]) 
#--------------------#-----------------#-----------------# 
# map filter reduce 

# map (Efficency purpose ke liye hum use karte hai...)

def cube(x):
    return x**2

print(cube(2))
 
#--------------------#-----------------#-----------------# getter syntaxt:-@property laga di to woh getter ban gaya.[in python are methods that are used to access the values of an object's properties.] New Method baan rahe jo behave kar raha hai like a property.
#**Actualy use :- kisi function ki return value ko Ek object ki property ki Tarah istmaal kar sakte hai And usko set bhi kar sakte hai 

# class Myclass:
#     def __init__(self,value):
#          self._value = value
#     def show(self):
#         print(f"value is {self._value}")     
        
#     @property # getter ye decorator hai hamara
#     def ten_value(self):
#         return 10* self._value
    
#     @ten_value.setter # setter Decorater 
#     def ten_value(self,new_value):
#         self._value = new_value/10
#         # return 10* self._value
    
# obj = Myclass(10)
# obj.ten_value = 67
# print(obj.ten_value)
# obj.show()

 
#setter syntax:- @(property-name).setter 
# @ten_value.setter       
 
#--------------------#-----------------#-----------------# 
# my_list = [n for n in range(1,201)]
# print(my_list) 


# numbers = list(range(1,101))
# print(numbers)
#--------------------#-----------------#-----------------# 
# genratore use ek ek value kod  genrate kiya jaa raha hai, store kiya jaa raha hai, and use kiya jaa raha hai 
# return retruns value and stop programe
# yield :- object Ata hai Ager next naa laagte hai (pause kar deta hai program to chalega.)


def sqr(n):
    for i in range(1,n+1):
        yield i**i
a = sqr(4) 
print(next(a))       
print(next(a))       
print(next(a))    

for a in a :
    print(a)    

#--------------------#-----------------#-----------------# 
# Genrator use 

def sqr(n):
    for i in range(1,n+1):
        yield i**i
        
# a = sqr(5)
# print(next(a))            
# print(next(a))            
# print(next(a))            
# print(next(a))            
# print(next(a))  

a = sqr(5) 
for a in a:
    print(a)  
           
#--------------------#-----------------#-----------------# 
