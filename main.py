from logic import QuizLogic

Quiz = QuizLogic("testfragen.json")
test = Quiz.get_question()

print(test)