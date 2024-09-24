menu ={
    
    'pizza':50,
    'coffe':30,
    'salad':80,
    'pasta':70,
      
}
print("welcom to python restaurant")
print("pizza:50RS coffe:30RS salad:80RS pasta:70RS")

order_total = 0

item_1 = input("Enter the number of the item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been add to your order: ")
    
else:
    print(f"order item {item_1} is not avialble yet! ")
    
another_order = input("Do you want add another iteme?(yes/No)")
if another_order == 'yes':
    item_2 = input("Enter the name of second item = ")  
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item{item_2} has been added to order")
    else:
        print(f"item {item_2} is not avialble yet!")
        
print(f"The total amount of items to pay is {order_total}")        
    




# alphabet = ['a','b','c','d','e']
# alphabet[1:3] = "code"
# print(alphabet)






# 1 ANS :- None  

# numbers = [1,2,3].append(4)
# print(numbers)
# # 2 ANS :- c
# name = "TOPS technology pvt.ltd."
# address = "Ring Road, Surat(395002)"
# print("company name:{1}and address is{2}.format(name,address)")

# 3 Ans:- A     its initialize the class variyables.

# 4 Ans:-  D     range returns an iterable objects,not a list

# 5 Ans:- B      False

# 6 Ans:- D      5

# 7 Ans:- B     it is a placeholder that does nothing

# 8 Ans:- C     'qkof'

# 9 Ans:-
# alphabet = ['a','b','c','d','e']
# alphabet[1:3] = "code"
# print(alphabet)

#ANS:- ['a', 'c', 'o', 'd', 'e', 'd', 'e']


# 10 Ans:- B

# def outer_function(x):
#     def inner_function(y):
#         return x * y
#     return inner_function
# result = outer_function(3)(4)
# print(result)




# a = [1,2,3]
# b = a 
# b[0] = 5
# print(a[0]) # 5




