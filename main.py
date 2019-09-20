import random

QA_DELIMITER = " -_- "
RESPONSES_TO_INCORRECT = ["Sorry, that's not it.", "Good guess, but no.", "Oof, not it.", "Try again."]
GREETING_FILE = "intro.txt"
QUESTION_FILE = "questions.txt"

def main():
    intro()
    if (yes_to("Are you up to the challenge? ")):
        play_game()
        finish()
    else:
        print("k fam")


def intro():
    with open(GREETING_FILE) as greeting:
        print(greeting.read())

def play_game():
    with open(QUESTION_FILE) as questions:
        for line in questions:
            parts = line.split(QA_DELIMITER)
            question = parts[0]
            answer = parts[1].strip()
            ask_until_correct(question, answer)

def ask_until_correct(question, answer):
    user_answer = input(question + " ")
    while (user_answer.lower() != answer.lower()):
        print(random.choice(RESPONSES_TO_INCORRECT))
        user_answer = input(question + " ")
    print("That's right!")

def finish():
    print("Good job, you escaped the room!")

def yes_to(prompt):
    ans = input(prompt)
    return ans.lower() == "yes" or ans.lower() == "yeet"

main()