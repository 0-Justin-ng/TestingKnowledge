import tkinter as tk
import questions
import interfaceUtils

def gui_loop():
    # Make the root window.
    root = tk.Tk()
    root.title('Test My Knowledge')
    w, h = (900, 600)
    root.geometry(f'{w}x{h}')

    # Create the major frames. 
    add_question_frame = tk.LabelFrame(
        root, 
        text='Add a Question', 
        width=450, height=300,
        pady = 3
        )

    remove_question_frame = tk.LabelFrame(
        root,
        text='Remove a Question',
        width=450, height = 300,
        pady=3
    )

    ask_question_frame = tk.LabelFrame(
        root,
        text='Test Your Knowledge',
        width=450, height = 600,
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
    add_answer_entry = tk.Entry(add_question_frame)

    add_question_button = tk.Button(
        add_question_frame, 
        text='Add Question',
        command=lambda: interfaceUtils.store_question(
            add_discipline_entry, add_topic_entry,
            add_question_entry, add_answer_entry
            )
    )

    add_clear_button = tk.Button(
        add_question_frame,
        text='Clear',
        command=lambda: interfaceUtils.clear_button(
            [add_discipline_entry, add_topic_entry,
            add_question_entry, add_answer_entry]
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
    add_answer_entry.grid(row=3,column=1) 

    add_question_button.grid(row=4, column=0)
    add_clear_button.grid(row=4, column=1)


    root.mainloop()