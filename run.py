from questions import questionBank

print('Welcome')
print('SDG Quiz')

# Create a list of question dictionaries.
qsns = questionBank()
score = 0


class User:
    """"
    Defines users
    """
    def __init__(self):
        """
        Get username to initialize name 
        """
        self.name = input('Enter your name:\n')


def get_user():
    """
    Create an instance of the user class.
    """
    user = User()
    return user


def update_score():
    """
    Increment score if the answer is correct
    """
    global score
    score += 1
    return score


def show_question(i):
    """
    Display question prompt and choices.
    """
    print(qsns[i]['question'])
    print(qsns[i]['options'])


def validate_answer(ans):
    """
    Get answer from user and validate.
    Input answer can only be one of a, b, c or d.
    Change input to lower case and look it up in the list.
    """
    if ans.lower() not in ['a', 'b', 'c', 'd']:
        print(ans.lower())
        print('You answer should be one of: a, b, c or d')
        ans = input('Try again.\n')
    return ans


def evaluate_answer(qsn, ans):
    """
    Get the current question number and the current answer.
    Compare it with corrent answer for the given question.
    Display feedback and if answer is correct, increment score.
    """
    if ans.upper() == qsns[qsn]['answer']:
        print('Correct! Well done.')
        update_score()
    else:
        print('Incorrect')
    print(score)


def take_quiz():
    """
    Start the quiz. Get answer, give feedback and show next question.
    """
    get_user()
    for i in range(len(qsns)):
        show_question(i)
        ans = input('You answer:\n')
        validate_answer(ans)
        evaluate_answer(i, ans)
    print(f'You have answered {score} questions out of {len(qsns)}.')


take_quiz()
