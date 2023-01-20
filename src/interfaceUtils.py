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

def clear_button(responses):
    for response in responses:
        try:
            response.delete(0, tk.END)
        except:
            # To catch clearing tkinter textbox
            response.delete('1.0', tk.END)

    return None


class questionAsker:
    '''
    A class that provides functionality to all the buttons involved in asking a question.
    '''
    def __init__(self):
        self.discipline = ''
        self.topic = ''
        self.question = ''
        self.answer = ''

    def _set_discipline(self, ask_discipline_entry):
        self.discipline = ask_discipline_entry.get()
        return None


    def _get_random_question(self):
        self.topic, self.question, self.answer = questions.get_random_question(self.discipline)
        return None

    
    def _output_random_question(self, ask_topic_text, ask_question_text):
        
        ask_topic_text.delete('1.0', tk.END)
        ask_topic_text.insert('1.0', self.topic[0])
    
        ask_question_text.delete('1.0', tk.END)
        ask_question_text.insert('1.0', self.question[0])
        
        return None


    def _output_random_answer(self, ask_real_answer_text):
        
        ask_real_answer_text.delete('1.0', tk.END)
        ask_real_answer_text.insert('1.0', self.answer[0])
        
        return None

    def question_button_function(self, ask_discipline_entry, ask_topic_text, ask_question_text):
        self._set_discipline(ask_discipline_entry)
        self._get_random_question()
        self._output_random_question(ask_topic_text, ask_question_text)

        return None

    def real_answer_button_function(self, ask_real_answer_text):
        self._output_random_answer(ask_real_answer_text)

