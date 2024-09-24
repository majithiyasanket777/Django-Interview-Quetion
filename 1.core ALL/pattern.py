# pattern

# num =6
# for row in range (1,num):
#     for col in range (1,num):
#         print("*",end=' ')
#     print()    



# num = 10
# for row in range (1,num):
#     for col in range (1,row+1):
#         print("*",end=' ')
#     print()    



# num = 6

# for row in range (1,10):
#     for col in range (1,row+1):
#         print(col,end=' ')
#     print()    




# num =6
# for row in range (1,6):
#     for col in range (1,row+1):
#         print(chr(col+64),end=' ')
#     print()    




# num =6
# for row in range (1,6):
#     for col in range (1,row+1):
#         print(chr(col+96),end=' ')
#     print()    


# num =6
# for row in range (1,6):
#     for col in range (1,row):
#         print(' ',end=' ')
#     print(chr(row+96),end='')
#     print()    




# num = 6
# for row in range (1,6):
#     for col in range (1,row):
#         print(' ',end=' ')
#     print(chr(row+96),end=' ')
#     print()    



# list_name = [1,'hghfyh', 67.09, 2, 4]
# print((list_name)) 

# m_items = ['milk', 'butter-milk', 'potato']
# n_items = ['milk', 'tomato']
# a_items = ['drink', 'chocolate']

# total_items = m_items + n_items + a_items
# print(total_items[-2])


# total_items=['milk', 'butter-milk', 'potato', 'milk', 'tomato', 'drink', 'chocolate']
# print(total_items[0:3])
# print(total_items[3:5])
# print(total_items[-2::-2])



"""list :- list is ,orderd,mutebal ,indexing , silicing, duplicate value are allowed. you can add value , remove , change
list is data sturcture that used to collection of items 
"""






# """list -  ordered, mutable, indexing, slicing, duplicate values are  allowed.
#    set - unoreder, unindexing,duplicate value are not allow,(mutable) .
#    frozen set- inmutable
#   tuple - ordered, immutable, indexing, slicing, duplicate values are allowed .  """"


# list- (in python list are data structure that used to collection of items ) -orderd,indexing,silicing , duplicate value are allowed,mutable
# set - unorderd,unindexing,dupalicate value are not allowed. mutable
# tuple- orderd, immutable,indexing,slicing, duplicate value are allowed


"""
* 
* *
* * *
* * * *

# """  
  
# for i in range (1,5):
#     for j in range(1,5):
#         if j<=i:
#            print("* ",end="")
#     print()    

"""
    *
   **
  ***
 ****
*****      
 
# """
# for i in range(1,5):
#     for j in range(1,5):
#         if j>=5-i:
#             print("*",end="")
#         else:    
#             print(" ",end="")
#     print()   


"""
****
***
**
*

# """
# for i in range(1,5):
#     for j in range(1,5):
#         if j<=5-i:
#             print("*",end="")
#         else:    
#             print("",end="")
#     print()        
"""
****
 ***
  **
   *



"""

# for i in range(1,5):
#     for j in range(1,5):
#         if j>=i:
#             print("*",end="")
#         else:
#             print(" ", end="")    
#     print()    
    
    

"""
   *   
  ***
 *****
*******

"""    
for i in range(1,5):
    for j in range(1,8):
        if j>=5-i and j<=3+i:
            print("*",end='')
        else:
            print(" ",end='')
    print()         

"""
   *******
    *****
     ***
      *  

    """
for i in range(1,5):
    for j in range(1,8):
        if j>=i and j<=8-i:
            print("*",end="")
        else:
            print(" ",end="")
    print()            
            
"""
   *   
  ***
 *****
*******
*******
 *****
  ***
   *

   

"""                  
            
for i in range(1,5):
    for j in range(1,8):
        if j>=5-i and j<=3+i:
            print("*",end='')
        else:
            print(" ",end='')
    print()         
for i in range(1,5):
    for j in range(1,8):
        if j>=i and j<=8-i:
            print("*",end="")
        else:
            print(" ",end="")
    print()             
























# dict:- mutable ,unorderd, unindexing,dupalicate value are not allowed .

# syntax :- 
# dict_name= {
#   'key1':'value1',
#   'key2':'value2'
  
#    }
# dict_name = dict

# store = {
#      'vegis':{
#        'tomato':{
#          'price-p/kg':30,
#           'qty':'20k'
#        },
#        'potato':{
#          'price-p/kg':20,
#          'qty':'100k'
#        }
         
#     },
#      'fruites':{
#        'apple':{
#          'price-p/kg':100,
#          'qty':'50k'
         
#       },
       
#        'banana':{
#             'price-p/dozen':24,
#             'qty':'30dozen'
#         }
#     }
# }

# print(dict(store))
# print(dict(store))

# print(store['vegis'])
# print(store ['fruites'])
# print(store.keys())
# print(store.values())     
# print(store.items())
# print(store.get('vegis'))
#  del store['vegis']
# store.pop('vegis')



# 'from keys '
# book_list = ['java','python','php']
# price=20
# books=dict()
# print(books.fromkeys(book_list,price))
# books.fromkeys(book_list, price)
# print(books)


# car = {
#     'color':'black',
#     'name':"BMW"
# }

# car.setdefault('model', "sghdjh@##d")
# car.setdefault('color', "red")
# print(car)

"""
dict - mutable, unindexing ,unorderd,dupalicate value are not allowed .

syntax-
dict_name = {
  'key1':'value1',
  'key2':'value2'
}
dict_name = dict()

method :- print(len(store))
          print(type(store))
          print(dict(store))
          
          clear , copy 
          add :- get,keys, items , values, 
          keys :- fruites , veggis
          value :- pottato ,apple , bananna etc
          
          updating :- new member adding exitsitng member all redy there 
          
      
          
          print(pop('vegis'))
          print(popitems())
          print (del(store))


dictonary are mutable , unorderd, unindexing , dupalicate value are not allowed

in python dictonary that is built in data that store key in pairs , in dictonary are mutable that change the value after creating . 




What does iterate mean in Python?
Repetitive execution of the same block of code over and over is


Iterable is an object which can be looped over or iterated over with the help of a for loop. 
Objects like lists, tuples, sets, dictionaries, strings, etc. are called iterables.
"""


# store['drinks'] = 'coco'
# store.update({
#     'new-fruites':{
#         'guava':{
#             'qty':'20k'
#         }
#     }
# })
# print(store)


# adding method :- get,value, keyes, items,
# updating :- 
# modiflying :-
# clear, pop
# frome keys,
# setdefault

"""""
what is function :- in python function is reuseable code that perfoemce specific task .function allow to you organize to your code it  block of easilyer to read  code , maintain , understand
function using defind def keywords follow by () paranteses :coma 
  syntax :-
  def function_name(paramteres):
    fumction is resuable code that performance spcipic task code is easiyer to read , maintain , understand function using (def), () paranteses , : coma
   
  function parameters 
  1.potistional parametres
  2. default parameters
  3. keywords parameteres
  4. variyable length
  5.
  6.
  
   """ 
   
""""iterable object :- itereble is object that used repitetive exctuion  same block  of code over and over that is itreable 
objects like 
# """
# # positional para
# def fullname(fname, lname):
#     print(fname + ' ' + lname)

# fullname('sanket', 'majithiya')





