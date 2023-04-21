import random
import time

with open('math_highscore.txt' , 'r+') as hiscore:
    highscore = hiscore.read()
    if highscore == '':
        hiscore.write('No_one:0')
score = 0
def sleep(num):
    time.sleep(num)

def load():
    for i in range(101):
        print(f"{i}% done", end = '\r', flush=True)
        sleep(random.uniform(0, 0.04))
        if i == 100:
            sleep(1)
            print("Complete!\n")
            sleep(2)

def title(title):
    print('-' * len(title))
    print(title)
    print('-' * len(title))

def type_effect(text):
    for letter in text:
        print(letter, end='', flush=True)
        sleep(0.01)

def leave():
    with open('math_highscore.txt' , 'r+') as hiscore:
        highscore = hiscore.read()
        key, value = highscore.split(':')
        mydict = {}
        mydict[key] = value
        names = mydict.keys()
        name = list(names)[0]
        hscores = mydict.values()
        hscore = list(hscores)[0]
        int_hscore = int(hscore)
        if score > int_hscore:
            type_effect(f"NEW HIGH SCORE! Your score was {score} points!\n")
            name = input("Enter your name: ")
            if ':' in name:
                while ':' in name:
                    type_effect("Invalid character used. Please don't use a colon(:).\n")
                    name = input("Enter your name: ")
            elif len(name) < 3:
                while len(name) < 3:
                    type_effect("Please make sure your name is greater than 3 characters.\n")
                    name = input("Enter your name: ")

            elif len(name) > 20:
                while len(name) > 20:
                    type_effect("Please make sure your name is lesser than 20 characters.\n")
                    name = input("Enter your name: ")
            hiscore.truncate(0)
            hiscore.seek(0)
            result = f'{name}:{score}'
            hiscore.write(f"{result}")
            type_effect(f"Congratulations {name} for achieving the new high score!\n")
        else:
            type_effect(f"HIGH SCORE: {hscore} by {name}\n")
        sleep(2)
    type_effect("Ok, you are now leaving the game.")
    sleep(1)

def menu():
    global score
    type_effect("\nMenu:\n\n")
    with open('math_highscore.txt', 'r') as hi:
        highscore = hi.read()
        key, value = highscore.split(':')
        mydict = {}
        mydict[key] = value
        names = mydict.keys()
        name = list(names)[0]
        hscores = mydict.values()
        hscore = list(hscores)[0]

    print(f"HIGH SCORE: {hscore} by {name}\n")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Indices")
    print("6. INSTRUCTIONS")
    print("7. CREDITS")
    print("8. EXIT\n")
    type_effect(f"SCORE: {score}\n\n")

def addition(num_1, num_2, num_3, num_4, p1, p2, l1, l2):
    global score
    while score >= 0:
        num1 = random.randint(num_1, num_2)
        num2 = random.randint(num_3, num_4)
        type_effect(f"What is {num1} + {num2}?\n")
        sleep(0.5)
        start = time.time()
        add_guess = input('>>> ')
        end = time.time()
        elapsed = end - start

        try:
            if add_guess == 'quit' or add_guess == 'exit' or add_guess == 'q' or add_guess == 'l':
                break

            if int(add_guess) == (num1 + num2):
                type_effect(f'Correct! That took you {round(elapsed, 2)} seconds to answer!\n')
                points = random.randint(p1, p2)
                score += points
                type_effect(f"You got {points} points!\n")
                type_effect(f"SCORE:  {score}\n")
                sleep(0.5)

            else:
                type_effect(f'Incorrect...{num1} + {num2} = {num1 + num2}. But you said it was {add_guess}.\n')
                loss = random.randint(l1, l2)
                score -= loss
                type_effect(f"You lost {loss} points.\n")
                type_effect(f"SCORE:  {score}\n")
                sleep(0.5)
        except ValueError:
            type_effect("Invalid input. Try again!\n")

    else:
        type_effect('You lost!\n')

