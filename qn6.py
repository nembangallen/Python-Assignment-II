def check_john(name_list):
    flag = False
    for item in name_list:
        if item == 'John':
            flag = True
            break
        else:
            pass
    return flag


name_list = ['Anil', 'Prajwol', 'Puskar', 'Hari', 'Ram']
if (check_john(name_list)):
    print('Found')
else:
    print('not found')
