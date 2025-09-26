#loop in lists
l=[3.4,54.65,3.4,6.7,4.4,3.2,2.98]
l2=[]
total=0
for num in l:
    l2.append(num*num)
    '''total=total+num
    print(total)
l2=2*(l)'''
print(l2)

#loops in dictionaries
rainbow={
    "v":"voilet",
    "o":"orange",
    "g":"green",
    "b":"blue"
}
for chars in rainbow.items():
    print(chars)
r=sorted(rainbow)
print(r)
r=max(rainbow)
print(r)
r=min(rainbow)
print(r)
print(type(rainbow))