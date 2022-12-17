from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import DictProperty, StringProperty, get_color_from_hex
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.uix.picker import MDThemePicker
from kivymd.uix.textfield import MDTextField

import demo.demo
from demo.demo import profiles
from kvs.dialog_config import DialogConfig

Builder.load_file('kvs/widgets/bank_layout.kv')
Builder.load_file('kvs/widgets/avatar.kv')
Builder.load_file('kvs/widgets/log_list_item.kv')

Builder.load_file('kvs/widgets/dialog_config.kv')

Window.size = (320, 700)


class WindowManager(ScreenManager):
    '''A window manager to manage switching between sceens.'''


class BankWithImage(MDCard):
    '''A horizontal layout with an image(profile picture)
        and a text(username) - The Story.'''
    profile = DictProperty()
    text = StringProperty()
    source = StringProperty()


class LogListItem(MDBoxLayout):
    '''A clickable chat item for the chat timeline.'''
    bank_name = StringProperty()
    mssg = StringProperty()
    timestamp = StringProperty()
    profile = DictProperty()


class HomeScreen(Screen):
    pass


class MainApp(MDApp):
    ''' The main App class using kivymd's properties.'''
    dialog = None
    runningBank = None

    def build(self):
        ''' Initializes the Application
        and returns the root widget'''
        self.theme_cls.theme_style = 'Light'
        self.title = "Bank config"
        self.wm = WindowManager(transition=FadeTransition())
        screens = [
            HomeScreen(name='home'),
        ]
        for screen in screens:
            self.wm.add_widget(screen)

        self.bank_list_builder()
        self.log_list_builder()

        return self.wm

    def bank_list_builder(self):
        '''Create a Story for each user and
        adds it to the story layout'''
        for profile in demo.demo.profiles:
            bank = BankWithImage()
            bank.text = profile['name']
            bank.source = profile['image']
            bank.profile = profile
            self.wm.screens[0].ids['bank_layout'].add_widget(bank)

    def log_list_builder(self):
        for messages in profiles:
            self.log_item = LogListItem()
            self.log_item.profile = messages
            self.log_item.bank_name = messages['name']
            self.log_item.mssg = "Service is running...."
            self.log_item.timestamp = "2022-09-19 17:44:17.858167"
            self.wm.screens[0].ids['logList'].add_widget(self.log_item)

    def bank_config(self, profile):

        cancel_button = MDFlatButton(
            text="Cancel",
            theme_text_color="Custom",
            radius=[8],
        )

        save_button = MDRaisedButton(
            text="Save",
            radius=[8],
            md_bg_color=get_color_from_hex("#27133a")
        )

        ui = DialogConfig(profile)
        def on_click(*args):
            i = 0
            while i < len(ui.bank_config.fields):
                ui.bank_config.fields[i]['value'] = ui.list_text_field[i].text
                i = i + 1
            self.runningBank = ui.bank_config
            self.dialog.dismiss()

        save_button.bind(on_release=on_click)
        cancel_button.bind(on_release=self.dismiss_dialog)
        self.dialog = MDDialog(
            size_hint=[0.9, None],
            title="Config for: " + profile.name,
            type="custom",
            content_cls=ui,
            auto_dismiss=False,
            buttons=[
                cancel_button,
                save_button
            ],
        )

        self.dialog.open()

    def dismiss_dialog(self, *args):
        self.dialog.dismiss()

    def start_service(self):
        toast("Start service")

    def stop_service(self):
        toast("Stop service")


if __name__ == "__main__":
    MainApp().run()

# python 3.9
# kivy 2.1.0
# kivymd 0.104.2
