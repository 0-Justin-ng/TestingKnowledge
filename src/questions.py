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
path_to_questions = p / 'questions'

def _initialize_questions():
    # Sets up question csvs to start storing questions. 
    if len(os.listdir(path_to_questions)) < 4:
        for discipline in MAIN_DISCIPLINES:
            discipline_path = path_to_questions / f'{discipline}.csv'
            with open(discipline_path, 'a') as file_object:
                writer_object = writer(file_object)
                writer_object.writerow(INITIAL_ROW)

def _get_csv_filepath(discipline):
    file_path = path_to_questions / discipline 
    return f'{file_path}.csv'
   
def add_question(discipline, topic, question, answer):

    file_path = _get_csv_filepath(discipline)

    df = pd.read_csv(file_path)
    index = len(df)

    row = [index, topic, question, answer]
    with open(file_path, 'a') as file_object:
        
        # Pass file object into csv.writer()
        writer_object = writer(file_object)

        # Write the rows into the writer_object.writerow()
        writer_object.writerow(row)

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

    print(len(df))

    random_index = randint(0, len(df)-1)

    random_question = df.iloc[[random_index]] # Returns a series. 

    topic = random_question['topic'].values
    question = random_question['question'].values
    answer = random_question['answer'].values
    
    return topic, question, answer





        

