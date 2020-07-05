"""
9. Write a binary search function. It should take a sorted sequence and
the item it is looking for. It should return the index of the item if found.
It should return -1 if the item is not found.
"""


def binary_search(seq_list, l, r, num):
    if r >= 1:
        mid = l + (r-1) // 2

        if seq_list[mid] == num:
            return mid

        elif seq_list[mid] > num:
            return binary_search(seq_list, l, mid-1, num)

        else:
            return binary_search(seq_list, mid+1, r, num)
    else:
        return -1


seq_list = [5, 7, 9, 10, 14, 17, 20]
num = 7
result = binary_search(seq_list, 0, len(seq_list)-1, num)
if result != -1:
    print('Element is present at index: ' + str(result))
else:
    print(result)
