import random

from questions import questions
from analysis import analyze_results
from visualization import show_graph

score = 0
results = []
user_answers = []

print("===== QUIZ ASSESSMENT SYSTEM =====\n")

random.shuffle(questions)

for i, q in enumerate(questions):

    print(f"Question {i+1}: {q['question']}")

    for opt in q["options"]:
        print(opt)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    user_answers.append(user_answer)

    if user_answer == q["answer"]:
        print("Correct!\n")
        score += 1
        results.append(1)

    else:
        print(f"Wrong! Correct answer is {q['answer']}\n")
        results.append(0)

total = len(questions)
percentage = (score / total) * 100

print("\n===== RESULT =====")
print(f"Score: {score}/{total}")
print(f"Percentage: {percentage:.2f}%")

if percentage >= 75:
    performance = "Excellent"

elif percentage >= 50:
    performance = "Good"

else:
    performance = "Needs Improvement"

print("Performance:", performance)

analyze_results(total, user_answers, results)

show_graph(results)
