# Kevin Pham
# This program asks the user questions or riddles as part of an escape room.
# Questions are stored in the file "questions.txt"

import random
import time

QA_DELIMITER = " -_- "
RESPONSES_TO_INCORRECT = ["Sorry, that's not it.", "Good guess, but no.", "Oof, not it.", "Try again."]
GREETING_FILE = "intro.txt"
QUESTION_FILE = "questions.txt"
RECORDS_FOLDER = "records/"

# Main function in program
def main():
    intro()
    if (yes_to("Are you up to the challenge? ")):
        finish(play_game())
    else:
        print("k fam")

# Prints the intro from file GREETING_FILE
def intro():
    with open(GREETING_FILE) as greeting:
        print(greeting.read())

# Plays a single round of the escape room
# Asks questions until the correct answer is guessed
def play_game():
    unit = str(input("What's your team name? "))
    start = time.time()
    with open(RECORDS_FOLDER + unit.replace(" ", "_") + ".txt", "w") as record:
        record.write("Team name: " + unit + "\n")
        last_time = start
        with open(QUESTION_FILE) as questions:
            for line in questions:
                parts = line.split(QA_DELIMITER)
                question = parts[0]
                answer = parts[1].strip()
                ask_until_correct(question, answer)
                current_time = time.time()
                record.write("\"" + question + "\" was answered in " + str(round(current_time - last_time)) + " seconds\n")
                last_time = current_time
        result = time.time() - start;
        record.write("The final time was " + str(result))
        return round(result)

# Repeatedly asks the user the given question until the answer is guessed
# @param {String} question - question to be asked in prompt
# @param {String} answer - answer to require from user, case insensitive
def ask_until_correct(question, answer):
    user_answer = input(question + " ")
    while (user_answer.lower() != answer.lower()):
        print(random.choice(RESPONSES_TO_INCORRECT))
        user_answer = input(question + " ")
    print("That's right!")

# Prints message when all riddles are solved
def finish(elapsed_time):
    print("Good job, you escaped the room in " + str(elapsed_time) + " seconds!")

# Returns if the user says yes to the given prompt
# @param {String} prompt - prompt to show to user
def yes_to(prompt):
    ans = input(prompt)
    return ans.lower() == "yes" or ans.lower() == "yeet"

main()