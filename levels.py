from typing import List, Dict
import random

def init_levels() -> List[Dict]:
    levels = [
        # --- C BASICS ---
        {
            "title": "Basics of C",
            "narrative": "You start your journey by revising the fundamentals of C language.",
            "question": {
                "prompt": "Which symbol is used to end a statement in C?",
                "choices": [":", ";", ".", ","],
                "answer": 1,
                "hint": "It’s like a period for code lines."
            }
        },
        {
            "title": "Data Types",
            "narrative": "Understand the basic building blocks of data.",
            "question": {
                "prompt": "Which data type is used to store characters in C?",
                "choices": ["char", "string", "int", "float"],
                "answer": 0,
                "hint": "It stores single letters like 'A'."
            }
        },
        {
            "title": "Constants",
            "narrative": "A glowing book asks you about constants.",
            "question": {
                "prompt": "Which keyword defines constants in C?",
                "choices": ["const", "define", "static", "fixed"],
                "answer": 0,
                "hint": "Starts with letter 'c'."
            }
        },
        # --- LOOPS & CONDITIONS ---
        {
            "title": "Conditional Cave",
            "narrative": "Decide your path using conditional logic.",
            "question": {
                "prompt": "Which statement is used for decision-making in C?",
                "choices": ["switch", "if", "goto", "case"],
                "answer": 1,
                "hint": "It checks true or false."
            }
        },
        {
            "title": "Loop Land",
            "narrative": "Endless loops surround you.",
            "question": {
                "prompt": "Which loop executes at least once?",
                "choices": ["for", "while", "do-while", "foreach"],
                "answer": 2,
                "hint": "Condition checked after running once."
            }
        },
        {
            "title": "Nested Logic",
            "narrative": "Deeper loops await your logic.",
            "question": {
                "prompt": "What keyword skips current iteration in a loop?",
                "choices": ["break", "stop", "exit", "continue"],
                "answer": 3,
                "hint": "It continues to the next iteration."
            }
        },
        # --- FUNCTIONS & RECURSION ---
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
            "title": "Scope Zone",
            "narrative": "Variables vanish outside their scope.",
            "question": {
                "prompt": "What is the lifetime of a static variable?",
                "choices": ["Until block ends", "Until program ends", "Until function call ends", "Until memory full"],
                "answer": 1,
                "hint": "It retains value even after function ends."
            }
        },
        # --- ARRAYS & STRINGS ---
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
            "title": "String Steps",
            "narrative": "The path is paved with characters.",
            "question": {
                "prompt": "Which library function is used to copy one string to another?",
                "choices": ["strcpy()", "copy()", "strcopy()", "strcat()"],
                "answer": 0,
                "hint": "Starts with 'str' and means copy."
            }
        },
        {
            "title": "Array Arena",
            "narrative": "You face multi-dimensional challenges.",
            "question": {
                "prompt": "What is the correct way to declare a 2D array in C?",
                "choices": ["int arr[2,3];", "int arr[2][3];", "array int[2][3];", "int arr{2}{3};"],
                "answer": 1,
                "hint": "Use square brackets twice."
            }
        },
        # --- MEMORY & POINTERS ---
        {
            "title": "Memory Maze",
            "narrative": "Memory spirits ask about pointers.",
            "question": {
                "prompt": "Which operator gives the address of a variable in C?",
                "choices": ["*", "&", "%", "#"],
                "answer": 1,
                "hint": "Used before a variable name."
            }
        },
        {
            "title": "Pointer Peak",
            "narrative": "Pointers and addresses everywhere!",
            "question": {
                "prompt": "If int *p, a=10; what does *p give?",
                "choices": ["Address of a", "Value of a", "Error", "NULL"],
                "answer": 1,
                "hint": "*p dereferences the pointer."
            }
        },
        {
            "title": "Dynamic Dungeon",
            "narrative": "A voice echoes: memory management is key.",
            "question": {
                "prompt": "Which function is used to allocate memory in C?",
                "choices": ["alloc()", "malloc()", "create()", "mem()"],
                "answer": 1,
                "hint": "Stands for memory allocation."
            }
        },
        {
            "title": "Memory Management",
            "narrative": "Free the trapped bytes.",
            "question": {
                "prompt": "Which function frees allocated memory in C?",
                "choices": ["delete", "free", "malloc", "clear"],
                "answer": 1,
                "hint": "Opposite of malloc."
            }
        },
        # --- DATA STRUCTURES ---
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
            "title": "Queue Quest",
            "narrative": "Orderly lines test your patience.",
            "question": {
                "prompt": "Which data structure follows FIFO?",
                "choices": ["Queue", "Stack", "Array", "Tree"],
                "answer": 0,
                "hint": "First come, first serve."
            }
        },
        {
            "title": "Tree Trail",
            "narrative": "Branches of data spread before you.",
            "question": {
                "prompt": "What is the topmost node of a tree called?",
                "choices": ["Leaf", "Root", "Parent", "Node"],
                "answer": 1,
                "hint": "Like the root of a plant."
            }
        },
        {
            "title": "Graph Gateway",
            "narrative": "Interconnected paths challenge you.",
            "question": {
                "prompt": "Which traversal uses a queue in graphs?",
                "choices": ["DFS", "BFS", "Inorder", "Postorder"],
                "answer": 1,
                "hint": "Breadth before depth."
            }
        },
        # --- OOP CONCEPTS ---
        {
            "title": "OOP Origin",
            "narrative": "You enter the land of Object-Oriented Programming.",
            "question": {
                "prompt": "Which concept hides data and functions into one unit?",
                "choices": ["Polymorphism", "Encapsulation", "Inheritance", "Abstraction"],
                "answer": 1,
                "hint": "It means wrapping data."
            }
        },
        {
            "title": "Inheritance Island",
            "narrative": "You inherit the wisdom of your ancestors.",
            "question": {
                "prompt": "Which concept allows reusing code in OOP?",
                "choices": ["Encapsulation", "Inheritance", "Abstraction", "Overloading"],
                "answer": 1,
                "hint": "Parent-child relationship."
            }
        },
        {
            "title": "Polymorphism Palace",
            "narrative": "One name, many forms.",
            "question": {
                "prompt": "Which concept allows same function name with different arguments?",
                "choices": ["Encapsulation", "Inheritance", "Polymorphism", "Overloading"],
                "answer": 3,
                "hint": "Function over..."
            }
        },
        {
            "title": "Abstraction Arena",
            "narrative": "Simplify the complex details.",
            "question": {
                "prompt": "Which OOP concept focuses on showing only essential details?",
                "choices": ["Encapsulation", "Abstraction", "Inheritance", "Polymorphism"],
                "answer": 1,
                "hint": "It hides unnecessary details."
            }
        }
    ]

    # ✅ Randomize question order
    random.shuffle(levels)

    # ✅ Randomize answer options inside every question
    for level in levels:
        q = level["question"]
        choices = q["choices"]
        correct_index = q["answer"]

        paired = [(c, i == correct_index) for i, c in enumerate(choices)]
        random.shuffle(paired)
        q["choices"] = [x[0] for x in paired]
        q["answer"] = [i for i, (_, correct) in enumerate(paired) if correct][0]

    return levels

  