def subtraction(num_1, num_2, num_3, num_4, p1, p2, l1, l2):
    global score
    while score >= 0:
        num1 = random.randint(num_1, num_2)
        num2 = random.randint(num_3, num_4)
        type_effect(f"What is {num1} - {num2}?\n")
        sleep(0.5)
        start = time.time()
        sub_guess = input('>>> ')
        end = time.time()
        elapsed = end - start

        try:
            if sub_guess == 'quit' or sub_guess == 'exit' or sub_guess == 'q' or sub_guess == 'l':
                break

            if int(sub_guess) == (num1 - num2):
                type_effect(f'Correct! That took you {round(elapsed, 2)} seconds to answer!\n')
                points = random.randint(p1, p2)
                score += points
                type_effect(f"You got {points} points!\n")
                type_effect(f"SCORE:  {score}\n")
                sleep(0.5)

            else:
                type_effect(f'Incorrect...{num1} - {num2} = {num1 - num2}. But you said it was {sub_guess}.\n')
                loss = random.randint(l1, l2)
                score -= loss
                type_effect(f"You lost {loss} points.\n")
                type_effect(f"SCORE:  {score}\n")
                sleep(0.5)
        except ValueError:
            type_effect("Invalid input. Try again!\n")

    else:
        type_effect('You lost!\n')

def multiplication(num_1, num_2, num_3, num_4, p1, p2, l1, l2):
    global score
    while score >= 0:
        num1 = random.randint(num_1, num_2)
        num2 = random.randint(num_3, num_4)
        mul = ['times', '*']
        type_effect(f"What is {num1} {random.choice(mul)} {num2}?\n")
        sleep(0.5)
        start = time.time()
        mul_guess = input('>>> ')
        end = time.time()
        elapsed = end - start

        try:
            if mul_guess == 'quit' or mul_guess == 'exit' or mul_guess == 'q' or mul_guess == 'l':
                break

            if int(mul_guess) == (num1 * num2):
                type_effect(f'Correct! That took you {round(elapsed, 2)} seconds to answer!\n')
                points = random.randint(p1, p2)
                score += points
                type_effect(f"You got {points} points!\n")
                type_effect(f"SCORE:  {score}\n")
                sleep(0.5)

            else:
                type_effect(f'Incorrect...{num1} {random.choice(mul)} {num2} = {num1 * num2}. ')
                type_effect(f'But you said it was {mul_guess}.\n')
                loss = random.randint(l1, l2)
                score -= loss
                type_effect(f"You lost {loss} points.\n")
                type_effect(f"SCORE:  {score}\n")
                sleep(0.5)
        except ValueError:
            type_effect("Invalid input. Try again!\n")

    else:
        type_effect('You lost!\n')
        sleep(2)

def division(num_1, num_2, num_3, num_4, p1, p2, l1, l2):
    global score
    while score >= 0:
        num1 = random.randint(num_1, num_2)
        num2 = random.randint(num_3, num_4)

        while not(num1 % num2 == 0 and num1 != num2 and num1 > num2):
            num1 = random.randint(num_1, num_2)
            num2 = random.randint(num_3, num_4)

        div = ['/']
        type_effect(f"What is {num1} {random.choice(div)} {num2}?\n")
        sleep(0.5)
        start = time.time()
        div_guess = input('>>> ')
        end = time.time()
        elapsed = end - start

        try:
            if div_guess == 'quit' or div_guess == 'exit' or div_guess == 'q' or div_guess == 'l':
                break

            if int(div_guess) == (num1 / num2):
                type_effect(f'Correct! That took you {round(elapsed, 2)} seconds to answer!\n')
                points = random.randint(p1, p2)
                score += points
                type_effect(f"You got {points} points!\n")
                type_effect(f"SCORE:  {score}\n")
                sleep(0.5)

            else:
                type_effect(f'Incorrect...{num1} {random.choice(div)} {num2} = {num1 / num2}.')
                type_effect(f'But you said it was {div_guess}.\n')
                loss = random.randint(l1, l2)
                score -= loss
                type_effect(f"You lost {loss} points.\n")
                type_effect(f"SCORE:  {score}\n")
                sleep(0.5)
        except ValueError:
            type_effect("Invalid input. Try again!\n")

    else:
        type_effect('You lost!\n')
        sleep(2)

