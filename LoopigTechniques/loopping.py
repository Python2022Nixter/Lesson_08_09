
import os


os.system('clear')

persons = {
    "John": {"age": 20, "email": "john20@gmail.com"},
    "Anna": {"age": 21, "email": "anna21@gmail.com"},
    "Peter": {"age": 22, "email": "petter22@gmail.com"},
    "Mike": {"age": 23, "email": "mike@gmail.com"},
}

print(persons)

# items()
for person in persons.items():
    print(person, type(person))
    # person[0] - string, person[1] - dictionary
    print(person[0], person[1]["email"])
    pass

# enumerate()
a1 = ["Sunday", "Monday", "Tuesday", "Wednesday",
      "Thursday", "Friday", "Saturday"]
for k, v in enumerate(a1):
    print(k, v)
    pass
for k, v in enumerate(persons):
    print(k, v, end="")
    print(persons[v]["email"])
    pass

# zip()
print("\n zip()\n")
l1 = [1, 2, 3, 4, 5]
t1 = (100, 200, 300, 400, 500)
for a, b in zip(l1, t1):
    print(a, b)
    pass

# reversed()
for i in reversed(range(0, 10, 2)):
    print(i)
    pass

# sorted()
print("\n sorted()\n")
days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"]

def sort_by_length(s):
    return len(s)
for day in sorted(set(days), key=sort_by_length):  # set() - remove duplicates
    print(day)
    pass
