import csv
# READER & WRITER
# accessing content of csv file
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader) # it will skip first line -  ['first_name', 'last_name', 'email']
    for line in csv_reader:
        print(line)


# writing content to new file
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_names.csv','w', newline='') as new_file:  # newline argument to avoid creating blank lines
        csv_writer = csv.writer(new_file, delimiter='\t') # by default, delimeter is ','

        for line in csv_reader:
            csv_writer.writerow(line)

# if we are passing delimeter other than ',', need to paas in while reading the csv file
with open('new_names.csv', 'r') as new_file:
    csv_reader = csv.reader(new_file, delimiter='\t')
    for line in csv_reader:
        print(line)

# DICTReader
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        print(line)  # {'first_name': 'John', 'last_name': 'Doe', 'email': 'john-doe@bogusemail.com'}
        print(line['email'])  #  john-doe@bogusemail.com

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    with open('new_names.csv', 'w', newline='') as new_file:
        field_names = ['first_name', 'last_name']  # removed 'email' column
        csv_writer = csv.DictWriter(new_file, fieldnames=field_names, delimiter='\t')
        csv_writer.writeheader()  # writing field names at the start.

        for line in csv_reader:
            del line['email'] # removed 'email' column
            csv_writer.writerow(line)
