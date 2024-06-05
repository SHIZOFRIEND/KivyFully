from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.scatter import Scatter
import time
Window.maximize()
Builder.load_string(
    '''
<CameraClick>:
    orientation: 'vertical'
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
    Scatter:
        do_scale: False
        do_translation: False
        Camera:
            id: camera
            resolution: (640, 480)
            allow_stretch: True
            keep_ratio: True
            play: True
'''
)
class CameraClick(BoxLayout):
    def capture(self):
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")
class TestCamera(App):
    def build(self):
        return CameraClick()
TestCamera().run()