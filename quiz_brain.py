class QuizBrain:

    def __init__(self, q_list):
        self.q_num = 0
        self.question_bank = q_list
        self.score = 0

    def still_has_question(self):
        return self.q_num < len(self.question_bank)

    def next_question(self):
        """Retrieve item at the current question number from the
        question list.
        Use the input function to show the user the question text
        and ask for their choice.
        """
        current_question = self.question_bank[self.q_num]
        self.q_num += 1
        user_answer = input(f"Q.{self.q_num}: {current_question.text}"
                            f"(True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_choice, correct_answer):
        if user_choice.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print(f"That is wrong. The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.q_num}\n")
