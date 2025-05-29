# # Create a list of 5 numbers and print the square of each element.
# list = [1,2,3,4,5]
# for i in list:
#     print(i*i)
    
# # Add an element to a list and then remove the same element.
# list.append(6)
# print(list)
# list.remove(6)
# print(list)

# # Even or Odd Separator
# even = []
# odd = []
# list2 = [1,2,3,4,5,6,7,8,9]
# for i in list2:
#     if (i%2 == 0):
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)


# # Given a list of integers, create two new lists: one with even numbers and one with odd numbers.

# # List Sum & Average

# list3 = [1,2,3,4,5]
# total = 0
# for i in list3:
#     total = total + i
# print(total)

# average = total/len(list3)
# print(average)

# Write a function that takes a list of numbers and returns the sum and average.

# take = int(input("enter list of numbers: "))
# total1 = 0
# while (take == "exit"):
#     list4 = [take]

# for i in list4:
#     total1 = total1 + i
# print(total1)

# average2 = total1 / len(list4)
# print(average2)

# Define a set of student full names
# student_names = {
#     "Alice Johnson",
#     "Bob Smith",
#     "Charlie Brown",
#     "Dana White",
#     "Eliot Spencer"
# }

# no = int(input("Enter the no of student:"))
# student_names={}
# for i in range(0,no):
#     student_names = {input("Enter name:")}
# print(student_names)
# # Print the last name of each student
# print("Last names of students:")
# for full_name in student_names:
#     # Split the full name and get the last part
#     last_name = full_name.split()
#     print(last_name)


# vowels = "aeiouAEIOU"

# sentence = ("How are you?").split()
# print(sentence)

# count = 0

# for ch in sentence:
#     if ch in vowels:
#         count += 1

# print(count)



# sentence = "how are you"
# sentence_list = sentence.split()
# print(sentence_list)

# reverse_list = [ ]
# for word in sentence_list:
#     reverse_list.append(word[::-1])

# print(reverse_list)
    
    
# with open("text1.txt", "r") as f:
#     lines = f.readlines()

# with open("text2.txt", "w") as t:
#     t.writelines(lines)

# with open("text1.txt", "r") as f:
#     words = f.read().split()

# count = 0 
# for word in words:
#     count += 1
    
# print(count)

# students = {
# "101": {"name": "A", "per": 55},
# "102": {"name": "B", "per": 75},
# "103": {"name": "C", "per": 85},
# }

# above_60 = {}
# below_60 = {}

# for key, value in students.items():
#     if value["per"] >= 60:
#         above_60[key] = key
#     else:
#         below_60[key] = key

# print(above_60)