from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.utils import get_color_from_hex
class RainbowApp(App):
    def build(self):
        layout = GridLayout(cols=2)
        rainbow_colors = {
            "красный": "#ff0000",
            "оранжевый": "#ff8800",
            "желтый": "#ffff00",
            "зеленый": "#00ff00",
            "голубой": "#00ffff",
            "синий": "#0000ff",
            "фиолетовый": "#ff00ff"
        }
        self.color_code = TextInput(text='', multiline=False)
        layout.add_widget(Label(text='Код цвета:'))
        layout.add_widget(self.color_code)
        self.color_name = Label(text='')
        layout.add_widget(Label(text='Название цвета:'))
        layout.add_widget(self.color_name)
        for color_name, color_code in rainbow_colors.items():
            button = Button(text=color_name, background_color=get_color_from_hex(color_code))
            button.bind(on_press=lambda instance, color=color_code: self.on_button_press(instance, color))
            layout.add_widget(button)
        return layout
    def on_button_press(self, instance, color_code):
        color_name = instance.text
        self.color_name.text = color_name
        self.color_code.text = color_code
if __name__ == '__main__':
    RainbowApp().run()