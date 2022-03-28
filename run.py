import os
import time
from termcolor import colored
from art import *
from questions import questionBank

sdg_art = text2art("SDG-Quiz")
print(colored(sdg_art, 'green'))
print(colored(f'''
            ::::::: WELCOME :::::::::: 
            ||        to            ||
            ||      SDG-Quiz        ||
            ::::::::::::::::::::::::::
            ''', 'yellow'))

# Create a list of question dictionaries.
qsns = questionBank()
score = 0


class Question:
    """
    Blueprint of questions.
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
        self.user_answer = input('Enter your answer.\n')
        return self.user_answer

    def ask_question(self):
        """
        Display question prompt and choices
        """
        print(f'{self.question_index}. {self.question} \n')
        print('A.', self.choice_a, '\n')
        print('B.', self.choice_b, '\n')
        print('C.', self.choice_c, '\n')
        print('D.', self.choice_d, '\n')
        self.user_answer = self.get_answer()


class User:
    """"
    Defines users
    """
    def __init__(self):
        """
        Get username to initialize name
        """
        self.name = self.get_name()
        self.score = 0
        self.given_answer = ''

    def get_name(self):
        """
        Accept user input and validate it.
        """
        self.name = input('Enter your name.\n')
        while True:
            if len(self.name)<=2:
                print('Name too short. It should be at least 3 characters.\n')
                self.name = input('Please enter a valid name.\n')
            elif len(self.name)>20:
                print('Name may not be more than 20 characters.\n')
                self.name = input('Please enter a valid name.\n')
            else:
                break
        return self.name

    def show_question(self, question_index):
        """
        Display questions and choices
        """
        self.question_object = Question(question_index, qsns[question_index])
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
            print('You answer should be one of: a, b, c or d')
            self.given_answer = input('Try again.\n')
        return self.given_answer

    def evaluate_answer(self, qsn, given_answer):
        """
        Get the current question number and the current answer.
        Compare it with corrent answer for the given question.
        Display feedback and if answer is correct, increment score.
        """
        if given_answer.upper() == qsns[qsn]['answer']:
            print(colored('Correct! Well done.', 'green'))
            self.update_score()
        else:
            print(colored('Incorrect', 'red'))
        print(f'Your score: {self.score}')
        time.sleep(0)
        os.system("clear")

def start_quiz():
    is_ready = input("Ready to start? Press 'y' or 'n' " )
    if is_ready.lower() != 'y':
        is_ready = input("You need to enter 'y' or 'n' ")
    # Create an instance of the user class.
    user = User()
    return user

def take_quiz():
    """
    Start the quiz. Get answer, give feedback and show next question.
    """
    user = start_quiz()
    for i in range(2):
        user.show_question(i)
        user.validate_answer()
        user.evaluate_answer(i, user.given_answer)
    print(f'You have answered {user.score} questions out of {len(qsns)}.')


take_quiz()