def indices(num_1, num_2, num_3, num_4, p1, p2, l1, l2):
    global score
    while score >= 0:
        num1 = random.randint(num_1, num_2)
        num2 = random.randint(num_3, num_4)
        ind = ['to the power', '**']
        type_effect(f"What is {num1} {random.choice(ind)} {num2}?\n")
        sleep(0.5)
        start = time.time()
        ind_guess = input('>>> ')
        end = time.time()
        elapsed = end - start

        try:
            if ind_guess == 'quit' or ind_guess == 'exit' or ind_guess == 'q' or ind_guess == 'l':
                break

            if int(ind_guess) == (num1 ** num2):
                type_effect(f'Correct! That took you {round(elapsed, 2)} seconds to answer!\n')
                points = random.randint(p1, p2)
                score += points
                type_effect(f"You got {points} points!\n")
                type_effect(f"SCORE:  {score}\n")
                sleep(0.5)

            else:
                type_effect(f'Incorrect...{num1} {random.choice(ind)} {num2} = {num1 ** num2}.')
                type_effect(f'But you said it was {ind_guess}.\n')
                loss = random.randint(l1, l2)
                score -= loss
                type_effect(f"You lost {loss} points.\n")
                type_effect(f"SCORE:  {score}\n")
                sleep(0.5)
        except ValueError:
            type_effect("Invalid input. Try again!\n")

    else:
        type_effect('You lost!\n')
        sleep(2)

