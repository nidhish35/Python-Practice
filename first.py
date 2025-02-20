a=200
b=200
e,f=20,40
c=a+b
h=e+f
print(c,h)

#you can assign single value to multiple value


#pack and unpack
c=10,20
a,b=c
print(a,b)

#finding data type
print(type(a))

#you can also do
a=int(100)
b=float(12.2)
name=str("mit")
print(type(name))

#typecasting
a=int(80.50)
d=float(a)
b=float("20")
print(a,b,d)


# comparision
a="CAT"
b="MAT"
ans=a<b

print("CAT<MAT", ans)

# logical operator (value of 0 is considered as false else all are true)
a = 30
b = 30
c = a and b

print(c)

#  learn bitwise , membership, identity operators
# swap 2 numbers using bitwise operator

a = 4 << 1
#a<<b = a * 2(power)b
#a>>b = a / 2(power)b
print(a)


a=4
b=6
c = a&b
print(c)

#membership Operator
# z = "Hello world HELLO"
# count = 0
# y = 'H'

# print("Hello" in a)



#Identity operator(it works on memory location Compares the memory location values)
a = 10
b = 10
print(a is b)


# inline if else
a = 100
b = 20
c = 30
print(a if a > b else b if b > c else c if c > a else a)

# q1 write a program to check prime number , perfect number , armstrong number ,fibonacci series
#  all string operations append , reverse etc
#  basic array operations reading the alternate arrays 
#  reverse the array, list 
# lc gcd and pascles traingle
# 3, 4 patters (star)

# Fibonacci series 
# def fibo(n):
#     a = 0
#     b = 1
#     if n == 1:
#         print(a)
#     else:
#         print(a)
#         print(b)
#         for i in range(2, n):
#             c = a + b
#             a = b
#             b = c
#             print(c)

# fibo(10)

# # # # Prime number
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# # Print prime numbers from 1 to 50
# for num in range(1, 51):
#     if is_prime(num):
#         print(num, end=" ")


# # # # Perfect number
# n = int (input("Enter the number: "))
# sum = 0
# for i in range(1, n):
#     if n % i == 0:
#         sum += i
# if sum == n:
#     print("Perfect number")
# else:
#     print("Not a perfect number")
    
# # # # Armstrong number
# num = int(input("Enter the number: "))
# length = len(str(num))
# sum = 0
# temp = num
# while temp > 0:
#     digit = temp % 10
#     sum += digit ** length
#     temp //= 10
# if num == sum:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")

# # # pelindrome number
# num = int(input("Enter the number: "))
# temp = num
# rev = 0
# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num //= 10
# if temp == rev:
#     print("Pelindrome number")
# else:
#     print("Not a pelindrome number")

# # reverse the digit of number
# num = int(input("Enter the number: "))
# rev = 0
# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num //= 10
# print(rev)

# # star pattern
# for i in range(5):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()

# # # star pattern 2
# for i in range(5):
#     for j in range(5-i):
#         print("*", end=" ")
#     print()

# # # star pattern 3
# for i in range(5):
#     for j in range(5-i):
#         print(" ", end=" ")
#     for k in range(i+1):
#         print("*", end=" ")
#     print()
    
# # String operations
# string = "Hello World"
# print(string[::-1])  # Reverse the string
# print(string + " " + "Python")  # Append the string

# read function pointer

# FUNCTIONS

def wow():
    print("wowowowo")

wow()

def wow2(a,b):
    print(a+b)
    
wow2(2,3)


def sum(a,b):
    return a+b

add = sum(5,5)
print(add)

# print("Addition of {1} & {0} = {2}".format(a,b,add))


# Pointer / variable argument
def show(*args):
    print(args[3])
    # for x in args:
    # print(x)                  to read the whole list
    
show(101,"wow","ten",8.90) 


def revNum(num):
    if num > 0:
        rem = num % 10
        num = num // 10
        print(rem, end ="")
        revNum(num)
        
revNum(1234)

def revNum(num, add=""):
    if num > 0:
        rem = num % 10
        num = num // 10
        add += str(rem)  # Store the digit
        return revNum(num, add)  # Recursive call with updated string
    return add  # Return the reversed number when recursion ends

# Call function and store result
result = revNum(1234)
print(result)  # Output: "4321"


# reverse the string (do with recursion)
# reverse the sentence (reverse each word at same place do with recursion)