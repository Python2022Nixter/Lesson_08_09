from array import array
import os
import pathlib

os.system('clear')

FILE_NAME = "MOCK_DATA.csv"
path_to_file = pathlib.Path(__file__).parent.joinpath(FILE_NAME)
customers_list = []

with open(path_to_file, "r") as file:
    customers_list = file.readlines()
    #print(customers_list, type(customers_list), len(customers_list))
    pass


customers_list1 = []
for person in customers_list:
    customers_list1.append(person.split(","))
    pass


male_counter = 0
female_counter = 0
other_counter = 0


for customer in customers_list1:
    if customer[4] == "Male":
        male_counter += 1
    elif customer[4] == "Female":
        female_counter += 1
    else:
        other_counter += 1
    pass


print(f"Males = {male_counter}, Females = {female_counter}, Others = {other_counter}")

# Create dictionary 

customers_dictionary = {}
for i in range(1, len(customers_list)):
    # add next record
    key = customers_list[i].split(",")[1] + "__" + customers_list[i].split(",")[2]
    value = customers_list[i].split(",")
    customers_dictionary[key] = value
    pass

print(customers_dictionary["Shalom__Medmore"], type(customers_dictionary), len(customers_dictionary))
