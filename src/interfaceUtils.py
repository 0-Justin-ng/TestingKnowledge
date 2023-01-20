import questions
import tkinter as tk


def parse_questions(discipline, topic, question, answer):
    discipline_response = discipline.get()
    topic_response = topic.get()
    question_response = question.get()
    answer_response = answer.get()

    print(discipline_response, topic_response, question_response, answer_response)
    return discipline_response, topic_response, question_response, answer_response

def store_question(discipline, topic, question, answer):
    responses = parse_questions(discipline, topic, question, answer)
    questions.add_question(responses)
    return None

def clear_button(responses):
    for response in responses:
        try:
            response.delete(0, tk.END)
        except:
            # To catch clearing tkinter textbox
            response.delete('1.0', tk.END)

    return None