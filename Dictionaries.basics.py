#Use dictionaries to work with key-value pairs, key unlocks value, value is data
#Empty set {"key": "value", "key": "value"...}
student = {"name": "John", "age": 25, "courses": ["Computer Science", "Math"]}
print(student)
#Prints keys and values

#Use print(var["key"]) to get the value of the key
print(student["name"])

#Use .get method to find a key and return it, if it doesn't exist it will return none
print(student.get("name"))
print(student.get("phone", "Not Found"))

#To Add more things use this:
student["phone"] = "555-555-5555"
print(student.get("phone", "Not Found"))

#Values get updated
student["name"] = "Jane"
print(student)

#Use update to replace values
student.update({"name": "Jeff", "age": 26, "phone": "444-444-4444"})
print(student)

#Use del to delete keys and associated values
del student["age"]
print(student)

#Reset
student["age"] = 26

#Use pop to take out a value and make it a variable outside the dictionary
age = student.pop("age")
print(student)
print(age)

#Finding number of keys in the dictionary is easy
print(len(student))

#To see the keys, values, and combinations of them use:
print(student.keys())
print(student.values())
print(student.items())

#To loop through keys use
for key in student:
    print(key)
#For both use:
for key, value in student.items():
    print(key, value)
