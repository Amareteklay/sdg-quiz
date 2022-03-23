# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from questions import questionBank

print('Welcome')
print('SDG Quiz')

name = input('Enter your name:\n')
print(f'Hello: {name}!')

# Create a list of question dictionaries.
qsns = questionBank() 
score = 0

def update_score():
    """ 
    Increment score if the answer is correct
    """
    global score
    score += 1
    return score

def check_answer(qsn, ans):
    """
    Get the current question number and the current answer.
    Compare it with corrent answer for the given question.
    Display feedback and if answer is correct, increment score.
    """
    if ans == qsns[qsn]['answer']:
        print('Correct! Well done.')
        update_score()
    else:
        print('Incorrect')
    print(score)

def take_quiz():
    """
    Start the quiz. Get answer, give feedback and show next question.
    """
    for i in range(len(qsns)):
        print(qsns[i]['question'])
        print(qsns[i]['options'])
        ans = input('You answer:\n')
        check_answer(i, ans)
    print(f'You have answered {score} questions out of {len(qsns)}.')


take_quiz()
