# a=200
# b=200
# e,f=20,40
# c=a+b
# h=e+f
# print(c,h)

# #you can assign single value to multiple value


# #pack and unpack
# c=10,20
# a,b=c
# print(a,b)

# #finding data type
# print(type(a))

# #you can also do
# a=int(100)
# b=float(12.2)
# name=str("mit")
# print(type(name))

# #typecasting
# a=int(80.50)
# d=float(a)
# b=float("20")
# print(a,b,d)


# # comparision
# a="CAT"
# b="MAT"
# ans=a<b

# print("CAT<MAT", ans)

# # logical operator (value of 0 is considered as false else all are true)
# a = 30
# b = 30
# c = a and b

# print(c)

# #  learn bitwise , membership, identity operators
# # swap 2 numbers using bitwise operator

# a = 4 << 1
# #a<<b = a * 2(power)b
# #a>>b = a / 2(power)b
# print(a)


# a=4
# b=6
# c = a&b
# print(c)

# #membership Operator
# # z = "Hello world HELLO"
# # count = 0
# # y = 'H'

# # print("Hello" in a)



# #Identity operator(it works on memory location Compares the memory location values)
# a = 10
# b = 10
# print(a is b)


# # inline if else
# a = 100
# b = 20
# c = 30
# print(a if a > b else b if b > c else c if c > a else a)

# # q1 write a program to check prime number , perfect number , armstrong number ,fibonacci series
# #  all string operations append , reverse etc
# #  basic array operations reading the alternate arrays 
# #  reverse the array, list 
# # lc gcd and pascles traingle
# # 3, 4 patters (star)

# # Fibonacci series 
# # def fibo(n):
# #     a = 0
# #     b = 1
# #     if n == 1:
# #         print(a)
# #     else:
# #         print(a)
# #         print(b)
# #         for i in range(2, n):
# #             c = a + b
# #             a = b
# #             b = c
# #             print(c)

# # fibo(10)

# # # # # Prime number
# # def is_prime(n):
# #     if n < 2:
# #         return False
# #     for i in range(2, int(n**0.5) + 1):
# #         if n % i == 0:
# #             return False
# #     return True

# # # Print prime numbers from 1 to 50
# # for num in range(1, 51):
# #     if is_prime(num):
# #         print(num, end=" ")


# # # # # Perfect number
# # n = int (input("Enter the number: "))
# # sum = 0
# # for i in range(1, n):
# #     if n % i == 0:
# #         sum += i
# # if sum == n:
# #     print("Perfect number")
# # else:
# #     print("Not a perfect number")
    
# # # # # Armstrong number
# # num = int(input("Enter the number: "))
# # length = len(str(num))
# # sum = 0
# # temp = num
# # while temp > 0:
# #     digit = temp % 10
# #     sum += digit ** length
# #     temp //= 10
# # if num == sum:
# #     print("Armstrong number")
# # else:
# #     print("Not an Armstrong number")

# # # # palindrome number
# # num = int(input("Enter the number: "))
# # temp = num
# # rev = 0
# # while num > 0:
# #     digit = num % 10
# #     rev = rev * 10 + digit
# #     num //= 10
# # if temp == rev:
# #     print("Pelindrome number")
# # else:
# #     print("Not a pelindrome number")

# # # reverse the digit of number
# # num = int(input("Enter the number: ")) 12345
# # rev = 0
# # while num > 0:
# #     digit = num % 10         5 4
# #     rev = rev * 10 + digit      5 54
# #     num //= 10                  1234 123
# # print(rev)

# # # star pattern
# # for i in range(5):
# #     for j in range(i+1):
# #         print("*", end=" ")
# #     print()

# # # # star pattern 2
# # for i in range(5):
# #     for j in range(5-i):
# #         print("*", end=" ")
# #     print()

# # # # star pattern 3
# # for i in range(5):
# #     for j in range(5-i):
# #         print(" ", end=" ")
# #     for k in range(i+1):
# #         print("*", end=" ")
# #     print()
    
# # # String operations
# # string = "Hello World"
# # print(string[::-1])  # Reverse the string
# # print(string + " " + "Python")  # Append the string

# # read function pointer

# # FUNCTIONS

# def wow():
#     print("wowowowo")

# wow()

# def wow2(a,b):
#     print(a+b)
    
# wow2(2,3)


# def sum(a,b):
#     return a+b

# add = sum(5,5)
# print(add)

# # print("Addition of {1} & {0} = {2}".format(a,b,add))


# # Pointer / variable argument
# def show(*args):
#     print(args[3])
#     # for x in args:
#     # print(x)                  to read the whole list
    
# show(101,"wow","ten",8.90) 


# def revNum(num):
#     if num > 0:
#         rem = num % 10
#         num = num // 10
#         print(rem, end ="")
#         revNum(num)
        
# revNum(1234)

# def revNum(num, add=""):
#     if num > 0:
#         rem = num % 10
#         num = num // 10
#         add += str(rem)  # Store the digit
#         return revNum(num, add)  # Recursive call with updated string
#     return add  # Return the reversed number when recursion ends

# # Call function and store result
# result = revNum(1234)
# print(result)  # Output: "4321"


# # reverse the string (do with recursion)
# # reverse the sentence (reverse each word at same place do with recursion)

# # STRINGS
# # string builder , sting buffer IMPORTANT for Placement

# strvar = "mitwpu pune"
# print(strvar)
# print(type(strvar))
# print(strvar[5])
# print(len(strvar))

# for i in range(0,len(strvar),2):       #printing alternate 
#     print(strvar[i], end="")

