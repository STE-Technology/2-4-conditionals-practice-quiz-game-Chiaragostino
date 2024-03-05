"""
File: quiz.py
Author: Chiara A
Date: 2024/02/01
Description: This program is a multiple quiz game!
"""

print("Multiple choice quiz game!\n")

total_questions = 4
questions_correct = 0

question_one = input("What is my nick name?: \na) Chiara \nb) kiki \nc) chichi \nd) ki \n")

if question_one == "b" or question_one == "B":
    print("Correct!\n")
    questions_correct = questions_correct + 1
else:
    print("Incorrect, the answer is kiki.\n")

question_two = input("\nWhat year was I born?: \na) 2008 \nb) 2006 \nc) 2007 \nd) 2005 \n")

if question_two == "c" or question_one == "C":
    print("Correct!\n")
    questions_correct = questions_correct + 1
else:
    print("Incorrect, the answer is 2007.\n")

question_three = input("What is my favourite number?: \na) 8 \nb) 11 \nc) 18 \nd) 14\n")

if question_three == "a" or question_three == "A":
    print("Correct!\n")
    questions_correct = questions_correct + 1
else:
    print("Incorrect, the answer is 8.\n")

question_four = input("What is my dogs name?: \na) Kernel \nb) Goldie \nc) Popcorn \nd) George\n")

if question_four == "c" or question_four == "C":
    print("Correct!\n")
    questions_correct = questions_correct + 1
else:
    print("Incorrect, the answer is popcorn.\n")

total_score = questions_correct / total_questions * 100 
rounded_score = round(total_score ,2)


print("Quiz complete!")
print("You answered" , questions_correct , "questions out of 4 correct! You scored a " , rounded_score , "% !")