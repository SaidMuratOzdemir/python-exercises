# These program works for finding a number which we find with some guesses.
# After entering guesses program provide some hints that is correct place and incorrect place correct place means
# some numbers are correct incorrect means the number includes some numbers but wrong place

number = int(input("Enter a number: "))

while (number < 100) or (number > 999):  # This section is for finding if the number is 3 digit or not
    print("Invalid number, enter a three-digit positive number: ")
    number = int(input("Enter a number: "))

guess = int(input("Your guess: "))

while (guess < 100) or (guess > 999):  # This section is for finding if the guess is 3 digit or not
    print("Invalid guess, enter a three-digit positive number: ")

    guess = int(input("Your guess: "))

while guess != number:  # This section is for finding if the guess is 3 digit or not
    while (guess < 100) or (guess > 999):
        print("Invalid guess, enter a three-digit positive number: ")
        guess = int(input("Your guess: "))

    # calculates the digits of the number
    # We calculate the digits of the number in while loop because we need to change them later.
    numberDigitThird = number % 10
    numberDigitSecond = (int(number / 10)) % 10
    numberDigitFirst = int(number / 100)

    # calculates the digits of the guess
    guessDigitThird = guess % 10
    guessDigitSecond = int(guess / 10) % 10
    guessDigitFirst = int(guess / 100)

    incorrectDigit = 0
    correctDigit = 0

    # checking for same numbers for each digit if it is not returns False for each digit
    if numberDigitFirst == guessDigitFirst:
        correctDigit += 1
        booleanFirst = True
    else:
        booleanFirst = False

    if numberDigitSecond == guessDigitSecond:
        correctDigit += 1
        booleanSecond = True
    else:
        booleanSecond = False

    if numberDigitThird == guessDigitThird:
        correctDigit += 1
        booleanThird = True
    else:
        booleanThird = False

    # booleans is used in some cases because the program has to behave differently
    # this section is works when first digit is same, second digit is not same and third digit is not same
    if booleanFirst and not booleanSecond and not booleanThird:
        if numberDigitSecond == guessDigitThird:
            incorrectDigit += 1
        if numberDigitThird == guessDigitSecond:
            incorrectDigit += 1
    # this section is works when first digit is not same, second digit is same and third digit is not same
    if not booleanFirst and booleanSecond and not booleanThird:
        if numberDigitFirst == guessDigitThird:
            incorrectDigit += 1
        if numberDigitThird == guessDigitFirst:
            incorrectDigit += 1

    # this section is works when first digit is not same, second digit is not same and third digit is same
    if not booleanFirst and not booleanSecond and booleanThird:
        if numberDigitFirst == guessDigitSecond:
            incorrectDigit += 1
        if numberDigitSecond == guessDigitFirst:
            incorrectDigit += 1

    # this section is works when first digit is not same, second digit is not same and third digit is not same
    if not booleanFirst and not booleanSecond and not booleanThird:
        if (guessDigitFirst == numberDigitSecond) or (guessDigitFirst == numberDigitThird):
            incorrectDigit += 1

            if guessDigitFirst == numberDigitSecond:
                numberDigitSecond = -1
            else:
                numberDigitThird = -1

            guessDigitFirst = -1  # this is to avoid counting the same digit twice

        if (guessDigitSecond == numberDigitFirst) or (guessDigitSecond == numberDigitThird):
            incorrectDigit += 1

            if guessDigitSecond == numberDigitFirst:
                numberDigitFirst = -1
            else:
                numberDigitThird = -1

            guessDigitSecond = -1  # this is to avoid counting the same digit twice
        if (guessDigitThird == numberDigitFirst) or (guessDigitThird == numberDigitSecond):
            incorrectDigit += 1
            # Since we don't calculate or check anything we don't need to change the numberDigit or guessDigit

    # prints the result
    if not (booleanFirst and booleanSecond and booleanThird):
        print("Correct place: " + str(correctDigit))
        print("Incorrect place: " + str(incorrectDigit))
        guess = int(input("Your guess: "))
print("You guessed the number. Congrats!")
