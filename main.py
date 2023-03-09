import random

print("Task 1")
print("By Using Binary Search, I Can Guess Numbers Faster.")
print("Write The Range Of Numbers From Which You Will Pick The Number.")
num1 = int(input("Lower Boundary: "))
num2 = int(input("Upper Boundary: "))
num3 = random.randint(num1, num2)
var1 = 0
var2 = 0
while var1 == 0:
    number1 = int(input("Did You Choose The Number "))
    if number1 == num3:
        str1 = "yes"
        print(str1)
        var2 += 1
        var1 = 1
    elif number1 >= num3:
        str1 = "less"
        print(str1)
        var2 += 1
    elif number1 <= num3:
        str1 = "greater"
        print(str1)
        var2 += 1
print("Secret Number Was Guessed In", var2, "Attempts!")

print("Task 2")
a = int(input("Enter A:"))
b = int(input("Enter B:"))
c = int(input("Enter C:"))
z = a
y = b
a = a+b
b = c-z
c = z+y+c
print(a, "( We Did A+B )")
print(b, "( We Did C-A )")
print(c, "( We Did A+B+C )")

print("Task 3")
numbers = [int(number) for number in input('Enter the numbers: ').split()]


def convert(km):
    miles = km / 1.6
    return miles


times = list(map(convert, numbers))
print(times)

print("Task 4")
words = ("first", "second", "third")
