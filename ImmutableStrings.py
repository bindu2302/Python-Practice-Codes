'''
1. String are immutable : once we declare the string we cannot modify it
if we try to modify the string it will create new string.

2. If new string does not have any reference variable then it will be removed

3. Python internally uses String Interning

4. String interning is the process of Checking string intern pool
before creating any new object.

whenever we want to create new object, python first
will check string intern pool, whether that object already exists or not.

when the object already exists in the string intern
records then address of the existing object will be reused.'''


# s1 = 'Kodnest'
# s1=s1.upper()
# print(s1)


# s1 = 'K'
# print(s1,id(s1))


s1 = 'Hello'
s2 = 'World'
print(s1,id(s1))
print(s2,id(s2))

print(s1[0]) #H
print(s1[-1]) #o

print("s1 Id of H:",id(s1[0]))
print('s2 Id of w:',id(s2[0]))

print(" s1 Id of o:",id(s1[-1]))
print('s2 Id of o:',id(s2[1]))

print(" s1 Id of l:",id(s1[2])) 
print("s2 Id of l:",id(s1[3])) 

print(" s1 Id of l:",id(s1[2])) 
print("s1 Id of l:",id(s1[3])) 
print("s2 Id of l:",id(s2[3])) 

