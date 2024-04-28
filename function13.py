# lambda arguments: expression= lambda is keyword
def squares(i):
    x=lambda i:i**2
    return x(i)

for i in range(1,6):
    print(f"The square of{i} is {squares(i)} ")