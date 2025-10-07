# levels.py
# Holds narrative + question definitions

from typing import List, Dict

MAX_LEVELS = 10

def init_levels() -> List[Dict]:
    levels = []

    levels.append({
        "title": "The Library Gate",
        "narrative": "You arrive at the ancient library. A riddling gatekeeper asks a test to prove your worth.",
        "question": {
            "prompt": "Which data structure uses LIFO (Last In, First Out)?",
            "choices": ["Queue", "Stack", "Tree", "Graph"],
            "answer": 1,
            "hint": "Think of stacking plates."
        }
    })

    levels.append({
        "title": "The Hall of Loops",
        "narrative": "A corridor full of looping murals blocks your path. A puzzle appears on the wall.",
        "question": {
            "prompt": "What is the 0-based index of the 3rd element in an array?",
            "choices": ["1", "2", "3", "0"],
            "answer": 1,
            "hint": "Start counting from 0."
        }
    })

    levels.append({
        "title": "Bridge of Functions",
        "narrative": "To cross the bridge you must answer how functions behave.",
        "question": {
            "prompt": "Which keyword in C is used to return a value from a function?",
            "choices": ["break", "goto", "return", "continue"],
            "answer": 2,
            "hint": "It's what you use to send the result back to caller."
        }
    })

    levels.append({
        "title": "The Final Door",
        "narrative": "A glowing door with a final question stands before you. Prove your mastery.",
        "question": {
            "prompt": "Which of these runs in O(n log n) average time for sorting?",
            "choices": ["Bubble Sort", "Insertion Sort", "Quick Sort", "Selection Sort"],
            "answer": 2,
            "hint": "Often uses divide and conquer."
        }
    })

    return levels
