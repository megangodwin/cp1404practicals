"""
CP1404 Practical 06
Loops through and prints names using dynamic buttons
Megan Godwin
Modified from dynamic_widgets
"""


from kivy.app import App
from kivy.app import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

class DynamicWidgetsApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        self.name_list = ["Ana", "Hana", "Lena", "Bob", "Jim", "Jesse", "Gabe"]

    def build(self):
        """
        Build the Kivy GUI
        :return: reference to the root Kivy widget
        """
        self.title = "Names"
        self.root = Builder.load_file('names.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """
        Create buttons from dictionary entries and add them to the GUI
        :return: None
        """
        for name in self.name_list:
            # create a button for each phonebook entry
            temp_button = Button(text=name)
            temp_button.bind(on_release=self.press_entry)
            # add the button to the "entriesBox" using add_widget()
            self.root.ids.entriesBox.add_widget(temp_button)

    def press_entry(self, instance):
        """
        Handler for pressing entry buttons
        :param instance: the Kivy button instance
        :return: None
        """
        # update status text
        name = instance.text
        self.status_text = "{}'s number is {}".format(name, self.name_list[name])

    def clear_all(self):
        """
        Clear all of the widgets that are children of the "entriesBox" layout widget
        :return:
        """
        self.root.ids.entriesBox.clear_widgets()


DynamicWidgetsApp().run()

