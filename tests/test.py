
import sys
from pathlib import Path

p = Path(__file__).parents[1] / 'src'
# Adds the path to src so we can import. 
print(p)
sys.path.insert(0, str(p))
print(sys.path)

import questions

# TODO Write actual tests for this section. 
def test_remove_questions():
    discipline = 'stats'
    indices = '1'
    return questions.remove_question(discipline, indices)


def test_get_random_question():
    discipline = 'stats'
    return questions.get_random_question(discipline)

def test_add_question():
    responses = [
        'stats',
        'test',
        'question',
        'answer'
    ]

    questions.add_question(responses)

test_add_question()