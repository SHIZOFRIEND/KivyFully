import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
Builder.load_file('quiz.kt')
questions = [
    {"question": "Какой это гриб?", "image": "images/question1.png", "options": ["Рыжик", "Подосиновик", "Лисичка", "Мухомор"], "answer": "Мухомор"},
    {"question": "Идентифицируйте этот гриб.", "image": "images/question2.jpg", "options": ["Лисичка", "Мухомор", "Подосиновик", "Рыжик"], "answer": "Подосиновик"},
    {"question": "Назовите этот гриб.", "image": "images/question3.png", "options": ["Мухомор", "Подосиновик", "Лисичка", "Рыжик"], "answer": "Лисичка"},
    {"question": "Какой тип гриба это?", "image": "images/question4.jpg", "options": ["Мухомор", "Лисичка", "Подосиновик", "Рыжик"], "answer": "Рыжик"},
    {"question": "Идентифицируйте этот гриб.", "image": "images/question5.jpg", "options": ["Устрица", "Рыжик", "Морель", "Белый гриб"], "answer": "Шиитаке"},
    {"question": "Что это за гриб?", "image": "images/question6.jpg", "options": ["Белый гриб", "Шиитаке", "Морель", "Устрица"], "answer": "Устрица"},
    {"question": "Назовите этот гриб.", "image": "images/question7.jpg", "options": ["Шиитаке", "Устрица", "Морель", "Белый гриб"], "answer": "Морель"},
    {"question": "Какой тип гриба это?", "image": "images/question8.jpg", "options": ["Белый гриб", "Морель", "Устрица", "Шиитаке"], "answer": "Белый гриб"},
    {"question": "Идентифицируйте этот гриб.", "image": "images/question9.jpg", "options": ["Майтаке", "Еноки", "Белый гриб", "Морель"], "answer": "Еноки"},
    {"question": "Что это за гриб?", "image": "images/question10.jpg", "options": ["Морель", "Еноки", "Белый гриб", "Майтаке"], "answer": "Майтаке"}
]
class WelcomeScreen(Screen):
    def start_quiz(self):
        self.manager.current = 'quiz'
class QuizScreen(Screen):
    def __init__(self, **kwargs):
        super(QuizScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.add_widget(self.layout)
        self.current_question_index = 0
        self.correct_answers = 0
        self.questions = random.sample(questions, len(questions))
        self.question_label = Label(text="", font_size=24)
        self.layout.add_widget(self.question_label)
        self.image = Image(source="")
        self.layout.add_widget(self.image)
        self.option_buttons = []
        for _ in range(4):
            btn = Button(text="", font_size=24)
            btn.bind(on_press=self.check_answer)
            self.layout.add_widget(btn)
            self.option_buttons.append(btn)
        self.load_question()
    def load_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.question_label.text = question["question"]
            self.image.source = question["image"]
            options = question["options"]
            for i, option in enumerate(options):
                self.option_buttons[i].text = option
        else:
            self.manager.current = 'result'
    def check_answer(self, instance):
        selected_option = instance.text
        correct_answer = self.questions[self.current_question_index]["answer"]
        if selected_option == correct_answer:
            self.correct_answers += 1
        self.current_question_index += 1
        self.load_question()
class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super(ResultScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.add_widget(self.layout)
        self.result_label = Label(text="", font_size=24)
        self.layout.add_widget(self.result_label)
        self.image = Image(source="images/result.png")
        self.layout.add_widget(self.image)
    def on_enter(self, *args):
        quiz_screen = self.manager.get_screen('quiz')
        self.result_label.text = f"Ты набрал {quiz_screen.correct_answers} из {len(questions)} верных!"
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(QuizScreen(name='quiz'))
        sm.add_widget(ResultScreen(name='result'))
        return sm
if __name__ == '__main__':
    MyApp().run()
