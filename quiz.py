import colorama
from colorama import Fore, Back, Style

# Question
class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer

# Quiz
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(Fore.LIGHTBLUE_EX, f'Question {self.questionIndex + 1}: {question.text}', Style.RESET_ALL)

        for q in question.choices:
            print('- ' + q)

        answer = input('\nAnswer: ')
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print(Fore.LIGHTYELLOW_EX, '\nScore: ', self.score, Style.RESET_ALL)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print(Fore.LIGHTYELLOW_EX, 'Quiz ended.', Style.RESET_ALL)
        else:
            print(Fore.BLUE, f'Question {questionNumber} of {totalQuestion}'.center(100, '-'), Style.RESET_ALL)


q1 = Question('Which is the capital city of Türkiye?', ['İzmir', 'Hatay', 'İstanbul', 'Ankara', 'Antalya'], 'Ankara')
q2 = Question('What number cannot be written in Roman numerals?', ['All', '0', '10000', '1000000', 'None'], '0')
q3 = Question('What is the capital of the European Union?', ['Zürich', 'Berlin', 'Brussels', 'Vienna', 'Rome'], 'Brussels')
q4 = Question('Which country has more than one capital?', ['Italy', 'Singapore', 'North Macedonia', 'Andorra', 'South Africa'], 'South Africa')
q5 = Question('Where was the first international sports organization in which the Republic of Türkiye participated?', ['Amsterdam', 'London', 'Paris', 'Berlin', 'Zürich'], 'Paris')

questions = [q1, q2, q3, q4, q5]

quiz = Quiz(questions)

quiz.loadQuestion()