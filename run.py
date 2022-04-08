# Import required external libraries
import os
import time
import statistics as st
from tabulate import tabulate
import gspread
from google.oauth2.service_account import Credentials
from termcolor import colored
from art import *

# Import questions and notes from data
from data import question_bank, sdg_note


# Set scope and cred variables as constants
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# Open the sdg_quiz google sheet
SHEET = GSPREAD_CLIENT.open('sdg_quiz')

# Open and store worksheets 
users = SHEET.worksheet('users')
answers = SHEET.worksheet('answers')

# Create a list of question dictionaries.
all_questions = question_bank()


class Question:
    """
    Defines the question class.
    Takes a list of dictionaries and displays questions and choices.
    """
    def __init__(self, question_index, dict_list):
        """"
        Initialize a question object
        """
        self.question_index = question_index + 1
        self.question = dict_list['question']
        self.choice_a = dict_list['choices']['A']
        self.choice_b = dict_list['choices']['B']
        self.choice_c = dict_list['choices']['C']
        self.choice_d = dict_list['choices']['D']
        self.answer = dict_list['answer']
        self.user_answer = ''

    def get_answer(self):
        """
        Get answer as user input
        """
        self.user_answer = input('Enter your answer:\n')
        return self.user_answer

    def ask_question(self):
        """
        Display question prompt and choices
        """
        print(f'{self.question_index}. {self.question} \n')
        print('  A.', self.choice_a, '\n')
        print('  B.', self.choice_b, '\n')
        print('  C.', self.choice_c, '\n')
        print('  D.', self.choice_d, '\n')
        self.user_answer = self.get_answer()


class User:
    """"
    Defines user the class
    """
    def __init__(self):
        """
        Get username to initialize name
        """
        self.name = self.get_name()
        self.score = None
        self.given_answer = ''

    def get_name(self):
        """
        Accept user input and validate it.
        """
        print(colored('\n................', 'yellow'))
        while True:
            self.name = input('Enter your name:\n')
            if self.name.isalpha():
                if len(self.name) <= 1 or len(self.name) > 20:
                    print('Name should be between 2 and 20 characters long.\n')
                else:
                    break
            else:
                print('Please use only alphabets.')
        os.system('clear')
        print(colored('......................', 'yellow'))
        print(colored(f'| Best of luck, {self.name}!', 'yellow'))
        print(colored('......................\n', 'yellow'))
        return self.name

    def show_question(self, question_index):
        """
        Display questions and choices
        """
        self.question_object = Question(question_index,
                                        all_questions[question_index])
        time.sleep(1)
        self.question_object.ask_question()
        self.given_answer = self.question_object.user_answer
        return self.given_answer

    def update_score(self):
        """
        Increment score if the answer is correct
        """
        self.score += 1
        return self.score

    def validate_answer(self):
        """
        Get answer from user and validate.
        Input answer can only be one of a, b, c or d.
        Change input to lower case and look it up in the list.
        """
        while self.given_answer.lower() not in ['a', 'b', 'c', 'd']:
            print('Your answer should be one of: a, b, c or d')
            self.given_answer = input('Try again.\n')
        return self.given_answer

    def evaluate_answer(self, this_question, given_answer):
        """
        Get the current question number and the current answer.
        Compare it with corrent answer for the given question.
        Display feedback and if answer is correct, increment score.
        """
        if given_answer.upper() == all_questions[this_question]['answer']:
            print(colored(f'Correct! Well done, {self.name}!', 'green'))
            self.update_score()
        else:
            print(colored('That was incorrect.', 'red'))
            print(f"The correct answer is:\
     {all_questions[this_question]['answer']}.")
        print('\n')
        time.sleep(1)


def welcome_board():
    """
    Display a Welcome message to the user
    """
    sdg_art = text2art("SDG-Quiz")
    print('\n')
    print(colored(f'::::::::::::::::::::: WELCOME :::::::::::::::::::::',
                  'yellow'))
    print(colored(f'''                        TO             ''', 'yellow'))
    print(colored(f'{sdg_art}', 'green'))
    print(colored(f':::::::::::::::::::::::::::::::::::::::::::::::::::',
                  'yellow'))
    time.sleep(2)


