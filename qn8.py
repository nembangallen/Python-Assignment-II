""""
8. Write a function, is_prime, that takes an integer and returns True if
the number is prime and False if the number is not prime.
"""


def is_prime(num):
    flag = False
    if num < 1:
        return flag
    for i in range(2, num):
        if (num % i) == 0:
            break
        else:
            flag = True
    return flag


print(is_prime(3))
