from kivy.lang import Builder
from kivy.properties import DictProperty
from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField


class DialogConfig(MDBoxLayout):
    bank_config = DictProperty()
    list_text_field = []

    def __init__(self, bank_config):
        self.fields = bank_config.fields
        super().__init__()

        self.bank_config = bank_config

        for field in self.bank_config.fields:
            textField = MDTextField()
            self.list_text_field.append(textField)

            textField.text = field['value']
            textField.hint_text = field['label']
            self.add_widget(textField)

