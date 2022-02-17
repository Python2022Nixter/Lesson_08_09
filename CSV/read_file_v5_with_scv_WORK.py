import csv
from itertools import count
import os
import pathlib
import platform

keys = []
count_searched = 0

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    pass


clear_screen()

# https://www.mockaroo.com
FILE_NAME = "MOCK_DATA.csv"
path_to_file = pathlib.Path(__file__).parent.joinpath(FILE_NAME)

# get keys for the scv file
with open(path_to_file, newline="") as file:
    keys = next(csv.reader(file))
    pass


# print function

def print_customer(customer):
    print(f"""
name: {customer[keys[1]]}
last name: {customer[keys[2]]}
email: {customer[keys[3]]}
country: {customer[keys[4]]}
ip address: {customer[keys[5]]}    
          
          """)


# search by key (input from user)
print("search by key:")
l1 = range(1, len(keys))
d1 = dict(zip(l1, keys))
for i in d1:
    print(f"{i} - {d1[i]}")
    pass


key = int(input("input key: "))
key = d1[key]
print(f"key: {key}")


# read file to list of dictionaries
customers_list = []
with open(path_to_file, newline="") as file:
    scv_reader = csv.DictReader(file, delimiter=",")
    for row in scv_reader:
        customers_list.append(row)
        pass
    pass

clear_screen()
text = input(f"search by {key}: ")

# print all finded customers

for customer in customers_list:
    if text in customer[key]:
        count_searched += 1
        print_customer(customer)
    pass

print(f"total found: {count_searched} customers\n")