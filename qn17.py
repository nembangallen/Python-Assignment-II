"""
17. Write a program that serves as a basic calculator. It asks for two
numbers, then it asks for an operator. Gracefully deal with input that
doesn't cleanly convert to numbers. Deal with division by zero errors.
"""


def sum_nums(num1, num2):
    print('Sum is: '+str(num1 + num2))


def diff_nums(num1, num2):
    print('Subtraction is: '+str(num1 - num2))


def product_nums(num1, num2):
    print('Product is: '+str(num1 * num2))


def div_nums(num1, num2):
    if num2 == 0:
        print('Indeteminant Form: Cannot divide by zero')
    else:
        print('Division is: '+str(num1/num2))


num1 = int(input('Enter first number:'))
num2 = int(input('Enter second number:'))
choose_op = input('Choose operators: +,-,/,*')

if (choose_op == '+'):
    sum_nums(num1, num2)
elif (choose_op == '-'):
    diff_nums(num1, num2)
elif (choose_op == '*'):
    product_nums(num1, num2)
elif (choose_op == '/'):
    div_nums(num1, num2)
else:
    pass
