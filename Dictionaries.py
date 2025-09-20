#dictionaries: Collection of key-values pairs. Unordered and mutable
'''meanings={
    #key :value,
    "amma":"mother",
    "appa" :"father",
    "anna":"brother"
}
print(type(meanings))
#Accessing dictionary elements using keys;
#print(dict name[key])
print(meanings["amma"])
print(meanings.get("akka")) # Best for large codes to avoid keyerrors
# Adding and updating
meanings["akka"]="sister" #dict name[key]=value
print(meanings)
#Removing an element from the dict
meanings.pop("anna") # use of pop
del meanings["amma"] #del keyword
print(meanings)
meanings.clear() # clear
print(meanings)
'''
item1={
    "name":"ravi",
    "weight":45,
    "hight":153
}
item2={
    "name":"manu",
    "weight":42,
    "hight":149
}
item3={
    "name":"hari",
    "weight":49,
    "hight":159
}
items=[item1,item2,item3]
print(items)
print(f"total weight:{item1["weight"]+item2["weight"]+item3["weight"]}")