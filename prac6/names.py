"""
CP1404 Practical 06
Loops through and prints names using dynamic buttons
Megan Godwin
Modified from dynamic_widgets
"""


from kivy.app import App
from kivy.app import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty

class DynamicWidgetsApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        self.name_list = ["Ana", "Hana", "Lena", "Bob", "Jim", "Jesse", "Gabe"]

    def build(self):
        self.title = "Names"
        self.root = Builder.load_file('names.kv')

    def create_label(self):
        for name in self.name_list:
            temp_button = Label(text=name)
            self.root.ids.entriesBox.add_widget(temp_button)



DynamicWidgetsApp().run()

