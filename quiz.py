#!/bin/python3
import docx
import random
import os

def generate_quiz(doc_path):
    doc = docx.Document(doc_path)
    quiz = []

    table = doc.tables[0]  # Assuming the table is the first one in the document

    for row in table.rows[1:]:  # Skip the header row
        question_number = row.cells[0].text.strip()
        question_text = row.cells[1].text.strip()
        answer = row.cells[2].text.strip()

        options = []
        for cell in row.cells[3:]:
            option = cell.text.strip()
            if option:
                options.append(option)

        quiz.append({
            'number': question_number,
            'question': question_text,
            'answer': answer,
            'options': options
        })

    return quiz

def generate_random_options(correct_option, options):
    # Remove empty options if any
    options = [option for option in options if option]

    # Check if the correct option is not empty and if options are available
    if correct_option and options:
        # Shuffle the options
        random.shuffle(options)

        # Find the index of the correct option
        correct_index = options.index(correct_option)

        # Adjust the options to maintain the correct answer position
        options.insert(0, options.pop(correct_index))

    return options

def print_quiz(quiz):
    for question in quiz:
        print(f"Question {question['number']}:")
        print(question['question'])
        print("Options:")
        options = generate_random_options(question['answer'], question['options'])
        for i, option in enumerate(options):
            print(f"{chr(65 + i)}) {option}")
        print()


def take_quiz(quiz):
    random.shuffle(quiz)
    score = 0
    total_questions = len(quiz)
    current_question = 0

    while current_question < total_questions:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
        question = quiz[current_question]
        print(f"Question {question['number']}:")
        print(question['question'])
        print("Options:")

        options = generate_random_options(question['answer'], question['options'])
        for i, option in enumerate(options):
            if option == question['answer']:
                print(f"\033[92m{chr(65 + i)}) {option}\033[0m")  # Green color for correct answer
            else:
                print(f"\033[91m{chr(65 + i)}) {option}\033[0m")  # Red color for incorrect answers

        user_answer = input("Your answer (enter A, B, C, D, P for previous, or N for next): ")

        if user_answer.upper() == 'P':
            current_question -= 1
            if current_question < 0:
                current_question = 0
            continue
        elif user_answer.upper() == 'N':
            current_question += 1
            if current_question >= total_questions:
                current_question = total_questions - 1
            continue

        if user_answer.upper() == question['answer']:
            print("\n\033[92mCorrect!\033[0m")
            score += 1
        else:
            print(f"\n\033[91mIncorrect. The correct answer is {question['answer']}.\033[0m")

        input("Press Enter to continue...")
        current_question += 1

    print(f"Quiz completed! Your score: {score}/{total_questions}")

quiz = generate_quiz('mis2.docx')
take_quiz(quiz)

