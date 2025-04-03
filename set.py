a=[13,15,6,13,6,9,9]
a=set(a)
print(a)
b={6,9,20,18}
#c=set([])
#print(b,c)

#operations on sets
#union= a+b |
print(a.union(b))
print(a|b)
 
#intersection= a & b
print(a.intersection(b))
print(a & b)

#symetric difference ^ union-intersection
print(a.symmetric_difference(b))
print(a^b)

#difference of sets a-b, b-a
print(a.difference(b))
print(a-b)
print(b.difference(a))
print(b-a)