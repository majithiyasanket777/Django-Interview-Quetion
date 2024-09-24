# Q -1 whether string is palindrome or not ?

# using slicing 1st method

palindrom = "MADAM"
if palindrom==palindrom[::-1]:
    print("yes")
else:
    print("No")   
    
# using loop from 0 to len/2   2nd method

# def ispalindrom(s):
#     n =len(s)
#     for i in range(0, int(n/2)):
#         if s[i] != s[n-i-1]:
#             return 'No'
#         return 'Yes'
    
#     s = "sanket"
#     print(ispalindrom(s))
    
# Q-2  Create fibonacci series using recorsion..? 
# with out recorsion 
            
n = int(input("Enter the number:"))
a = 0
b = 1
c = 0
for i in range(n):
    c = a + b
    a = b
    b = c
    print(c)
    
# List compareinsion(code ka size Dicrese hota hai Number of lines kaam hojati hai...)

# 1. Basic List Comprehension Syntax:-
# [expression for item in iterable] 
# EX :-
square = [x**2 for x in range(1,6)]
print(square)    
    
# with  recorsion means function call it self again and again (ye tab use hoga jab for loop ke bina baar baar condition repeat karani ho hume or out put chahiye ...)



# Q-3 count No of ocurrence of A character in A string Also print charcter & it's count

# Q- 4 Diffrence Between Generators And iterators....

"""
  GENERATOR :- --> generator use "yied" keyword koi pertucular value lene ke liye ...
  ---> every generator is an iterator...
  ---> generator is lazy, it only generates values when asked for.
  ---> generator can be used to create an infinite sequence of values.
   
  EX:-  
"""
def sqr(n):
    for i in range(1,n+1):
        yield i*i
a = sqr(3)
print(next(a))
print(next(a))
print(next(a))

"""
ITERATOR : --->Every iterator is not a generator
---> Iterator is an object that defines the sequence
---> Iterator uses iter() and next()functions.
---> ye values ko one by one lega contains countable numbers of values and it is used to iter objects like list,tuple sets etc
EX:-        
"""
iter_list = iter(['A','B','C'])   
print(next(iter_list))    # A
print(next(iter_list))    # B
print(next(iter_list))    # C
#--------------------#-----------------#-----------------#  
# Dict set-Default 
my_dict = {
    'Model':'BMW',
    'Colour':'Red'
} 
my_dict.setdefault ('Model','Range rover')
my_dict.setdefault ('Colour','Black')
print(my_dict)

#--------------------#-----------------#-----------------#
# List Append or extend methods :-
# my_list = [1,2,3]
# my_list.append(4)
# print(my_list)
#--------------------#-----------------#-----------------#
# Extend 
my_list = [1,2,3]
my_list.extend(({4,5,6,7,8}))
print(my_list)
#--------------------#-----------------#-----------------#
# 1.) how to remove Duplicate list  
my_list = [20,20,30,40,80,80,-20,-20,30]

unique_value = (list(set(my_list)))
print(unique_value)
#--------------------#-----------------#-----------------#
#2.) List is emty or not

list2 = []

if not list2:
    print('list is emtey')
else:
    print("The List is not Empty")  

#--------------------#-----------------#-----------------#
#3) Write a Python program to find the second smallest number in a list.   
my_list = [10,20,50,30,40,60,5,10]

squence_list = (sorted(my_list))

print(squence_list[1])
#--------------------#-----------------#-----------------# 
# 4) # convert  tuple to dictionary t
my_list = [("sanket","majithiya"),("prashant","Bhai"),("Age",21)]

my_dict = (dict(my_list))
print(my_dict) 
  
# output :- {'sanket': 'majithiya', 'prashant': 'Bhai', 'Age': 21}  
#--------------------#-----------------#-----------------#   


# Q- 5 what is Decorator Explain With Example ...
   
# jab bhi hum ek function me Dusre kisi function ko call karte hai usse Decorater kaa name de dete woh function me without change function uski sari functionality ajayegi...
# example :-
# @my_decorator
# def my_function():
#     pass
# my_function()  # my_function() function ko modify kar dega my_decorator function


    
# Q-6 what & which Are Mutable & Immutable Datatypes In python?

