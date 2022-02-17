import imp


import csv
import os
import pathlib

os.system('clear')

# https://www.mockaroo.com
FILE_NAME = "MOCK_DATA.csv"
path_to_file = pathlib.Path(__file__).parent.joinpath(FILE_NAME)

customers = []
with open(path_to_file, newline="") as file:
    scv_reader = csv.reader(file, delimiter=",", quotechar='|')
    customers = list(scv_reader)
    # for row in scv_reader:
    #     customers.append(row)
    #     pass
    # pass

print(type(customers), len(customers))
print(customers[1])

# read file to dictionary
customers_dictionary = {}
with open(path_to_file, newline="") as file:
    scv_reader = csv.DictReader(file, delimiter=",")
    for row in scv_reader:
        customers_dictionary[row["email"]] = row
        pass
    pass

print(type(customers_dictionary), len(customers_dictionary), customers_dictionary["agrimblebyh@berkeley.edu"]["gender"])

