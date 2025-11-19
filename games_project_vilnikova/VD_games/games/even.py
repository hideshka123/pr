import random


def generate_question_answer():
    number = random.randint(1, 100)
    question = str(number)
    answer = "yes" if number % 2 == 0 else "no"
    return question, answer
