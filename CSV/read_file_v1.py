from array import array
import os
import pathlib

os.system('clear')

FILE_NAME = "MOCK_DATA.csv"
path_to_file = pathlib.Path(__file__).parent.joinpath(FILE_NAME)
list_from_file = []
with open(path_to_file, "r") as file:
    list_from_file = file.readlines()
    #print(list_from_file, type(list_from_file), len(list_from_file))
    pass

# count  Male, Female, Bigender, Agender, Polygender

Male = 0
Female = 0
Bigender = 0
Agender = 0
Polygender = 0
for person in list_from_file:
    d = person.split(",")
    if d[4] == "Male":
        Male += 1
        pass
    if d[4] == "Female":
        Female += 1
        pass
    if d[4] == "Bigender":
        Bigender += 1
        pass
    if d[4] == "Agender":
        Agender += 1
        pass
    if d[4] == "Polygender":
        Polygender += 1
        pass
print("Male -", Male)
print("Female - ", Female)
print("Bigender - ", Bigender)
print("Agender - ", Agender)
print("Polygender - ", Polygender)