def display_instructions():
    """
    Describes how to take the quiz
    """
    os.system('clear')
    print(colored('::::::::::::::::::::::::::::::::', 'yellow'))
    print(colored('::     General Instructions    ::', 'yellow'))
    print(colored('::::::::::::::::::::::::::::::::\n', 'yellow'))
    print('1. This quiz consists of 10 multiple choice questions.\n')
    print('2. You will answer each question by selecting a, b, c or d.\n')
    print('3. The program will tell you if your answer is correct or not.\n')
    print('4. You will see your total score at the end of the quiz.\n')
    print('5. Each correct answer is worth one point.\n\n')
    time.sleep(3)
    is_ready = ''
    while True:
        is_ready = input("Press P and hit Enter to start the quiz.\n")
        if is_ready.lower() == 'p':
            break


def will_play():
    """
    Ask user if they want to play or quit
    """
    play_quiz = input('''Press P and hit Enter to take the quiz.
    \nPress Q and hit Enter to exit.\n''')
    if play_quiz.lower() == 'p':
        os.system('clear')
        display_instructions()
    elif play_quiz.lower() == 'q':
        print('Thank you for showing interest.\nGoodbye!')
        exit()
    else:
        print(colored('Invalid choice!', 'red'))
        return will_play()


def display_score_board():
    """
    Tabulate and display the names and top 5 scores
    """
    print('Fetching the highest 5 scores...\n')
    data = users.get_all_values()
    print(tabulate(data[0:5], headers='firstrow', tablefmt='fancy_grid'))
    time.sleep(3)
    will_play()


def main_menu():
    """
    Display menu and redirect user to
    start quiz or scoreboard or SDGs
    """
    print('\n')
    print('Please choose one of the following.\n')
    print('   1. Start quiz\n')
    print('   2. Show highest scores\n')
    print('   3. Read about SDGs\n')
    print('   4. Exit\n')
    menu_choice = None
    while True:
        menu_choice = input('Type 1, 2, 3 or 4 and hit Enter.\n')
        try:
            menu_choice = int(menu_choice)
        except ValueError:
            print('Invalid input! Please choose one of the alternatives')
            continue
        if menu_choice == 1:
            display_instructions()
            break
        elif menu_choice == 2:
            display_score_board()
            break
        elif menu_choice == 3:
            os.system('clear')
            sdg_note() # function imported from data
            time.sleep(3)
            will_play()
            break
        elif menu_choice == 4:
            print('Thank for stopping by.\nGoodbye!')
            time.sleep(2)
            os.system('clear')
            exit()
            break
        else:
            print('Choice out of range.')


def add_new_data(user):
    """
    Add new record to google sheet
    """
    new_answers = [user.name] + user.answers
    answers.append_row(new_answers)
    new_data = [user.name, user.score]
    users.append_row(new_data)
    users.sort((2, 'des'),)


def rank_score():
    """
    Get updated data
    Calculate and display descriptive statistics of score
    """
    scores = [int(item) for item in users.col_values(2)[1:]]
    print('\n')
    print(colored(':::::Quiz Statistics:::::\n', 'yellow'))
    print(f'The average score is: {round(st.mean(scores), 2)}')
    print(f'The median score is: {st.median(scores)}')
    print(f'The highest score is: {max(scores)}')
    print(colored('.........................', 'yellow'))


def play(user):
    """
    Iterate through all questions and alternate between
    asking a question, validation and evaluation of answers.
    """
    user.answers = []
    user.score = 0
    for i in range(len(all_questions)):
        user.show_question(i)
        user.validate_answer()
        user.answers.append(user.given_answer)
        user.evaluate_answer(i, user.given_answer)
    return user.answers


def end_quiz(user):
    """
    Tell user quiz is over, show scores
    Display statistics
    """
    os.system('clear')
    qover_art = text2art("QUIZ OVER")
    print(colored(f'{qover_art}', 'yellow'))
    print('Calculating your score...\n')
    time.sleep(3)
    add_new_data(user)
    print(f'''You have correctly answered {user.score}\
questions out of {len(all_questions)}.''')
    if user.score >= 7:
        print(colored(f'Excellent, {user.name}!', 'green'))
    elif user.score >= 5:
        print(colored(f'Very good, {user.name}!', 'green'))
    else:
        print(colored(f'Nice, {user.name}!', 'green'))
    print('\nThank you for taking the', colored('SDG QUIZ', 'green'), '.')
    rank_score()
    time.sleep(2)
    print('\n')
    print('Click on the Run Program button to start again.\n')


def main():
    """
    Start the quiz. Get answer, give feedback and show next question.
    """
    welcome_board()
    main_menu()
    user = User()
    play(user)
    end_quiz(user)

main()
