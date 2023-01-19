import questions


MAIN_DISCIPLINES = ['stats', 'linear_algebra', 'machine_learning', 'programming']

    
if __name__=='__main__':
    
    questions._initialize_questions()

    # Will replace this with tkinter gui later.
    choice = input('Would you like to (1) add/remove a question or be (2) asked a question? ')
    if choice in ['1']:
        choice = input('Would you like to (1) Add or (2) Remove questions? ')
        if choice in ['1']:
            while True:
                discipline = input('What is the discipline (stats, linear_algebra, machine_learning, programming) for the question? Type "quit" if you want to stop adding questions. ')
                if discipline in MAIN_DISCIPLINES:
                    topic = input('What is the topic? ')
                    question = input('What is the question? ')
                    answer = input('What is the answer? ')
                    questions.add_question(discipline, topic, question, answer)
                elif discipline in ['quit']:
                    break
                else: 
                    print('That is not a valid discipline. Try again.')
        elif choice in ['2']:
            discipline = input('From which discipline do you want to remove a question? ')
            indices = input('What are the indices of the questions you want to remove (separate choices with a space)? ')
            questions.remove_question(discipline, indices)
    
    if choice in ['2']:
        discipline = input('Which discipline do you want to be tested on? ')
        print(questions.get_random_question(discipline))