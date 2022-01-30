try:
    #Main game source code
    import random
    num = random.randint(1,500)
    gpr = 8
    guesses = 8
    name = input("Enter your name: ").capitalize()
    print('In this game you have to guess a hidden number.\nIn between the game will tell you whether your guess is greater or lesser than hidden number.')
    print('Hidden number is between 1 to 500.')
    print(f'You have {str(gpr)} guesses to play\n')
    while True:
        guesses -= 1
        guess1 = int(input('Enter your guess: '))
        if guesses == 0 and guess1 == num:
            print('You won, you took', gpr - guesses, 'guesses to win this game')
            break
        if guesses == 0:
            print('No guesses are left')
            print('You lose, correct no. is',num)
            break
        if guess1 == num:
            print('You won, you took',gpr - guesses,'guesses to win this game')
            break
        elif guess1>num:
            print('Your guess is greater than hidden number, try again')
            print(guesses,'guesses are left')
            continue
        else:
            print('Your guess is lower than hidden number, try again')
            print(guesses,'guesses are left')
            continue
except Exception as e:
    print("Unexpected error!")
    print(num)

#Feedback saving code
feedback = input("Enter your feedback: ")
with open('Feedbacks.txt', 'a')as feedback_text:
    feedback_text.write(f'{name} - {feedback}\n')