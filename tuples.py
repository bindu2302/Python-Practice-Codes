'''
1. In Tuple we can store homogeneous as well as Hetergenous data.
2. In tuple we can store duplicates
3. Tuples are ordered collection of data
4. Tuples are Immutable: Once we declare the tuple we cannot modify it.
'''

tup1 = (10,22.55,'Kodnest',True,10)
print(tup1) #(10, 22.55, 'Kodnest', True, 10)
# tup1.append(400)
# tup1.remove(55)
# tup1.pop()
# del tup1[2]
print(tup1[2]) #'Kodnest'
del tup1 # Remove entire tuple, deletes the complete object
# print(tup1) # error


t1 = (1,2,3)
t2 = (4,5,6)
t3 = t1+t2
print(t3) # (1,2,3,4,5,6)