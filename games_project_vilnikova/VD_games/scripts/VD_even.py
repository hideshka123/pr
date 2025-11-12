import random
from prompt import string
from VD_games.cli import welcome_user


def is_even(number):
    return number % 2 == 0


def play_game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    for _ in range(3):
        number = random.randint(1, 100)
        print(f"Question: {number}")
        user_answer = string("Your answer: ").strip().lower()
        
        correct_answer = "yes" if is_even(number) else "no"
        
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")


def main():
    name = welcome_user()
    play_game(name)


if __name__ == "__main__":
    main()
