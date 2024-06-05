import pyodbc
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
server = 'DESKTOP-OIV0VNA\\SQLEXPRESS'
database = 'UserDatabase'
driver = '{ODBC Driver 17 for SQL Server}'
conn = pyodbc.connect(
    f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
)
cursor = conn.cursor()
Builder.load_file('windows.kv')
class WelcomeScreen(Screen):
    def go_to_register(self):
        self.manager.current = 'register'
    def go_to_login(self):
        self.manager.current = 'login'
class RegisterScreen(Screen):
    def register(self):
        username = self.ids.username_input.text
        password = self.ids.password_input.text
        cursor.execute("SELECT * FROM Users WHERE Username=?", (username,))
        if cursor.fetchone():
            self.add_widget(Label(text='Username already exists!'))
        else:
            cursor.execute("INSERT INTO Users (Username, Password) VALUES (?, ?)", (username, password))
            conn.commit()
            self.manager.current = 'login'
class LoginScreen(Screen):
    def login(self):
        username = self.ids.username_input.text
        password = self.ids.password_input.text
        cursor.execute("SELECT * FROM Users WHERE Username=? AND Password=?", (username, password))
        if cursor.fetchone():
            self.add_widget(Label(text='Login successful!'))
        else:
            self.add_widget(Label(text='Invalid username or password!'))
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(LoginScreen(name='login'))
        return sm
if __name__ == '__main__':
    MyApp().run()
