#Data Types - set, frozenset, list, tuple, dict

#set - { } - Ordered, Mutable, Unique

set1 = {1,2,3,4,5}
print(set1)
print(type(set1))

#METHODS.................
#ADD  - adding element in set
print('--------------------------------------------')


set1 = {1,2,3,4,5}
set1.add(10)
print(set1)
set1.add('ram')
print(set1)

#removing elements in set
#remove()  -  to remove particular item.
print('--------------------------------------------')



set1.remove(10)
print(set1)

print('--------------------------------------------')
#POP() - to delete any element

set1={1, 2, 3, 4, 5, 'ram'}
set1.pop()
print(set1)

set1.pop()
print(set1)

print('--------------------------------------------')
#CLEAR() - to clear all elements,but set remains empty

set1 = {3, 4, 5, 'ram'}
set1.clear()
print(set1)

print('--------------------------------------------')
#UNION

a = {1,2,3,4,5}
b = {4,5,6,7}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

a = {1,2,3,4}
b = {3,4}
print(b.issubset(a))
print(b.issuperset(a))

print('--------------------------------------------')
#Update - to join 2 sets

i={1,2,3,4}
j={3,4,5,6}
i.update(j)
print(i)
j.update(i)
print(j)
print(i)

print('--------------------------------------------')
#Copy - to copy data of another variable

a = {1,2,3,4,5}
b = a.copy()
print(b)
b.add(6)
print(a)
print(b)
a.add('ram')
b = a.copy()
print(b)

print('--------------------------------------------')
#FROZEN set - frozen([]) - Unordered, Immutable, Unique

ff = frozenset([1,2,3,4])
print(ff)
print(type(ff))

f2 = {frozenset([1,2,3]),frozenset([4,5,6])}
print(f2)

print('--------------------------------------------')
#Methods
#Only able to union and copy because it is Immutable

#Copy

fs1 = frozenset([1,2,3])
fs2 = fs1.copy()
print(fs2)

print('--------------------------------------------')
#Union

fs1 = frozenset([1,2,3])
fs2 = frozenset([4,5,6])
print(fs1.union(fs2))

fs1 = frozenset([1,2,3])
fs2 = frozenset([2,3])
print(fs1.intersection(fs2))
print(fs2.issubset(fs1))
print(fs1.issuperset(fs2))
print(fs2.issuperset(fs1))

print('--------------------------------------------')
#List - [] - Ordered, Mutable, Allows duplicates, Indexable

list1 = ['apple','banana','carrot']
print(list1)
print(type(list1))

print('--------------------------------------------')
#Methods
#we can elements in 2 ways - append, insert

#Append. - used to add an element, basically its add at end of the list

num = [1,2,3,4,5]
num.append(6)
print(num)

print('--------------------------------------------')
#Insert - (index,value) - we can insert any place using index value

list1 = [1,2,3,4]
list1.insert(4,5)
print(list1)
list1.insert(0,'kumar')
print(list1)

print('--------------------------------------------')
#Extend - To join 2 lists

list1 = [1,2,3]
list2 = [4,5,6]
list1.extend(list2)
print(list1)

print('--------------------------------------------')
#pop - to delete specific position value

list1 = [1,2,3,4,5]
list1.pop(1)
print(list1)

print('--------------------------------------------')
#remove - to delete an element

list1 = [1,2,3,4,5]
list1.remove(5)
print(list1)

print('--------------------------------------------')
#clear - to remove all elements

list1.clear()
print(list1)


print('--------------------------------------------')
#Count - to a element how many times repeated/ the count of a specific item

list1 = [1,2,3,2,1,5,6,2]
a=list1.count(2)
print(a)
print(list1.count(1))


print('--------------------------------------------')
#Reverse
list1 = [1,2,3,4]
list1.reverse()
print(list1)


print('--------------------------------------------')
#Tuple - () - Ordered, Immutable, Allows duplicates

tuple1 = (1,2,3,4,5)
print(tuple1)
print(type(tuple1))


print('--------------------------------------------')
#methods - Is Immutable - so we cant modify

#Count

tuple1 = (1,3,2,3,4,3,5)
print(tuple1.count(3))


print('--------------------------------------------')
#Index

tuple1 = (1,1,2,4,3)
print(tuple1.index(3))


print('--------------------------------------------')
#DICT {'key':"value"}

student = {'name':'praneeth','age':25,'grade':'A'}
print(student)
print(type(student))

print(student.keys())
print(student.values())
print(student.items())

student2 = student.copy()
print(student2)

print(student2.pop('age'))
print(student2)
print(student2.popitem())
print(student2)
print(student2.clear())
print(student2)