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
print(set1^set2) #symmitric defference
#add(element) — Add an element to the set
#remove(element) — Remove an element (raises error if not present)
#discard(element) — Remove an element if it exists
#issubset(other_set) — Check if the set is a subset of another
#issuperset(other_set) — Check if the set is a superset of another
#copy() — Create a shallow copy of the set
#clear() — Remove all 