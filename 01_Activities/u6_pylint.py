


# CODE SOURCE: SOFTWARE ARCHITECTURE WITH PYTHON
#
# def factorial(n):
# """ Return factorial of n """
# if n == 0:
# return 1
# else:
# return n*factorial(n-1)



def factorial(n):
    """ Return factorial of n """
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))