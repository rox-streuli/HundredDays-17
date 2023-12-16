from question_model import Question
from data import question_data, question_data_computers
from quiz_brain import QuizBrain

question_bank = []

# for item in question_data:
#     question_bank.append(Question(q_text=item['text'], q_answer=item['answer']))
#
# quiz = QuizBrain(question_bank)

for item in question_data_computers:
    question_bank.append(Question(q_text=item['question'], q_answer=item[
        'correct_answer']))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz!")
print(f"your final score was: {quiz.score}/{quiz.q_num}")
