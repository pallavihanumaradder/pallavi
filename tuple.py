#tuples
tuple1=('f','e',('j','k'))
tuple2=('g','e',)
tuple3=tuple1+tuple2
print(tuple3)
print(tuple3*3)
print('f' in tuple2)
print(tuple3.count('e'))
print(len(tuple3))
print(tuple3.index('e'))
#sets:collection of unique elements in a unordered or unindexed.Does not allow duplications and can perform union,intersection and difference.

set1={4,6,4,3,8,5,3,4}
set2={2,8,5,3,9,0}
print(type(set1))
print(set1 | set2) #union
union_set=set1.union(set2)
print(union_set)
print(set1 & set2) #intersection
intersection_set=set1.intersection(set2)
print(intersection_set)
print(set1  - set2) #difference
difference_set=set1.difference(set2)
print(difference_set)
print(set1^set2)