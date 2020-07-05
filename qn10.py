"""
10. Write a function that takes camel-cased strings (i.e.
ThisIsCamelCased), and converts them to snake case (i.e.
this_is_camel_cased). Modify the function by adding an argument,
separator, so it will also convert to the kebab case
(i.e.this-is-camel-case) as well.
"""


def convert_to_snake_case(string):
    res = [string[0].lower()]
    for char in string[1:]:
        if char in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            res.append('_')
            res.append(char.lower())
        else:
            res.append(char)
    return ''.join(res)


def convert_to_kebab_case(string, separator):
    return ''.join([separator + x.lower() if x.isupper() else x for x in string]).lstrip(separator)


string = 'ThisIsCamelCased'
print(convert_to_snake_case(string))
print(convert_to_kebab_case(string, '-'))
