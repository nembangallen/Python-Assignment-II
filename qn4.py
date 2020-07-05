"""
4. Create a list. Append the names of your colleagues and friends to it.
Has the id of the list changed? Sort the list. What is the first item on
the list? What is the second item on the list?
"""
name_list = []
first = id(name_list)
name_list.append('Prajwol')
name_list.append('Anil')
name_list.append('Ram')
name_list.append('Shyam')
last = id(name_list)
if first != last:
    print('Id of list has been changed')
else:
    print('No change in Id of the list.')
name_list.sort()
print('First Item: ' + name_list[0])
print('Second Item: ' + name_list[1])
