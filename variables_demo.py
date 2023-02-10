x=12
y=24
z=50


def task2():
    global y
    y="hello"
task2()

def task3():
    global z
    z="bye"
    task3() #if task3() doesnt have space before global will effects since def func works

# def task1():
#     global x
#     x="wait"
#   task1    #indentation error will come

print(y)
print(z)
print(x)
