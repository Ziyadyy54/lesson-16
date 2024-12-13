def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
print(factorial.__doc__)
print("factoial of 0 is",factorial(0))
print("factoial of 1 is",factorial(1))
print("factoial of 5 is",factorial(5))
print("factoial of 9 is",factorial(9))
print("factoial of 49 is",factorial(49))