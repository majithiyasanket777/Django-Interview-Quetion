# A = 100
# b = 2

# print(A+b)
# print(A-b)
# print(A*b)
# print(A/b)
# print(A%b)
# print(A**b)


""" python is case sensitive
    """
    
    
# list = [1,2,3,4,5,8,10],60    
# print(list[3:6:-1])

#--------------#------------#----------------# 
# Day :- 3 functions 
# def function_name(parameter bhi keh sakte or arrguments bhi keh sakte hai )

"""
1) value inserting ----> but not return out put 
2) accpting any thin (lenga kuch bhi)----> but return karega hi (kuch bhi...)
3) no input no return (lega bhi nahi kuch or return bhi nahi karega kuch) 

directory change karni hai (c:\users\hp>  cd d:),(c:\users\hp> dir)

"""
print("hello world") # function it self define by python ( is ko predefine function bhi kehte hai )
myList1 =[1,2,3,4,5]
len(myList1)
#--------------#------------#----------------# 
from math import sqrt #(inbuild hai [python me squar root])
print(sqrt(5))
 
#--------------#------------#----------------# 
from copy import deepcopy
mycopyList = deepcopy(myList1)
 
print(mycopyList) 
 
#--------------#------------#----------------# 
 
"""
in python (None) means nothing,void, blank speace (kai nahi)
flase --> 0(zero) or None consdare hoga means ke woh False huva 
for Example  :-
if None : esa hoga to woh condtion ko false consider karna
""" 
#--------------#------------#----------------#  
 
temp = "bhdchvydsvbsdb"
mylist = temp.split("ds") 

print(mylist)
#--------------#------------#----------------#  
def sum3(a,b,c):
    print(f"value of is {a}\nvalue of b is {b}\nvalue of c is {c}")
    print(a+b+c)
    
sum3(10,20,30)

sum3(b=10,a=20,c=30)    
 
# 51 min baaki 
 
 
 
 
 

#--------------#------------#----------------#  
 
# Scope Local variable(), Global variable()



# x = 50 # global variable

# def my_function():
#     print(x)
    
    
# my_function()
# print(x)               
           
           
# Local variable ()

           

