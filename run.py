# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from questions import questionBank

print('Welcome')
print('SDG Quiz')

name = input('Enter your name:\n')

print(f'Your name is: {name}')

# Create a list of question dictionaries.
qsns = questionBank()
score = 0

def check_answer(qsn, ans):
    """
    Get the current question number and the current answer.
    Compare it with corrent answer for the given question.
    Display feedback and if answer is correct, increment score.
    """
    if ans == qsns[qsn]['answer']:
        print('Correct! Well done.')
        score += 1
    else:
        print('Incorrect')
        score += 0
    return score


for i in range(len(qsns)):
    print(qsns[i]['question'])
    print(qsns[i]['options'])
    ans = input('You answer:\n')
    check_answer(i, ans)
print(answer)



