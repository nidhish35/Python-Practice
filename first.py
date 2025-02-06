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
def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

n = int(input("Enter a number: "))
print(fibonacci(n))

# Prime number
def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if prime(num):
    print(num ,"is a prime number.")
else:
    print(num ," is not a prime number.")
