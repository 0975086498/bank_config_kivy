
from kivy.lang import Builder
from kivy.properties import DictProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField



class DialogConfig(MDBoxLayout):
    bank_config = DictProperty()

    def __init__(self, bank_config):
        super().__init__()

        self.bank_config = bank_config
        # self.ids.name = self.bank_config.name

        for field in self.bank_config.fields:
            textField = MDTextField()

            def on_text(*args):
                field['value'] = textField.text
                print(field['value'])

            textField.on_text = on_text
            textField.text = field['value']
            textField.hint_text = field['label']
            self.add_widget(textField)

    # def on_save(self, instance, value):



