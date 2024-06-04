from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.camera import Camera
from kivy.uix.screenmanager import ScreenManager, Screen
from datetime import datetime

Builder.load_file('camera.kv')
class CameraScreen(Screen):
    def __init__(self, **kwargs):
        super(CameraScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.camera = Camera(play=True)
        self.layout.add_widget(self.camera)

        self.capture_button = Button(text="Сделать снимок")
        self.capture_button.bind(on_press=self.capture_image)
        self.layout.add_widget(self.capture_button)

        self.add_widget(self.layout)

    def capture_image(self):
        current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"photo_{current_datetime}.png"
        self.camera.export_to_png(filename)
        print(f"Фотография сохранена как {filename}")


class MainScreen(Screen):
    pass


class TestApp(App):
    def build(self):

        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(CameraScreen(name='camera'))
        return sm


if __name__ == '__main__':
    TestApp().run()
