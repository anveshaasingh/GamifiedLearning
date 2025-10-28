
  from typing import List, Dict

def init_levels() -> List[Dict]:
    levels = [
        {
            "title": "Library Gate",
            "narrative": "The gatekeeper tests your knowledge of data structures.",
            "question": {
                "prompt": "Which data structure follows LIFO?",
                "choices": ["Queue", "Stack", "Tree", "Graph"],
                "answer": 1,
                "hint": "Plates in a stack."
            }
        },
        {
            "title": "Hall of Loops",
            "narrative": "A corridor filled with repeating symbols challenges you.",
            "question": {
                "prompt": "Index of the 3rd element in a 0-based array?",
                "choices": ["1", "2", "3", "0"],
                "answer": 1,
                "hint": "Start from 0."
            }
        },
        {
            "title": "Bridge of Functions",
            "narrative": "Answer a question about function keywords.",
            "question": {
                "prompt": "Which keyword returns a value from a function in C?",
                "choices": ["break", "goto", "return", "continue"],
                "answer": 2,
                "hint": "It sends the result back."
            }
        },
        {
            "title": "Door of Recursion",
            "narrative": "A whisper asks about recursion...",
            "question": {
                "prompt": "What must every recursive function have?",
                "choices": ["A print statement", "A base case", "A loop", "A pointer"],
                "answer": 1,
                "hint": "To stop infinite calling."
            }
        },
        {
            "title": "Tunnel of Sorting",
            "narrative": "You face sorting algorithms written in stone.",
            "question": {
                "prompt": "Which has O(n log n) average time?",
                "choices": ["Bubble", "Insertion", "Quick", "Selection"],
                "answer": 2,
                "hint": "Divide and conquer."
            }
        },
        {
            "title": "Cave of Arrays",
            "narrative": "An echo asks about arrays.",
            "question": {
                "prompt": "What does array index start with in C?",
                "choices": ["1", "0", "-1", "Depends on compiler"],
                "answer": 1,
                "hint": "Computer counting starts from..."
            }
        },
        {
            "title": "Maze of Memory",
            "narrative": "A ghost asks about memory management.",
            "question": {
                "prompt": "Which function frees allocated memory in C?",
                "choices": ["delete", "free", "malloc", "clear"],
                "answer": 1,
                "hint": "Opposite of malloc."
            }
        },
        {
            "title": "Pyramid of Pointers",
            "narrative": "You must identify pointer basics.",
            "question": {
                "prompt": "What does a pointer store?",
                "choices": ["A variable", "A value", "An address", "A function"],
                "answer": 2,
                "hint": "Memory location of variable."
            }
        },
        {
            "title": "Valley of Variables",
            "narrative": "Choose the correct statement about variables.",
            "question": {
                "prompt": "Which keyword defines constants in C?",
                "choices": ["const", "static", "define", "final"],
                "answer": 0,
                "hint": "Starts with 'c'."
            }
        },
        {
            "title": "Final Door",
            "narrative": "The last door glows with golden code.",
            "question": {
                "prompt": "Which concept allows same function name with different arguments?",
                "choices": ["Inheritance", "Polymorphism", "Encapsulation", "Overloading"],
                "answer": 3,
                "hint": "Function over..."
            }
        }
    ]

    return levels
