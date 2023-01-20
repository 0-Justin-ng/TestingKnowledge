import questions
import tkinter as tk


def parse_questions(discipline, topic, question, answer):
    discipline_response = discipline.get()
    topic_response = topic.get()
    question_response = question.get()
    answer_response = answer.get('1.0', tk.END)

    print(discipline_response, topic_response, question_response, answer_response)
    return discipline_response, topic_response, question_response, answer_response


def store_question(discipline, topic, question, answer):
    responses = parse_questions(discipline, topic, question, answer)
    questions.add_question(responses)
    return None


def output_random_question(discipline_response, ask_topic_text, ask_question_text):
    discipline = discipline_response.get()
    topic, question, answer = questions.get_random_question(discipline)
    
    ask_topic_text.delete('1.0', tk.END)
    ask_topic_text.insert('1.0', topic[0])
   
    ask_question_text.delete('1.0', tk.END)
    ask_question_text.insert('1.0', question[0])
    
    print(topic, question, answer)
    return(topic, question, answer)


def output_random_answer(random_question_info, ask_real_answer_text):
    answer = random_question_info[0][2]
   
    ask_real_answer_text.delete('1.0', tk.END)
    ask_real_answer_text.insert('1.0', answer[0])
    
    return None



def clear_button(responses):
    for response in responses:
        try:
            response.delete(0, tk.END)
        except:
            # To catch clearing tkinter textbox
            response.delete('1.0', tk.END)

    return None