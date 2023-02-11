list= ["D","D","E","F","G","A","A","B","C","D","D","E","F","G","A"]
tupple= ("D","D","E","F","G","A","A","B","C","D","D","E","F","G","A")
sett={"P","Q","R","R","S","Q","T","T","U","V","W","X","Y","Y","Y","Z"}

x=list

x.append("M") #append means allows one operatiopn to add at last
x.insert(4,"KK") # inserts in list by index-position where to insert
x.reverse()
x.remove("E") # removes the attributes given
x.pop(PPPP)
x2=len(x)
y=tupple
z=sett

print(x)  #allow duplicates,fixed sort order based on system,changable operation can do
print(x2) #gives the length of list
print(y)  #allow duplicates,fixed sort order based on system,changable operation cant be done
print(z)  #doesnt allow duplicates,autosorts based on system,changable operation can do