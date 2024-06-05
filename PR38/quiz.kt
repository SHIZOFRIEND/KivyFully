<WelcomeScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 50
        spacing: 20
        Label:
            text: 'Добро пожаловать в грибной квиз!'
            font_size: 32
        Button:
            text: 'Начнем квиз'
            font_size: 24
            size_hint: None, None
            size: 200, 50
            on_press: root.start_quiz()
<QuizScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 50
        spacing: 20
        Label:
            id: question_label
            text: ''
            font_size: 24
        Image:
            id: question_image
            source: ''
        Button:
            id: option1
            text: ''
            font_size: 24
            on_press: root.check_answer(self)
        Button:
            id: option2
            text: ''
            font_size: 24
            on_press: root.check_answer(self)
        Button:
            id: option3
            text: ''
            font_size: 24
            on_press: root.check_answer(self)
        Button:
            id: option4
            text: ''
            font_size: 24
            on_press: root.check_answer(self)
<ResultScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 50
        spacing: 20
        Label:
            id: result_label
            text: ''
            font_size: 24
        Image:
            id: result_image
            source: 'images/result.png'