# # no. of vowels count
# str = "mitwpu pune"
# vowels = "aeiou"
# count = 0
# for ch in str:
#     if ch in vowels:
#         count += 1
# print(count)
# # print alternate chr
# str = "mitwpu pune"
# for i in range(0, len(str), 2):
#     print(str[i], end="")
    

# take input and find out the chr frequency (ex. how many times a in the string)

# for ch in strvar:
#     print(ch,end=' ' )
    
# flag=1
# for ch in strvar:
#     if flag==1:
#         print(ch,end='')
#         flag=0
#     else:
#         flag=1
# #  String Slicing
# str = "Hello World"
# print(str[0:5])  # Output: Hello
# print(str[6:])  # Output: World
# print(str[:5])  # Output: Hello
# print(str[6])  # Output: W
# print(str[-5:])  # Output: World
# print(str[:-6])  # Output: Hello
# print(str[-5:-1])  # Output: World
# print(str[0:5:2])  # Output: Hlo
# print(str[::-1])  # Output: dlroW ol


# Modules
# import math
# print(math.sqrt(16))
# print(math.pow(2, 3))
# print(math.pi)
# print(math.e)
# print(math.factorial(5))
# print(math.ceil(3.4))
# print(math.floor(3.4))
# print(math.gcd(12, 15))
# print(math.log(10))
# print(math.log10(10))
# print(math.log2(10))
# print(math.sin(90))
# print(math.cos(90))
# print(math.tan(90))
# print(math.degrees(math.pi))


# import calci
# print(calci.addsum(10, 20))

# try, except, else, finally
# x = 100
# try:
#     print(x)
# except:
#     print("not found") 
# else :
#     x = x+1
#     print(x)
# finally:
#     print("done")
    

# error handling practice
# try:
#     x = 10
#     print(x) #NameError
    
#     print(10/0) #ZeroDivisionError
    
#     print("Hello") #IndentationError
    
#     print(int("Hello")) #ValueError
    
#     fp = open("file.txt") #FileNotFoundError
    
# except NameError:
#     print("NameError occurred")

# except ZeroDivisionError:
#     print("ZeroDivisionError occurred")
    
# except IndentationError:
#     print("IndentationError occurred")

# except ValueError:
#     print("ValueError occurred")

# except FileNotFoundError:
#     print("FileNotFoundError occurred")

# else:
#     print("No error occurred")

# finally:
#     print("Finally block executed")


# # Assertion Error
# def check_positive(number):
#     assert number > 0, "Number must be positive"
#     print("Valid number!")

# try:
#     check_positive(-5)
# except AssertionError as e:
#     print(f"Assertion Error: {e}")



# str = "new"
# reverse = str[::-1]
# print(str == reverse)

# LIST
# new1 = input("Enter the list: ")
# list = [new1]
# print(list)

# new = [101, "Amit", 20.5,]
# new[0] = 102
# print(new)

# print(len(new))

# for i in range(len(new)):
#     print(new[i])
    

# # insert, append, remove, pop, clear, sort, reverse, copy
# new.append("MIT")
# print(new)

# new.insert(1, "Pune")
# print(new)

# new.remove("Pune")
# print(new)

# new.pop(1)
# print(new)

# new.clear()
# print(new)

# new = [101, "Amit", 20.5,]
# new.sort()
# print(new)

# new.reverse()
# print(new)

# new1 = new.copy()
# print(new1)

# alist =["amit", 101, 89.90]
# alist.insert(2, "MCA")
# alist.insert(4,"Pune")
# alist.insert(8, "abc@home")
# alist.insert(-1, "xyz@home")
# print(alist)

# # # Tuple
# tuple = (101, "Amit", 20.5)
# print(tuple)
# print(type(tuple))


# temp = 100,"MIT",90.88
# print(type(temp))

# for i in range(0,len(tuple)):
#     print(tuple[i], end=" ")
    
# tvar = (101,"ajay", "MIT", "MCA", 89.89)
# name = "Amit"
# # tvar[1] = name
# print(tvar)


# # add
# tvar1 = (101, "ajay")
# tvar2 = (101,20)
# tvar1 = tvar1+tvar2
# print(tvar1)

# # SET DEMO (sort the numeric data in ascending order and shuffle the strings)
# sobj={1,2,4,5, "amit", "ajay", "omkar", "rajesh"}
# print("Set: ", sobj)

# # in set print the 2nd part of a string 
# sobj = {"amit kumar", "ajay", "omkar", "rajesh"} # in this case i want to print only kumar 

set1 =  {1,2,3,4}
alist = ["a","b","c","d",1,2,3,]
strvar = "my name is xyz"
tupvar = ("ABCD",) # when u apply , it becomes tuple if not then it will be treated as string
temp = tupvar[0]
# set1.update(alist)
set1.update(alist)
new =set(set1)

# print(new)
# count=0
# print("SET 1 : ",set1," Len : ",len(set1))

# for var in new:
#     if var in "":
#         count = count+1
#         print(count)
        
        
        
# dictionary
dictvar = {"name" : "amit", "program": "MCA","per" : 89.90,"city" : "Pune", "name" : "rajesh"}  # it overrides the last name value
print(dictvar)

newdict = {101: {"name": "Amit", "program": "MCA", "per": 89.90, "city": "Pune"},
        102: {"name": "Ajay", "program": "MCA", "per": 90.00, "city": "Mumbai"},
        103: {"name": "Omkar", "program": "MCA", "per": 85.50, "city": "Nashik"}}
print(newdict[101]["name"])
print(newdict[102]["program"])
print(newdict[103]["per"])