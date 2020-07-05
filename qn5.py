"""
5. Create a tuple with your first name, last name, and age. Create a list,
people, and append your tuple to it. Make more tuples with the
corresponding information from your friends and append them to the
list. Sort the list. When you learn about sort method, you can use the
key parameter to sort by any field in the tuple, first name, last name,
or age.
"""
# create list storing first name , last name and age
my_intro = ('Allen', 'Nembang', 22)

# create empty list
people = []
people.append(my_intro)
friend1_intro = ('Prajwol', 'Niroula', 22)
friend2_intro = ('Anil', 'Poudel', 22)
friend3_intro = ('Puskar', 'Dhungana', 22)
people.append(friend1_intro)
people.append(friend2_intro)
people.append(friend3_intro)
print('Before sorting: ')
print(people)
people.sort(key=lambda x: x[0])
print('After sorting by first name: ')
print(people)
