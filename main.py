from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import DictProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.uix.picker import MDThemePicker

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
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Teal'
        self.theme_cls.accent_palette = 'Teal'
        self.theme_cls.accent_hue = '400'
        self.title = "Bank config"
        self.wm = WindowManager(transition=FadeTransition())
        screens = [
            HomeScreen(name='home'),
        ]
        for screen in screens:
            self.wm.add_widget(screen)

        self.story_builder()
        self.chat_list_builder()

        return self.wm


    def show_theme_picker(self):
        '''Display a dialog window to change app's color and theme.'''
        theme_dialog = MDThemePicker()
        theme_dialog.open()



    def story_builder(self):
        '''Create a Story for each user and
        adds it to the story layout'''
        for profile in demo.demo.profiles:
            bank = BankWithImage()
            bank.text = profile['name']
            bank.source = profile['image']
            bank.profile = profile
            self.wm.screens[0].ids['bank_layout'].add_widget(bank)

    def chat_list_builder(self):
        for messages in profiles:
            self.log_item = LogListItem()
            self.log_item.profile = messages
            self.log_item.bank_name = messages['name']
            self.log_item.mssg = "Service is running...."
            self.log_item.timestamp = "2022-09-19 17:44:17.858167"
            self.wm.screens[0].ids['logList'].add_widget(self.log_item)

    def bank_config(self, profile):
        save_button = MDRaisedButton(
            text="Start",
            radius=[8],

        )
        save_button.bind(on_release=self.on_save)
        self.dialog = MDDialog(
            title="Config for: " + profile.name,
            type="custom",

            content_cls=DialogConfig(profile),
            buttons=[
                MDFlatButton(
                    text="Cancel",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    radius=[8],
                ),
                save_button
            ],
        )

        self.dialog.open()

    def on_save(self, profile):
        toast(profile.name)

if __name__ == "__main__":
    MainApp().run()