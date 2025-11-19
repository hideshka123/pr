import random


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def generate_question_answer():
    number = random.randint(2, 100)
    question = str(number)
    answer = "yes" if is_prime(number) else "no"
    return question, answer
