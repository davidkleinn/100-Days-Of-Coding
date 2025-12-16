from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []

for question in question_data:
    txt = question["text"]
    ans = question["answer"]
    new_q = Question(txt, ans)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.has_questions():
    quiz.next_q()

print("you've done it")
print(f"final score is: {quiz.score_tracker}/{quiz.q_num}")
print("\n")