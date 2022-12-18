from kivy.lang import Builder
from kivy.properties import DictProperty
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivy.core.window import Window

class DialogConfig(ScrollView):
    bank_config = DictProperty()
    list_text_field = []

    def __init__(self, bank_config):
        self.fields = bank_config.fields
        super().__init__()
        window_sizes = Window.size
        self.bank_config = bank_config
        self.height = (window_sizes[1] * 60)/100
        for field in self.bank_config.fields:
            textField = MDTextField()
            self.list_text_field.append(textField)
            textField.text = field['value']
            textField.hint_text = field['label']
            self.ids['contentLayout'].add_widget(textField)
