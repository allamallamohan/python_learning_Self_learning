for x in range(1,50):
    if (x==25):
        print("-----> X=25 Triggered <------")
        break  ##  Breaks the operation at a point where if condition satisfied
    print(x)

for y in range(100,150):
    if (y==125):
        print("-----> X=125 Triggered <------")
        continue ## Operation break at a point where if condition satisfied and continued
    print(y)

print(x,y) ## Here x,y stores the last dynamic value x breaks at 25 and y continue at 149 range last value
