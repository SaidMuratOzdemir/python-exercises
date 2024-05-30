# This program separates a number by its digits


input1 = int(input("Enter a valid number: "))
input1Backup = input1  # Since first while loop (line 10) destroys number, so we use backup

digitController = 1

while input1Backup > 0:  # These while loop controls the number of digits
    digitController *= 10
    input1Backup = input1Backup // 10

while True:
    if digitController == 0:  # This if statement prevents integer/0 error
        break
    if input1 // digitController == 0:  # This if statement provides that the zeros
        # in the middle of the number is not printed
        digitController = digitController // 10
    else:
        print("(", input1 // digitController, " * ", digitController, ")", sep="", end="")
        input1 = input1 % digitController
        digitController = digitController // 10
        if digitController == 0:  # This if statement checks whether there is  other digits  or not
            break
        elif input1 != 0:  # This if statements prints '+' if all other digits are not zero
            print(" + ", end="")
            