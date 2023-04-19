import unittest

def fibonacci_iterative(n):
    assert n > 0
    secondLast = 0
    Last = 1
    if n == 1:
        print(secondLast)
    elif n == 2:
        print(Last)
    else:
        for i in range(3, n + 1):
            result = secondLast + Last
            secondLast = Last
            Last = result
        print(result)


#fibonacci_iterative(8)
#fibonacci_iterative(7)
#fibonacci_iterative(4)



def fibonacci_recursive(n):
    assert n > 0
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
#print(fibonacci_recursive(8))
#print(fibonacci_recursive(7))
#print(fibonacci_recursive(4))

