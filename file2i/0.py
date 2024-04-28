num=[1,2,3,4,5,6]
with open("num.txt","r") as f:
    for i in num:
        x=f.read(int(i))
        print(x)

