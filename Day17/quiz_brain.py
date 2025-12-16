#TODO: asking the questions
#TODO: checking if the answer was correct
#TODO: checking if we're the end of the quiz

from data import question_data

class QuizBrain:

    def __init__(self, q_list):
        self.score_tracker = 0
        self.q_num = 0
        self.q_list = q_list

    def next_q(self):
        current_question = self.q_list[self.q_num]
        self.q_num += 1

        while True:
            user_answer = input(f"Q.{self.q_num}: {current_question.text} (True/False): ")
            if user_answer.lower() in ["true", "false"]:
                break
            else:
                print("\n")
                print("invalid input")
                print("\n")
                
        self.check_answer(user_answer, current_question.answer)

    def has_questions(self):
        return self.q_num < len(question_data)
    
    def check_answer(self, user_answer, correct_answer):

        if user_answer.lower() == correct_answer.lower():
            self.score_tracker += 1
            print("\n")
            print("correct")
        else:
            print("\n")
            print("wrong")
        print(f"the answer was: {correct_answer}.")
        print(f"current score is: {self.score_tracker}/{self.q_num}")
        print("\n")


    


