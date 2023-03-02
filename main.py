import random

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
