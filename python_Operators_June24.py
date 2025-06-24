#Arthematic Operators
# +

a = 2
b = 3
print("Output for a+b is :",a+b)
print("Output for a-b is :",a-b)
print("Output for a*b is :",a*b)
print("Output for a/b is :",a/b)
print("Output for a//b is :",a//b)
print("Output for a%b is :",a%b)
print("Output for a**b is :",a**b)


print('-------------')

#Assignment Operators

i=5

print(i)

i+=3
print(i)

i=5
i-=3
print(i)

i=5
i*=2
print(i)

i=5
i/=2
print(i)

i=5
i//=2
print(i)

i=5
i%=2
print(i)

i=5
i**=2
print(i)

#Comparison Operators
print('-------------------')

x=9
y=9

print(x==y)

x=4
y=7
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

#Logical Operators
print('-----------------')

a=1
b=2
print(a==b and a<=b)
print(a==b or a<=b)
print(not(a==b))

a=4
b=4
print(a==b and a>=b)
print(a>b or a<=b)
print(not(a==b))

#Bitwise Operator
print('--------------')

a = 12
b = 10

print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a<<1)
print(a>>1)


#Membership Operators
print('----------------')

print('n' in 'banana')
print('n' not in 'banana')
print('m' not in 'banana')

fruits = ['apple','mango','kiwi','orange']
print('kiwi' in fruits)
print('Guvva' not in fruits)

num = {1,2,3,4,5}
print(5 in num)
print(10 not in num)


#Identity Operators
print('----------------------')

a=5
b=a

print(a is b)
print(b is a)
print(a is not b)