
# # SOME BASIC OF PYTHON LANGUAGE
# # message = 'welcome to python crash course'
# # print(message)

# # console = 'this is my class and i am here to learn some stuff'
# # print(console.title())

# # name = "'abdifatah '"
# # print(name)
# # name.rstrip()
# # print(name)

# # print(4+4)

# # squere = 4**3

# # print(squere)

# # age = 23
# # message = "Happy " + str(age) + "rd Birthday!"
# # print(message

# Lists and how they work

# lists example
students = ['abdi', 'ali', 'xamse', 'mukhtar', 'saynab']

# accessing individual elements

# replace or add value to the list
students[0] = 'hasan'

# appending an elements
students.append('faarax')

# inserting element in list
students.insert(0, 'yusuf')

# removing elements in list using del statement
del students[0]

# removing elemets using pop method
popped = students.pop()

# removing of item value
students.remove('xamse')

# sorting lists
students.sort()
students.sort(reverse = True)

# sorting list using sorted() function
# print(sorted(students))

# printing list in reverse order
print(students)
students.reverse()
print(students)
print(len(students))
print(students[1])