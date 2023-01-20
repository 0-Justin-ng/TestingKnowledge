import pandas as pd 
from csv import writer

from random import randint 
from pathlib import Path
import os

MAIN_DISCIPLINES = ['stats', 'linear_algebra', 'machine_learning', 'programming']
INITIAL_ROW = ['index','topic', 'question', 'answer']

# Path creates a Path object that tracks where something is in the directory. 
# (__file__) specifies the path of where this python file is located. 
# parents return an iterable of paths each going one level higher in the current file path.
# /home/usr/TestingKnowledge/src , /home/usr/TestingKnowledge, /home/jng, /home, /
# Index at 1 to select a path one level up from the current directory where this file is located.
p = Path(__file__).parents[1]
PATH_TO_QUESTIONS = p / 'questions'


def _initialize_questions():
    # Sets up question csvs to start storing questions. 
    if len(os.listdir(PATH_TO_QUESTIONS)) < 4:
        for discipline in MAIN_DISCIPLINES:
            discipline_path = PATH_TO_QUESTIONS / f'{discipline}.csv'
            with open(discipline_path, 'a') as file_object:
                writer_object = writer(file_object)
                writer_object.writerow(INITIAL_ROW)

def _get_csv_filepath(discipline):
    file_path = PATH_TO_QUESTIONS / discipline 
    return f'{file_path}.csv'


def add_question(responses):

    discipline = responses[0]
    topic = responses[1]
    question = responses[2]
    # Need to strip extra whitespace from text field from tkinter.
    answer = responses[3].strip()

    file_path = _get_csv_filepath(discipline)

    df = pd.read_csv(file_path)
    
    # This is sets the correct initial index if there are no questions.
    if len(df.index.values) == 0:
        new_index = 0
    else:
        new_index=list(df.index.values)[-1] + 1

    df.loc[new_index] = [0, topic, question, answer]
    df['index'] = list(df.index.values)

    df.to_csv(file_path, index=False)
   
    return 'Done adding question.'


def remove_question(discipline, indices):

    indices = str.split(indices, ' ')

    file_path = _get_csv_filepath(discipline)
    df = pd.read_csv(file_path)

    for index in indices:
        df.drop(int(index), axis=0, inplace=True)

    df.to_csv(file_path, index=False)


def get_random_question(discipline):
    file_path = _get_csv_filepath(discipline)
    df = pd.read_csv(file_path)

    random_index = randint(0, len(df)-1)

    random_question = df.iloc[[random_index]] # Returns a series. 

    topic = random_question['topic'].values
    question = random_question['question'].values
    answer = random_question['answer'].values
    
    return topic, question, answer





        

