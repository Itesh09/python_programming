# function to print the factorical of number (n is parameter)
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

factorial(4)