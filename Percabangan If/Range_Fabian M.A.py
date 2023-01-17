down = 0
up = 100
for i in range(1, 100):
    guessed_age = int((up + down) / 2)
    answer = input("Are you " + str(guessed_age) + " years old? ")
    if answer.lower() == "correct":
        print("Nice")
        break
    elif answer.lower() == "less":
        up = guessed_age
    elif answer.lower() == "more":
        down = guessed_age
    else:
        print("wrong answer")
