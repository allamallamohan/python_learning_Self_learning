biodata={

"name":"Mohan",
"age":28,
"graph":2e+6,
"percentage":94.80,
"scores":[86.66,94.80,75.49]

}

print(biodata)
print(type(biodata))
print(len(biodata))

for x in biodata:
    print(x)
for y in biodata:
    print(y)
for x,y in biodata.items():   # to use key(x) and value(y) need to def dict as items
    print(x+" --->  "+str(y)) #key always string and value may be any type