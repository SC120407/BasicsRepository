courses = ["History", "Math", "Physics", "Computer Science"]

# Print out the variable list
print(courses)

# Print out an item from the variable list
print(courses[1])

# Print out multiple item from the variable list (in order) (First index inclusive, last index exclusive)
print(courses[0:2])

#Implied go to end of list
print(courses[1:])

#Use negative index to go backwards in the list
print(courses[-1])

#Adds list/value to end of the string
courses.append("Art")
print(courses)

#Adds list/value into given index
courses.insert(2, "English")
print(courses)

#Adds multiple values
courses_2 = ["Chemistry", "PE"]

#See how there is more brackets: embedded lists
courses.insert(0, courses_2)
print(courses)

#The whole list is taken as the first index
print(courses[0])

#Remove to make future easier and add back as extend method in line 41
courses.remove(courses_2)

#Using extend makes the elements of the sublist become an index of the superlist (Apply to the end of the list)
courses_3 = ["Drama", "Biology"]
courses.extend(courses_2)
courses.extend(courses_3)
print(courses)

#Removes an element from the list
courses.remove("Math")
print(courses)

#Using pop method, remove final element of list
popped = courses.pop()
print(courses)
print(popped)

#Use reverse method to reverse the list
courses.reverse()
print(courses)

#Use sort to sort by alphabetical order
courses.sort()
print(courses)

#Sort makes numbers in ascencding values
nums = [5, 3, 1, 4, 2]
nums.sort()
print(nums)

#To sort values in descending order, instead of making new line to reverse, use reverse method in brackets
nums.sort(reverse=True)
print(nums)

#To apply a function on a list without changing the list itself, use the functions
#Rewrite variables to reset
nums = [5, 3, 1, 4, 2]
courses = ['Art', 'English', 'Computer Science', 'Physics', 'History', 'Chemistry', 'Drama', 'PE']

#The sorted function doesn't change the print of the output, use variables to strore values
courses_sort = sorted(courses)
nums_sort = sorted(nums)
print(courses)
print(nums)
print(courses_sort)
print(nums_sort)

#Use min, max, and sum methods for lists of numbers
print(min(nums))
print(max(nums))
print(sum(nums))

#To find the index of a value
print(courses.index("Drama"))

#To return a T/F statement for a value in the list
print("Biology" in courses)
print("Physics" in courses)

#Using loops to print out items
for item in courses:
    print(item)

#Using loops to print out index number and value
for index, course in enumerate(courses, start = 1):
    print(index, course)

#Use join function to turn a list into a string
courses_str = ", ".join(courses)
print(courses_str)

#Use split function to turn a string into a list
new_list = courses_str.split(", ")
print(new_list)

#Lists are mutable objects so if list_1 = list_2, both change with respect to list_1
#Tuples are immutable, they use parantheses instead of square brackets, you can't change an item in a tuple after it is defined
#Sets are mutable, they use curly brackets instead of square brackets, there contents come out jumbled, Sets remove duplicates and are optimized for finding values

cs_courses = {"Math", "History", "Physics", "Computer Science"}
art_courses = {"Math", "History", "Art", "Design"}

#Use intersection to find common elements in the sets
print(cs_courses.intersection(art_courses))

#Use difference for uncommon elements in the sets (Doesn't list all, just ones from the main set)
print(cs_courses.difference(art_courses))

#Use union for all courses in two sets
print(cs_courses.union(art_courses))

#For them use an empty class list(), tuple(), set() set to a variable
