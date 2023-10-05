# Python Quiz Generator

This Python script allows you to generate and take quizzes from a Microsoft Word document. It randomizes the order of questions, shuffles answer choices, and provides immediate feedback on your answers.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [How to Use](#how-to-use)
- [Sample Quiz Document](#sample-quiz-document)
- [License](#license)

## Features

- Reads quiz questions and answers from a Microsoft Word document.
- Randomizes the order of questions for a quiz experience.
- Provides immediate feedback on correct and incorrect answers.

## Technologies Used

- **Python 3**: The scripting language used to create the quiz generator.
- **python-docx**: A library for working with Microsoft Word (.docx) files in Python.

## How to Use

1. Ensure you have Python 3 installed on your system.

2. Install the required `python-docx` library if you haven't already:

   ```bash
   pip install python-docx
   ```

3. I have developed code with this design in mind, so try to check if it is the same or arrange as necessary

   ```
   | Question Number | Question Text | Correct Answer | Option A | Option B | Option C | Option D |
   |-----------------|--------------|----------------|----------|----------|----------|----------|
   | 1               | What is...   | A              | Option A | Option B | Option C | Option D |
   | 2               | How does...   | C              | Option A | Option B | Option C | Option D |
   ```
   
4. Run the script using the following command:

   ```bash
   python3 quiz_generator.py yourquizdocument.docx
   ```
   
5. Follow the on-screen instructions to take the quiz.
