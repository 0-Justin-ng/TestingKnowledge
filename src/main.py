import questions
import interface

MAIN_DISCIPLINES = ['stats', 'linear_algebra', 'machine_learning', 'programming']

    
if __name__=='__main__':
    
    questions._initialize_questions()
    interface.gui_loop()
    