from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.clock import Clock
from datetime import datetime, timedelta
class ReminderApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.reminders = []
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.date_spinner = Spinner(text='Выберите дату')
        self.date_spinner.values = self.generate_date_values()
        self.time_spinner = Spinner(text='Выберите время')
        self.time_spinner.values = [str(i) + ':00' for i in range(24)]
        set_reminder_button = Button(text='Установить напоминание')
        set_reminder_button.bind(on_press=self.set_reminder)
        layout.add_widget(Label(text="Выберите дату и время для напоминания:"))
        layout.add_widget(self.date_spinner)
        layout.add_widget(self.time_spinner)
        layout.add_widget(set_reminder_button)
        Clock.schedule_interval(self.check_reminders, 60)
        return layout
    def generate_date_values(self):
        today = datetime.now().date()
        date_values = []
        for i in range(7):
            date = today + timedelta(days=i)
            date_values.append(date.strftime("%Y-%m-%d"))
        return date_values
    def set_reminder(self, instance):
        selected_date = self.date_spinner.text
        selected_time = self.time_spinner.text
        reminder_datetime = datetime.strptime(selected_date, "%Y-%m-%d").replace(hour=int(selected_time.split(':')[0]), minute=0, second=0)
        current_datetime = datetime.now()
        if reminder_datetime <= current_datetime:
            popup = Popup(title='Ошибка', content=Label(text='Выберите будущую дату и время!'), size_hint=(None, None), size=(300, 200))
            popup.open()
        else:
            self.reminders.append(reminder_datetime)
    def check_reminders(self, dt):
        current_datetime = datetime.now()
        for reminder in self.reminders:
            if current_datetime >= reminder:
                self.show_reminder(reminder)
                self.reminders.remove(reminder)
    def show_reminder(self, reminder):
        reminder_time = reminder.strftime("%Y-%m-%d %H:%M:%S")
        popup = Popup(title='Напоминание', content=Label(text=f"Время: {reminder_time}!"), size_hint=(None, None), size=(300, 200))
        popup.open()
if __name__ == '__main__':
    ReminderApp().run()
