import random

# Task 1
print("Think Of A Number Between 1 And 15")
var1 = 0
number3 = 0
while var1 == 0:
    number1 = int(input("Your Number Is:"))
    number2 = random.randint(1, 15)
    if number1 != number2:
        string1 = "no"
        if number1 != number2:
            print(string1)
            number3 += 1

    else:
        string1 = "yes"
        if number1 == number2:
            print(string1)
            number3 += 1
            var1 = 1
print("Secret Number Was Guessed In", number3, "Attempts!")