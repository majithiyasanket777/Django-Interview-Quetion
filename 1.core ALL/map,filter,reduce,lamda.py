# map function use hota efficance propse ke liye map ko pehle de do function ka name  fir de  do woh list har eliment me ye function apply karna chate ho...
    
def cube (x):
    return x * x * x

print(cube(2))


l = [1, 2, 4, 6, 4,3]
# newl = []
# for item in l:
#   newl.append (cube(item)) 

newl = list(map(cube,l)) # function name(cube) and list (l) aapi directly function ke under ki arrguments ko run kar dii...
print(newl)


# FILTER  
def filter_function(a):
    return a>4

newnewl = filter(filter_function)

# reduce()
from functools import reduce
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

z = reduce(lambda x, y: x + y, l)  # Sum all numbers
print(z)  # Output: 55


""" What is lamda function ...?

its Anomus function in python jiska name nahi hota hum usko function ke under function pass kar sakte hai ..  
"""

# def double(x):
#     return x*2

# def appl(fx, value):
#     return 6 + fx(value)


# double = lambda x: x*2
# cube =   lambda x: x*x*x
# avg =   lambda x, y, z: (x + y+z) / 3

# print(double(5))
# print(cube(5))
# print(avg(3,5,10))
# print(appl(lambda x: x* x* x, 2))



# def add(x,y):
#     return (x+y)
# print(add(5,5))

# print((lambda x,y: x+y)(5,5))


# filter syntax :- filter(function, iterable)
        
l = [1,2,3,4,5,6,7,8,9,10]

z = list(filter(lambda x: x %2==0,l))

print(z)            

# Map function syntax:- map(function, iterable)
l = [1,2,3,4,5,6,7,8,9,10]

z = list(map(lambda x: x*x,l))

print(z)            


try: 10/5 

except:
    print("zero divsion error")
else:
    print('its your code result') 
finally:
    print("all done")       




# list Comprehension

# my_list =[1,2,3,4,5,6,7,8,9,10]

# print(my_list[::-2])
# 

# my_list = [i for i in range (1,100,3)]
# print(my_list)

#--------------------#-----------------#-----------------#
#1.) Basic syntax of List Comprehension 
# [expresion for item in iterable]

square = [x**2 for x in range(1,6)]
print(square)
# simple second method Basic List Comprehension
# n = [i for i in range(1,51)]
# print(n)

#-------------#-----------------#-----------------#-------#
# 2). List Comprehension with Condition: Syntax
#[expresion for item in itrable if condition]

n = [i for i in range(0,11) if i % 2==0 ]
print(n)
#--------------------#-----------------#-----------------#
# 3). List Comprehension with Function:
# syntax : [function(item) for item in itrable]

def cube(x):
    return x * 2

my_list = [cube(x) for x in range(5)]
print(my_list)
#--------------------#-----------------#-----------------#
# 4) Nested List Comprehension:
# [expression for item1 in itrable1 for item2 in itrable2]

paris = [(x,y)for x in [1,2] for y in [3,4]]
print(paris)
# out put: [(1, 3), (1, 4), (2, 3), (2, 4)]

#--------------------#-----------------#-----------------#
# 5). List Comprehension with Multiple Conditions:
# syntax :- [expression for item in iterable if condition1 and condition2]
numbers = [x for x in range(20) if x % 2 == 0 and x % 3 == 0]
print(numbers)
# Output: [0, 6, 12, 18]







    