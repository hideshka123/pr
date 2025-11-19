from prompt import string


def run_game(description, generate_question_answer):
    print(description)
    
    for _ in range(3):
        question, correct_answer = generate_question_answer()
        print(f"Question: {question}")
        user_answer = string("Your answer: ").strip()
        
        if user_answer == str(correct_answer):
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            return False
    
    return True
