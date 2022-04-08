"""
This module stores and provides the data required for
the quiz application.
Data are questions and notes and SDGs.
"""
# Import textwrap format notes printed on screen
import textwrap as tr
import time


def question_bank():
    """
    A function that stores and returns
    a list of dictionaries of questions
    """
    questions = [

        {'question': 'What does SDG stand for?',
         'choices': {
             'A': 'Sustainable Department Goals',
             'B': 'Sustainable Development Goals',
             'C': 'Sustainable Development Governance',
             'D': 'Sustainable Development Grants'},
         'answer': 'B'},

        {'question': 'When was the 2030 Agenda for Sustainable\
 Development adopted?',
         'choices': {
             'A': '2010',
             'B': '2015',
             'C': '2016',
             'D': '2020'},
         'answer': 'B'},

        {'question': 'How many SDGS are there?',
         'choices': {
             'A': 15,
             'B': 27,
             'C': 17,
             'D': 30},
         'answer': 'C'},

        {'question': 'Which is not a dimension of Sustainable Development?',
         'choices': {
             'A': 'Economic',
             'B': 'Social',
             'C': 'Environmental',
             'D': 'None'},
         'answer': 'D'},

        {'question': '''Goal 17 seeks to Strengthen the means of implementation and\n revitalize\
 the Global Partnership for Sustainable Development.\
\nWhat are these means of implementation?''',
         'choices': {
             'A': 'Finance',
             'B': 'Technology',
             'C': 'Capacity-building',
             'D': 'All'},
         'answer': 'D'},

        # 2 questions copied/adapted from https://quizizz.com/admin/quiz/\
        # 5c6c4413206101001a84dce7/sustainable-development-goals
        {'question': 'Which is not an obstacle to achieving the\
 Sustainable Development Goals?',
         'choices': {
             'A': 'Capital cities',
             'B': 'Differences in income',
             'C': 'Ecological problems',
             'D': 'Using more than we produce or grow'},
         'answer': 'A'},

        {'question': '''Which SDG aims to Conserve and sustainably use the\
 oceans, seas and marine\n resources for Sustainable Development?''',
         'choices': {
             'A': 'Life of land',
             'B': 'Life below water',
             'C': 'Climate action',
             'D': 'No poverty'},
         'answer': 'B'},

        {'question': 'Which statement is correct?',
         'choices': {
             'A': 'Sustainable development is the same as economic\
  development',
             'B': 'The 2030 Agenda for Sustainable Development has 17 goals\
  and 169 targets',
             'C': 'Each of the 17 goals in the SDGs has the same number of\
  targets',
             'D': 'Developed countries do not have to include SDGs in their\
  national policies because they are already developed'},
         'answer': 'B'},

        {'question': 'Which goal aims to achieve sustainable management and\
 efficient use of natural\n resources by 2030?',
         'choices': {
             'A': 'Climate actions',
             'B': 'Clean water and sanitation',
             'C': 'Responsible consumption and production',
             'D': 'Life on land'},
         'answer': 'C'},
        # Question adapted from\
        # https://www.statista.com/statistics/266138/climate-change-the-countries-with-the-highest-achievements/#:~:text=Based%20on%20the%202022%20Climate,climate%20protection%2C%20followed%20by%20Sweden.
        {'question': 'Based on the 2022 Climate Change Performance Index,\
 ______ was ranked\n as the country with the highest achievement in\
  climate protection,\n followed by _______.',
         'choices': {
             'A': 'Denmark, Sweden',
             'B': 'Sweden, Denmark',
             'C': 'Norway, Sweden',
             'D': 'Sweden, Norway'},
         'answer': 'A'}
    ]
    return questions


def sdg_note():
    """ A function to store and print a short note
    on and a list of the 17 SDGs.
    """
    notes = "The Sustainable Development Goals (SDGs), also known as the\
Global Goals, were adopted by the United Nations in 2015 as a\
universal call to action to end poverty, protect the planet,\
 and ensure that by 2030 all people enjoy peace and prosperity.\
The 17 SDGs are integrated—they recognize that action in one area will\
affect outcomes in others, and that development must balance social,\
economic and environmental sustainability."

    # Wrap text and print to fit the width constraint
    for note_line in tr.wrap(notes, width=78):
        print(note_line)

    time.sleep(3)
    # Print list of goals
    print('\n')
    print('''The 17 sustainable development goals (SDGs) to transform our world are:
    GOAL 1: No Poverty
    GOAL 2: Zero Hunger
    GOAL 3: Good Health and Well-being
    GOAL 4: Quality Education
    GOAL 5: Gender Equality
    GOAL 6: Clean Water and Sanitation
    GOAL 7: Affordable and Clean Energy
    GOAL 8: Decent Work and Economic Growth
    GOAL 9: Industry, Innovation and Infrastructure
    GOAL 10: Reduced Inequality
    GOAL 11: Sustainable Cities and Communities
    GOAL 12: Responsible Consumption and Production
    GOAL 13: Climate Action
    GOAL 14: Life Below Water
    GOAL 15: Life on Land
    GOAL 16: Peace and Justice Strong Institutions
    GOAL 17: Partnerships to achieve the Goal
    ''')
