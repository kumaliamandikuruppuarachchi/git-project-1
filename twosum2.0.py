x=[25,10,15,8]
target=int(input("Enter the target: "))
for i in x:
    for y in x:
        if target-i==y:
            print(i,y)
            exit()