"""
mutable data type in python
LIST is mutable usme run time hum changes kar sakte hai
Dict :- key :- mutable and value :- immutable

immutable :- string, Tuple, set

"""

# Q-7 Difference between The Break & Continue Statement ?
"""
jab bhi hum for loop yaa while loop ka use karte hai tub hum break yaa continue statements kaa use karte hai 

break statement :- break jab chalti hai tab uske baad kaa jitna bhi execution hota hai particular loop kaa woh bandh hojata hai woh wahi se nikal kar bhar ajata hai

Continue Statement :- 
uske aage wali itration to nahi chalti lekin uske next wali chalne lagti hai  (woh use ko skip kar degi waha se...) woh for loop fir se work karti hai ...
"""
# Q-8  what is Diffrence Between *args & **kwargs ?
# ANS :- Basicaly hum function definede karte hai or jab Hume pata nahi hota hai isme kitne Number off parameter jayenge Tab hum ye dono kaa use karte hai  
# list me parameter Bhej rahe hote hai tab use karte hai only (key)
# **kwaegs:- Dict me  hum key values parameter behj te hai  tab use karte hai  

# Q-9 what is GIL in (Global  Interpretor Lock) python

# ek time par multiple Thereds bhi run hone lagte hai hum deadlock kind situation me naa fass jaye. AND Ek time par ek hi Thred ka use kare uske liye hum GIL kaa use karte hai ... 

# Q-10 Explain request & Response Cycle In Django?

# Q-11 How To Fetch Data from Database Using Query Set?

# ANS:= A Query is a collection of SQL queries...
# A query set in Django is basically a collection of objects from our database.. 

# user.object.all() all Data behj na hai tab Table se
#       user.object.filter(name="nitin") sirf name behj na 
#       user.object.get(id=3) sirf id ,on by on behj naa 

# Q-12 makemigrations commond use of data bases
# ANS:- python manage.py makemigrations ()




# ROUND 2 :=


# Q-1 Find the maximuum and min value from a list without using any predefind function
"""
 Q-2 find Requried Output? revese string find
 Input-    'the sum is yellow'
 output-   'yellow is sun the'

"""
# string = 'the sun is yellow'
# string = string.split()
# string = string[::-1]
# print(string)

# or
# print(''.join(string.split()[::-1]))

# Q-3 Tell me about Oppos (Inharitance ,polymorphrishm,encapsulation....)

# Q-4  How Exception Is Handled In python?
"""
"""
try:
    # Trying to divide by zero
    result = 10 / 0
except ZeroDivisionError:
    # Handling the error
    print("Error: You can't divide by zero!")
else:
    # This block runs if no exceptions occur
    print(f"Result: {result}")
finally:
    # This block always runs
    print("End of the operation.") #(Deffienty runkare) 


# Q-5 Differnce beteen select_related & prefetch_related ?

# Ans:=
"""
Hamare pass Models hai uska connection Ager foregin Key ke sath hoga usme Ek(1) to hum data base ko heat kare or waha se result leke aaye  
second(2) chiz ki hum  ek Data ko load kar rahe hai to sath me Dusre ko bhi load kara le  Takki hume baar baar Data Base me jaane ki jaroorat na pade to hum uske liye ye dono chiz ka use karte hai 
"""

# Q-6  What is Django ORM ?
# ANS:= Data base related queries likh ni hoti hai tab hum Django ORM kaa use karte hai. Django me hum  queryset use karte hai woh Django ORM based hi hoti hai Woh sab ko use kar ke hum Data base me kisi bhi Tarah ki modification kar sakte hai..

# Q-7  Ager kya hoga hum get function use katre hai query set me or usko particular Record na mile To kya situation Ho sakti hai ...     

# ANS:= DoesNotExist exception ki error Ajati hai usko hume handle karna padta hai            


# Q-8 Difference Between Authorization & Authentication?

# ANS := Authentication ---> who Are you?
# Authorization ----> what permissions Do you Have?

# Q-9 Have you Ever Start The project From the Scratch ?

# ANS := kis Tarah se  Pehle low level Design kiya fir High level Design kiya . Data Base kese Create kiya .client se kese baat karta tha. Devlopment kese kii back End kese chal raha tha Front End kese chal raha tha mera kya contribution uss particular project me Explain kii...

# Q-10 Explain Current Project ..?






