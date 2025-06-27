#5. Dictionary - key:Value ,Ordered,Mutable,not allowed duplicates
from operator import index

student = {
    'ID': 2,
    'name':'praneeth',
    'age':25,
    'score':200
}

print(student)
print(type(student))

'''
........................................
#Methods
........................................
'''

#1. ADD - adding a key pair

student['class']=10
print(student)

#2. Update - to add multiple keys

student.update({'section':'b','school':'HighSchool'})
print(student)

#3.get/access dict values:

print(student['class'])
print(student.get('name'))

#4.Pop()

dict1 = {
    'a':1,
    'b':2,
    'c':3,
    'd':4,
}
value = dict1.pop('c')
print(value)
print(dict1)


print('-----------------------------------------')
#5. popitem() - it removes last inserted key-value

dict1 = {
    'a':1,
    'b':2,
    'c':3,
    'd':4,
}
value = dict1.popitem()
print(value)
print(dict1)


print('--------------------------------------------')
#6. Clear() - it delete all the data in dict

dict1 = {
    'a':1,
    'b':2,
    'c':3,
    'd':4,
}
dict1.clear()
print(dict1)
print(type(dict1))




print('---------------------------------------------------------')
# name=(input('enter your name:'))
# age=int(input('enter your age:'))
# if age>18:
#     print(name,'you are allow')

#sort()

listA = [4,3,6,78,83,2,5]
print(sorted(listA))

#index()
print(listA.index(5))

#set of dicts in list

product1 = {
    'ID':232323,
    'name':"iphone",
    'price':50000
}
product2 = {
    'ID':556323,
    'name':"TV",
    'price':100000
}
product3 = {
    'ID':344323,
    'name':"Laptop",
    'price':880000
}
product4 = {
    'ID':112323,
    'name':"Car",
    'price':9990000
}

listOfProducts = []

listOfProducts.append(product1)
listOfProducts.append(product2)
listOfProducts.append(product3)
listOfProducts.append(product4)
print(listOfProducts)

#Student


listOfStudents = []

student1 = {
    'rollno':1,
    'name':'ram',
    'age':16,
    'score':500
}
student2 = {
    'rollno':2,
    'name':'raj',
    'age':14,
    'score':700
}
student3 = {
    'rollno':3,
    'name':'sekar',
    'age':13,
    'score':400
}
student4 = {
    'rollno':4,
    'name':'rakesh',
    'age':15,
    'score':900
}

listOfStudents.append(student1)
listOfStudents.append(student2)
listOfProducts.append(student3)
listOfStudents.append(student4)
print(listOfStudents)

#Order

listOfOrders = []

order1 ={
    'id':1001,
    'quantity':2,
    'cost':110000
}
order2 ={
    'id':2001,
    'quantity':12,
    'cost':230000
}
order3 ={
    'id':4001,
    'quantity':20,
    'cost':440000
}
order4 ={
    'id':5001,
    'quantity':1,
    'cost':90000
}

listOfOrders.append(order1)
listOfOrders.append(order2)
listOfOrders.append(order3)
listOfOrders.append(order4)
print(listOfOrders)

#Updating and adding the dict

order4['name']='Iphone'
print(order4)
print(listOfOrders)

order4.update({'value':2000})
print(listOfOrders)