"""
13. Write a function to write a comma-separated value (CSV) file. It
should accept a filename and a list of tuples as parameters. The
tuples should have a name, address, and age. The file should create
a header row followed by a row for each tuple. If the following list of
tuples was passed in:
[('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
it should write the following in the file:
name,address,age
George,4312 Abbey Road,22
John,54 Love Ave,21
"""
import csv


def write_csv(file_name, intro_list):
    headers = ['name', 'address', 'age']
    with open(file_name, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)
        writer.writerows(intro_list)


file_name = 'intro.csv'
intro_list = [('Allen Nembang', 'Jhapa', 23),
              ('Anil Poudel', 'Jhapa', 23),
              ('Prajwol Niroula', 'Morang', 24)]


write_csv(file_name, intro_list)
