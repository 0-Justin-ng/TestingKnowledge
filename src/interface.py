import tkinter as tk
import interfaceUtils

def gui_loop():
    # Make the root window.
    root = tk.Tk()
    root.title('Test My Knowledge')
    w, h = (1100, 600)
    root.geometry(f'{w}x{h}')

    # Create the major frames__________________________________________________ 
    add_question_frame = tk.LabelFrame(
        root, 
        text='Add a Question', 
        width=w/2, height=h/2,
        pady = 3
        )

    remove_question_frame = tk.LabelFrame(
        root,
        text='Remove a Question',
        width=w/2, height = h/2,
        pady=3
    )

    ask_question_frame = tk.LabelFrame(
        root,
        text='Test Your Knowledge',
        width=w/2, height = h,
        pady=3
    )

    # Layout major frames_______________________________________________________
    add_question_frame.grid(row=0, column = 0, sticky=tk.NW)
    remove_question_frame.grid(row=1, column = 0)
    ask_question_frame.grid(row = 0, column = 1, rowspan = 2, sticky=tk.NE)
   

    # Create widgets for the 'add questions' frame.______________________________
    add_discipline_label = tk.Label(add_question_frame, text='Discipline:')
    add_topic_label = tk.Label(add_question_frame, text='Topic:')
    add_question_label = tk.Label(add_question_frame, text='Question:')
    add_answer_label = tk.Label(add_question_frame, text='Answer:')

    add_discipline_entry = tk.Entry(add_question_frame)
    add_topic_entry = tk.Entry(add_question_frame)
    add_question_entry = tk.Entry(add_question_frame)
    add_answer_text = tk.Text(add_question_frame)

    add_question_button = tk.Button(
        add_question_frame, 
        text='Add Question',
        command=lambda: interfaceUtils.store_question(
            add_discipline_entry, add_topic_entry,
            add_question_entry, add_answer_text
            )
    )

    add_clear_button = tk.Button(
        add_question_frame,
        text='Clear',
        command=lambda: interfaceUtils.clear_button(
            [add_discipline_entry, add_topic_entry,
            add_question_entry, add_answer_text]
            )
    )


    # Layout all the widgets in the 'add questions' frame
    add_discipline_label.grid(row=0,column=0, sticky= tk.W)  
    add_topic_label.grid(row=1,column=0, sticky= tk.W)  
    add_question_label.grid(row=2,column=0, sticky= tk.W)  
    add_answer_label.grid(row=3,column=0, sticky= tk.NW)  

    add_discipline_entry.grid(row=0,column=1, sticky= tk.W) 
    add_topic_entry.grid(row=1,column=1, sticky= tk.W) 
    add_question_entry.grid(row=2,column=1, sticky= tk.W) 
    add_answer_text.grid(row=3,column=1, sticky= tk.W) 

    add_question_button.grid(row=4, column=0, sticky= tk.W)
    add_clear_button.grid(row=4, column=1, sticky= tk.W)
    
    # ____________________________________________________________________________
    # Create widgets for ask question.
    ask_discipline_label = tk.Label(ask_question_frame, text='Discipline:')
    ask_topic_label = tk.Label(ask_question_frame, text='Topic: ')
    ask_question_label = tk.Label(ask_question_frame, text='Question:')
    ask_entry_label = tk.Label(ask_question_frame, text='Your Answer:')
    ask_real_answer_label = tk.Label(ask_question_frame, text='Real Answer:')

    ask_discipline_entry = tk.Entry(ask_question_frame)
    ask_topic_text = tk.Text(ask_question_frame)
    ask_question_text = tk.Text(ask_question_frame)
    ask_answer_text = tk.Text(ask_question_frame)

    
    question_asker = interfaceUtils.questionAsker() # Stores the data for the random question.
    
    ask_get_random_button = tk.Button(
        ask_question_frame, text='Random Question', 
        command=lambda: question_asker.question_button_function(
            ask_discipline_entry, ask_topic_text, ask_question_text
        )
    )
    
    ask_check_answer_button = tk.Button(
        ask_question_frame, text='Check Answer',
        command=lambda: question_asker.real_answer_button_function(
            ask_real_answer_text
        )
    )

    ask_clear_button = tk.Button(
        ask_question_frame,
        text='Clear',
        command=lambda: interfaceUtils.clear_button(
            [ask_discipline_entry, ask_topic_text,
            ask_question_text, ask_answer_text, 
            ask_real_answer_text]
            )
    )

    ask_real_answer_text = tk.Text(ask_question_frame)
  
  
    # Layout for ask question frame.
    ask_discipline_label.place(x=5, y=5)
    ask_discipline_entry.place(x=100,y=5)
    ask_get_random_button.place(x=225, y=0)

    ask_topic_label.place(x=5, y=30)
    ask_topic_text.place(x=100, y=30, height=75, width = 400)

    ask_question_label.place(x=5, y=55)
    ask_question_text.place(x=100, y=55, height=75, width = 400)

    ask_entry_label.place(x=5, y= 80)
    ask_answer_text.place(x=100, y=80, height=200, width=400)

    ask_check_answer_button.place(x=5, y= 285)
    ask_clear_button.place(x=105,y=285)

    ask_real_answer_label.place(x=5, y=315)
    ask_real_answer_text.place(x=100, y=315, height = 200, width=400)
    
    
    root.mainloop()