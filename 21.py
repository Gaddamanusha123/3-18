# Task1 Take a list of dictionary{Name: ,age: ,citize: } check whether that person is eligible for vote or not and also check the citizen.if both conditions are True add { eligible: True}

people = [
    {"Name": "Anusha", "age": 20, "citizen": "Yes"},
    {"Name": "Ravi", "age": 17, "citizen": "Yes"},
    {"Name": "Kiran", "age": 25, "citizen": "No"},
    {"Name": "Meena", "age": 30, "citizen": "Yes"}
]

for person in people:
    if person["age"] >= 18 and person["citizen"] == "Yes":
        person["eligible"] = True
    else:
        person["eligible"] = False

print("Updated list with eligibility:")
for p in people:
    print(p)



# Task2: Take a tuple of elements, print the unique elements in the new list
data = (1, 2, 3, 2, 4, 1, 5, 6, 3)
unique_elements = list(set(data))

print("Unique elements:", unique_elements)
