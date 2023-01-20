import tkinter as tk
import interfaceUtils

def gui_loop():
    # Make the root window.
    root = tk.Tk()
    root.title('Test My Knowledge')
    w, h = (900, 800)
    root.geometry(f'{w}x{h}')

    # Create the major frames. 
    add_question_frame = tk.LabelFrame(
        root, 
        text='Add a Question', 
        width=400, height=300,
        pady = 3
        )

    remove_question_frame = tk.LabelFrame(
        root,
        text='Remove a Question',
        width=400, height = 300,
        pady=3
    )

    ask_question_frame = tk.LabelFrame(
        root,
        text='Test Your Knowledge',
        width=500, height = 600,
        pady=3
    )

    # Layout major frames.
    add_question_frame.grid(row=0, column = 0)
    remove_question_frame.grid(row=1, column = 0)
    ask_question_frame.grid(row = 0, column = 1, rowspan = 2)

    # Create widgets for the 'add questions' frame.
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


    # Layout all the widgets in the 'add questions' frame.
    add_discipline_label.grid(row=0,column=0, sticky= tk.W)  
    add_topic_label.grid(row=1,column=0, sticky= tk.W)  
    add_question_label.grid(row=2,column=0, sticky= tk.W)  
    add_answer_label.grid(row=3,column=0, sticky= tk.W)  

    add_discipline_entry.grid(row=0,column=1) 
    add_topic_entry.grid(row=1,column=1) 
    add_question_entry.grid(row=2,column=1) 
    add_answer_text.grid(row=3,column=1) 

    add_question_button.grid(row=4, column=0)
    add_clear_button.grid(row=4, column=1)

    # Create widgets for ask question.
    ask_discipline_label = tk.Label(ask_question_frame, text='Discipline:')
    ask_entry_label = tk.Label(ask_question_frame, text='Your Answer:')
    
    ask_discipline_entry = tk.Entry(ask_question_frame)
    ask_answer_text = tk.Text(ask_question_frame)

    ask_real_answer_text = tk.Text(ask_question_frame)
    ask_real_answer_text.config(state=tk.DISABLED)

    ask_check_answer_button = tk.Button(ask_question_frame, text='Check Answer')
    ask_clear_button = tk.Button(
        ask_question_frame,
        text='Clear',
        command=lambda: interfaceUtils.clear_button(
            [ask_discipline_entry, ask_answer_text, ask_real_answer_text]
            )
    )

    # Layout of ask question frame.
    ask_discipline_label.grid(row=0, column=0, sticky=tk.W)
    ask_entry_label.grid(row=1, column=0, sticky=tk.W)
    ask_discipline_entry.grid(row=0, column=1, sticky=tk.W)
    ask_answer_text.grid(row=1, column=1)
    ask_check_answer_button.grid(row=2, column=0)
    ask_real_answer_text.grid(row=2, column=1)
    ask_clear_button.grid(row=3, column=0)

    root.mainloop()