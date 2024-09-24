# lamda syntax Argumets:expression

# (practice)*
#--------------#------------------#-------------#---------
# constoructore
# class Fruite:
#     def __init__(self):
#         print("object has been created")
        
#     def show(self,Frute_type):
#         print(f"The Fruite is {Frute_type}.")
# obj = Fruite()
# obj.show('Apple')             
#--------------#------------------#-------------#---------
# 2>costrouctore(parameter rise)

# class Fruite: 
#     def  __init__(self,name,python,English):
#         self.name = name 
#         self.marks = python,English

# obj = Fruite('sanket',90,80)
# print(obj.__dict__)
# obj = Fruite('Amit',90,88)
# print(obj.__dict__)

#--------------#------------------#-------------#---------

# 2) inharitance (multiple)

# class Animal:
#     def speck(self):
#         print("Animal can speak")
        
# class Dog:
#     def walk(self):
#         print("Boww!!")
        
# class Cat(Animal,Dog):
#     def eat(self):
#         print("Mioww!!") 
        
# my_animal  = Cat()
# my_animal.speck()                       
# my_animal.walk()                       
# my_animal.eat()                       
#--------------#------------------#-------------#---------

# 3 polymorphrisum 

# class Animal:
#     def sound(self):
#         print("Animal make sound")

# class Dog(Animal):
#     def sound(self):
#         print("Boww!!!") 
        
# class Cat(Animal):
#     def sound(self):
#         print("Mioww!!!") 
               
# def make_sound(animal):               
#     animal.sound()
    
    
# dog = Dog()    
# cat = Cat()

# make_sound(dog)
# make_sound(cat)
#--------------#------------------#-------------#---------

# mrthod over loading

# class A:
#     def show(self):
#         print('Welcome')
        
#     def show(self,Firstname=''):
#         print('Welcome',Firstname)
            
#     def show(self,Firstname='',Lastname=''):
#         print('Welcome',Firstname,Lastname) 
        
# obj = A()
# obj.show()           
# obj.show('sanket')           
# obj.show('sanket','majithiya')           
#--------------#------------------#-------------#---------
# method -over loading

# class A:
#     def show(self):
#         print('This is child class is heare')
        
# class B(A):
#     def show(self):
#         print('This is a  parant class ')  
#         super().show()   
        
        
# obj = B()
# obj.show()           
# obj.show()           
#--------------#------------------#-------------#---------

# Abstraction

# from abc import ABC,abstractmethod

# class car(ABC):
#    def show(self):
#        print('Every car has been 4 wheels')
       
# @abstractmethod       
# def speed(self):
#     pass

# class maruti(car):
#     def speed(self):
#         print('Maruti speed is 100 km/h')
        
# class Suzuki(car):
#     def speed(self):
#         print('suzuki speed is 70 km/h')
        
# obj = maruti()         
# obj.speed()    
     
# obj = Suzuki()
# obj.speed()         

#--------------#------------------#-------------#---------

# Encapsulation 

# class A:
#     _a = 10 # protected
#     __b = 20 # private
    
#     print('a is =', _a)    
#     print('b is =', __b)

# obj = A()
# print('out side of the class', A._a)        
# print('out side of the class', obj._A__b)        
#--------------#------------------#-------------#---------

# decorator 

# def my_decorator(fx):
#     def wrapper():
#         print('Good Morning')
#         fx()
#         print('Thanks for messageing me..!!')
#     return wrapper

# @my_decorator
# def sanket():
#     print('my name is sanket')      
 
# sanket()    
    
#--------------#------------------#-------------#---------

# Genrator

# def sqr(n):
#     for i in range(1,n+1):
#         yield i**2
# a = sqr(4)
# print(next(a))        
# print(next(a))        
# print(next(a))        
# print(next(a))        
        

# map Efficency puropse ke liye use hota hai...

# syntax map(function, itrable)
# l = [1,2,3,4,5,6,7,8,9,10]        

# z =list(map(lambda x: x*x,l))

# print(z)
# #--------------#------------------#-------------#---------

#--------------#------------------#-------------#---------

# filter syntax:- filter(function,itrable)
# l = [1,2,3,4,5,6,7,8,9,10,11,12]

# z = list(filter(lambda x: x %2==0,l))

# print(z)
#--------------#------------------#-------------#---------
# map syntax:- map(function,itrable)

# Geanerator

# def sqr(n):
#     for i in range(1,n+1):
#         yield i**2
            
# a = sqr(4)
# print(next(a))            
# print(next(a))            
# print(next(a))            
# print(next(a))            
    
#--------------#------------------#-------------#---------
    
# List Comphrsion syntax [expression for itam in itrable] 

# my_list = [n for n in range(1,101)]
# print(my_list)
#--------------#------------------#-------------#---------
# # condtions with list comphrison syntax :- [expression for itam in range if condtion] 
# n = [n for n in range(10) if n %2==0 ]
# print(n)

#--------------#------------------#-------------#---------

# function based List Comphrison syntax:-(function(itam) for in itrable) 

# def cube(x):
#     return x**2

# n = [cube(x) for x in range(6)]
# print(n)

#--------------#------------------#-------------#---------

# itratore

# my = iter(['A','B','C','D'])
# print(next(my))
# print(next(my))
# print(next(my))
# print(next(my))

#--------------#------------------#-------------#---------

# Remove duplicate
# my_list = [10,10,20,20,30,40,65,65]
# remove_duplicate =  set(sorted(my_list))
# print(remove_duplicate)

#--------------#------------------#-------------#---------

# Empty list or not

list = [10]

if  not list:
    print('The list is Empty')
else:
    print('The list is not empty')
    
#--------------#------------------#-------------#---------
# last smallest number in the list


my_list = [90,80,71,50,36,90,18,5]

Last_small = (sorted(my_list))
print(Last_small[1])
#--------------#------------------#-------------#---------

# palindrom or not 

palindrom = "MADAM" 
if palindrom == palindrom[::-1]:
    print ('Yes')
else:
    print('No')    
#--------------#------------------#-------------#---------

# fibonacii

n = int(input("Pleas Enter A number:"))
a = 0
b = 1
c = 0
for i in range(n):
    c = a + b
    a = b
    b = c
    print(c)    


# n = int(input("Enter the number:"))
# a = 0
# b = 1
# c = 0
# for i in range(n):
#     c = a + b
#     a = b
#     b = c
#     print(c)