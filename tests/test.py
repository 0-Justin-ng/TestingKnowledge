
import sys
from pathlib import Path

p = Path(__file__).parents[1] / 'src'
# Adds the path to src so we can import. 
print(p)
sys.path.insert(0, str(p))
print(sys.path)

from questions import remove_question, get_random_question


def test_remove_questions():
    discipline = 'stats'
    indices = '1'
    return remove_question(discipline, indices)


def test_get_random_question():
    discipline = 'stats'
    return get_random_question(discipline)
