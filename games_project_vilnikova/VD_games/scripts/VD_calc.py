from VD_games.cli import welcome_user
from VD_games.engine import run_game
from VD_games.games.calc import generate_question_answer


def main():
    name = welcome_user()
    success = run_game(
        "What is the result of the expression?",
        generate_question_answer
    )
    if success:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
