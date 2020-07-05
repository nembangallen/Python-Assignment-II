"""
7. Create a list of tuples of first name, last name, and age for your
friends and colleagues. If you don't know the age, put in None.
Calculate the average age, skipping over any None values. Print out
each name, followed by old or young if they are above or below the
average age.
"""

my_list = [('Puskar', 'Dhungana', 23), ('Anil', 'Poudel', None),
           ('Ram', 'Limbu', 23), ('Shyam', 'Rai', 21), ('Madan', 'Bhatta', None)]
sum_val = 0
num = 0
for item in my_list:
    if (item[2] != None):
        sum_val += item[2]
        num += 1
avg = sum_val/num
print(avg)
for item in my_list:
    if (item[2] != None):
        if item[2] > avg:
            print(str(item[0]) + ' is old')
        else:
            print(str(item[0]) + ' is young')
