from questions import questionBank

print('Welcome')
print('SDG Quiz')

# Create a list of question dictionaries.
qsns = questionBank()
score = 0


class Question:
    """
    Blueprint of questions.
    Takes a list of dictionaries and displays questions and choices.
    """
    def __init__(self, dict_list):
        """"
        Initialize a question object
        """
        self.question = dict_list['question']
        self.choice_a = dict_list['choices']['A']
        self.choice_b = dict_list['choices']['B']
        self.choice_c = dict_list['choices']['C']
        self.choice_d = dict_list['choices']['D']
        self.answer = dict_list['answer']
        self.user_answer = self.get_answer()


    def ask_question(self):
        """
        Display question prompt and choices
        """
        print(self.question, '\n')
        print('A.', self.choice_a, '\n')
        print('B.', self.choice_b, '\n')
        print('C.', self.choice_c, '\n')
        print('D.', self.choice_d, '\n')


    def get_answer(self):
        """
        Get answer as user input
        """
        self.ask_question()
        self.user_answer = input('Enter your answer.\n')
        return self.user_answer


class User:
    """"
    Defines users
    """
    def __init__(self):
        """
        Get username to initialize name
        """
        self.name = input('Enter your name:\n')
        self.score = 0
        self.given_answer = ''


    def show_question(self, question_index):
        self.question_object = Question(qsns[question_index])
        self.given_answer = self.question_object.user_answer
        return self.given_answer

    def update_score(self):
        """
        Increment score if the answer is correct
        """
        self.score += 1
        return self.score


    def validate_answer(self, given_answer):
        """
        Get answer from user and validate.
        Input answer can only be one of a, b, c or d.
        Change input to lower case and look it up in the list.
        """
        if given_answer.lower() not in ['a', 'b', 'c', 'd']:
            print(given_answer.lower())
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
            print('Correct! Well done.')
            self.update_score()
        else:
            print('Incorrect')
        print(self.score)


def take_quiz():
    """
    Start the quiz. Get answer, give feedback and show next question.
    """
    #Create an instance of the user class.
    user = User()
    for i in range(3):
        user.show_question(i)
        user.validate_answer(user.given_answer)
        user.evaluate_answer(i, user.given_answer)
    print(f'You have answered {user.score} questions out of {len(qsns)}.')


take_quiz()
