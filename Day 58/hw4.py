def number():
    number = int(input("guess the number:"))

    if number == 11:
        print("correct answer. good job")

    elif number == 1:
        print("wrong answer. try again")

number()