title("  Crazy Numbers!  ")
load()
while score >= 0:
    menu()
    choice = input("Enter your choice: ")
    while choice not in ['1', '2', '3', '4', '5', '6', '7', '8']:
        type_effect("Invalid menu option!\nPlease choose from 1, 2, 3, 4, 5, 6, 7, or 8.\n")
        choice = input("Please choose a valid option: ")

    if choice == '8':
        leave()
        break

    elif choice == '6':
        title("  INSTRUCTIONS  ")
        type_effect("This is a simple game built with the intention to ")
        type_effect("increase the problem-solving ability of an individual.\n")
        type_effect("Here are the instructions: \n\n")
        print(" 1. Choose the type of problem that you want to solve. For example, enter 1 if you want to do addition.")
        print(" 2. Within that, choose the difficulty level that you want to attempt.")
        print(" 3. If you ever want to leave, just enter 'quit' or 'exit'. It will return you back to the main menu.")
        print("    Tip: You could just enter 'q' or 'l' which stands for quit and leave respectively.")
        sleep(5)
        input("Press 'enter' to return to the menu: ")
        sleep(0.5)

    elif choice == '7':
        title("  CREDITS  ")
        type_effect("The main developer: Shashwat Bhandari\n\n")
        print("Creator:    Shashwat Bhandari")
        print("Scripter:   Shashwat Bhandari")
        print("Tester:     Shashwat Bhandari\n")
        sleep(3)
        input("Press 'enter' to return to the menu: ")
        sleep(0.5)

    elif choice == '1':
        type_effect("OK! Choose the difficulty level:\n")
        type_effect("Addition Levels available:\n\n")
        print("   1. Effortless")
        print("   2. Easy")
        print("   3. Medium")
        print("   4. Difficult")
        print("   5. Extreme")
        print("   6. Insane")
        print("   7. Crazy")
        print("   8. MENU")
        print("   9. QUIT\n")
        type_effect(f"   SCORE: {score}\n\n")
        add_choice = input("Choose the level that you want to attempt: ")

        while add_choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            type_effect("Invalid option!\nPlease choose from 1, 2, 3, 4, 5, 6, 7, 8, or 9.\n")
            add_choice = input("Please choose a valid option: ")

        if add_choice == '9':
            leave()
            break

        elif add_choice == '8':
            type_effect("OK! Now returning to the menu.\n")
            sleep(1)
            continue

        elif add_choice == '1':
            type_effect("OK! This will be a piece of cake!\n")
            sleep(1)
            addition(0, 10, 0, 25, 2, 8, 2, 6)

        elif add_choice == '2':
            type_effect("OK! This will be quite easy!\n")
            sleep(1)
            addition(10, 60, 25, 75, 8, 14, 6, 10)

        elif add_choice == '3':
            type_effect("OK! This will be quite hard!\n")
            sleep(1)
            addition(20, 135, 75, 150, 14, 20, 10, 14)

        elif add_choice == '4':
            type_effect("OK! This will be quite difficult!\n")
            sleep(1)
            addition(30, 485, 150, 500, 20, 26, 14, 18)

        elif add_choice == '5':
            type_effect("OK! This will be very difficult!\n")
            sleep(1)
            addition(40, 985, 500, 1000, 26, 32, 18, 22)

        elif add_choice == '6':
            type_effect("OK! This will be insanely difficult!\n")
            sleep(1)
            addition(50, 4985, 1000, 5000, 32, 38, 22, 26)

        elif add_choice == '7':
            type_effect("Good luck! You will need it...\n")
            sleep(1)
            addition(100, 14985, 5000, 15000, 38, 50, 26, 30)

    elif choice == '2':
        type_effect("OK! Choose the difficulty level:\n")
        type_effect("Subtraction Levels available:\n\n")
        print("   1. Effortless")
        print("   2. Easy")
        print("   3. Medium")
        print("   4. Difficult")
        print("   5. Extreme")
        print("   6. Insane")
        print("   7. Crazy")
        print("   8. MENU")
        print("   9. QUIT\n")
        type_effect(f"   SCORE: {score}\n\n")
        sub_choice = input("Choose the level that you want to attempt: ")

        while sub_choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            type_effect("Invalid option!\nPlease choose from 1, 2, 3, 4, 5, 6, 7, 8, or 9.\n")
            sub_choice = input("Please choose a valid option: ")

        if sub_choice == '9':
            leave()
            break

        elif sub_choice == '8':
            type_effect("OK! Now returning to the menu.\n")
            sleep(1)
            continue

        elif sub_choice == '1':
            type_effect("OK! This will be a piece of cake!\n")
            sleep(1)
            subtraction(10, 25, 0, 10, 2, 8, 2, 6)

        elif sub_choice == '2':
            type_effect("OK! This will be quite easy!\n")
            sleep(1)
            subtraction(40, 75, 10, 40, 8, 14, 6, 10)

        elif sub_choice == '3':
            type_effect("OK! This will be quite hard!\n")
            sleep(1)
            subtraction(75, 150, 40, 75, 14, 20, 10, 14)

        elif sub_choice == '4':
            type_effect("OK! This will be quite difficult!\n")
            sleep(1)
            subtraction(150, 500, 75, 150, 20, 26, 14, 18)

        elif sub_choice == '5':
            type_effect("OK! This will be very difficult!\n")
            sleep(1)
            subtraction(500, 1000, 150, 750, 26, 32, 18, 22)

        elif sub_choice == '6':
            type_effect("OK! This will be insanely difficult!\n")
            sleep(1)
            subtraction(1000, 5000, 750, 3000, 32, 38, 22, 26)

        elif sub_choice == '7':
            type_effect("Good luck! You will need it...\n")
            sleep(1)
            subtraction( 5000, 15000, 3000, 10000, 38, 50, 26, 30)

    elif choice == '3':
        type_effect("OK! Choose the difficulty level:\n")
        type_effect("Multiplication Levels available:\n\n")
        print("   1. Effortless")
        print("   2. Easy")
        print("   3. Medium")
        print("   4. Difficult")
        print("   5. Extreme")
        print("   6. Insane")
        print("   7. Crazy")
        print("   8. MENU")
        print("   9. QUIT\n")
        type_effect(f"   SCORE: {score}\n\n")
        mul_choice = input("Choose the level that you want to attempt: ")

        while mul_choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            type_effect("Invalid option!\nPlease choose from 1, 2, 3, 4, 5, 6, 7, 8, or 9.\n")
            mul_choice = input("Please choose a valid option: ")

        if mul_choice == '9':
            leave()
            break

        elif mul_choice == '8':
            type_effect("OK! Now returning to the menu.\n")
            sleep(1)
            continue

        elif mul_choice == '1':
            type_effect("OK! This will be a piece of cake!\n")
            sleep(1)
            multiplication(0, 5, 0, 5, 2, 8, 2, 6)

        elif mul_choice == '2':
            type_effect("OK! This will be quite easy!\n")
            sleep(1)
            multiplication(5, 10, 5, 10, 8, 14, 6, 10)

        elif mul_choice == '3':
            type_effect("OK! This will be quite hard!\n")
            sleep(1)
            multiplication(3, 15, 3, 15, 14, 20, 10, 14)

        elif mul_choice == '4':
            type_effect("OK! This will be quite difficult!\n")
            sleep(1)
            multiplication(5, 20, 5, 20, 20, 26, 14, 18)

        elif mul_choice == '5':
            type_effect("OK! This will be very difficult!\n")
            sleep(1)
            multiplication(7, 50, 7, 50, 26, 32, 18, 22)

        elif mul_choice == '6':
            type_effect("OK! This will be insanely difficult!\n")
            sleep(1)
            multiplication(9, 100, 9, 100, 32, 38, 22, 26)

        elif mul_choice == '7':
            type_effect("Good luck! You will need it...\n")
            sleep(1)
            multiplication( 11, 200, 11, 200, 38, 50, 26, 30)

    elif choice == '4':
        type_effect("OK! Choose the difficulty level:\n")
        type_effect("Division Levels available:\n\n")
        print("   1. Effortless")
        print("   2. Easy")
        print("   3. Medium")
        print("   4. Difficult")
        print("   5. Extreme")
        print("   6. Insane")
        print("   7. Crazy")
        print("   8. MENU")
        print("   9. QUIT\n")
        type_effect(f"   SCORE: {score}\n\n")
        div_choice = input("Choose the level that you want to attempt: ")

        while div_choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            type_effect("Invalid option!\nPlease choose from 1, 2, 3, 4, 5, 6, 7, 8, or 9.\n")
            div_choice = input("Please choose a valid option: ")

        if div_choice == '9':
            leave()
            break

        elif div_choice == '8':
            type_effect("OK! Now returning to the menu.\n")
            sleep(1)
            continue

        elif div_choice == '1':
            type_effect("OK! This will be a piece of cake!\n")
            sleep(1)
            division(0, 50, 1, 50, 2, 8, 2, 6)

        elif div_choice == '2':
            type_effect("OK! This will be quite easy!\n")
            sleep(1)
            division(5, 100, 5, 100, 8, 14, 6, 10)

        elif div_choice == '3':
            type_effect("OK! This will be quite hard!\n")
            sleep(1)
            division(10, 200, 10, 200, 14, 20, 10, 14)

        elif div_choice == '4':
            type_effect("OK! This will be quite difficult!\n")
            sleep(1)
            division(20, 300, 20, 300, 20, 26, 14, 18)

        elif div_choice == '5':
            type_effect("OK! This will be very difficult!\n")
            sleep(1)
            division(30, 400, 30, 400, 26, 32, 18, 22)

        elif div_choice == '6':
            type_effect("OK! This will be insanely difficult!\n")
            sleep(1)
            division(40, 500, 40, 500, 32, 38, 22, 26)

        elif div_choice == '7':
            type_effect("Good luck! You will need it...\n")
            sleep(1)
            division( 50, 1000, 50, 1000, 38, 50, 26, 30)

    elif choice == '5':
        type_effect("OK! Choose the difficulty level:\n")
        type_effect("Indices Levels available:\n\n")
        print("   1. Effortless")
        print("   2. Easy")
        print("   3. Medium")
        print("   4. Difficult")
        print("   5. Extreme")
        print("   6. Insane")
        print("   7. Crazy")
        print("   8. MENU")
        print("   9. QUIT\n")
        type_effect(f"   SCORE: {score}\n\n")
        ind_choice = input("Choose the level that you want to attempt: ")

        while ind_choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            type_effect("Invalid option!\nPlease choose from 1, 2, 3, 4, 5, 6, 7, 8, or 9.\n")
            ind_choice = input("Please choose a valid option: ")

        if ind_choice == '9':
            leave()
            break

        elif ind_choice == '8':
            type_effect("OK! Now returning to the menu.\n")
            sleep(1)
            continue

        elif ind_choice == '1':
            type_effect("OK! This will be a piece of cake!\n")
            sleep(1)
            indices(0, 5, 0, 3, 2, 8, 2, 6)

        elif ind_choice == '2':
            type_effect("OK! This will be quite easy!\n")
            sleep(1)
            indices(3, 10, 2, 3, 8, 14, 6, 10)

        elif ind_choice == '3':
            type_effect("OK! This will be quite hard!\n")
            sleep(1)
            indices(5, 15, 2, 3, 14, 20, 10, 14)

        elif ind_choice == '4':
            type_effect("OK! This will be quite difficult!\n")
            sleep(1)
            indices(10, 20, 2, 3, 20, 26, 14, 18)

        elif ind_choice == '5':
            type_effect("OK! This will be very difficult!\n")
            sleep(1)
            indices(5, 20, 3, 4, 26, 32, 18, 22)

        elif ind_choice == '6':
            type_effect("OK! This will be insanely difficult!\n")
            sleep(1)
            indices(2, 10, 3, 5, 32, 38, 22, 26)

        elif ind_choice == '7':
            type_effect("Good luck! You will need it...\n")
            sleep(1)
            indices( 10, 30, 3, 5, 38, 50, 26, 30)
