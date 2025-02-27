my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "job": "Engineer"
}

key = input("Enter the key to search: ")

if key in my_dict:
    print("Key found! The value is: " + str(my_dict[key]))
else:
    print("Key not found!")
