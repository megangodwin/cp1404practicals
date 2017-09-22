"""
CP1404 Practical 06
Convert Miles to Kilometers - Kivy Exercise
Megan Godwin
"""

from kivy.app import App
from kivy.app import Builder

MILES_TO_KM = 1.60934

class MilesConverterApp(App):
    def build(self):
        self.title = "Convert miles to kilometers"
        self.root = Builder.load_file('convert_m_to_km.kv')
        return self.root

    def handle_conversion(self):
            value = self.get_miles()
            conversion = value * MILES_TO_KM
            self.root.ids.output_label.text = str(conversion)

    def handle_increment_up(self):
        value = self.get_miles()
        value = value + 1
        self.root.ids.input_miles.text = str(value)
        self.handle_conversion()

    def handle_increment_down(self):
        value = self.get_miles()
        value = value - 1
        self.root.ids.input_miles.text = str(value)
        self.handle_conversion()

    def get_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0.0

MilesConverterApp().run()
