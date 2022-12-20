from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.progressbar import MDProgressBar


class ProgressLoader(MDBoxLayout):

    def __init__(self):
        super().__init__()
        progress_bar = MDProgressBar(
            type="indeterminate",
            color=get_color_from_hex("#27133a")
        )
        self.orientation = 'vertical'
        progress_bar.start()
        self.add_widget(progress_bar)
        self.add_widget(Widget(
            height='24sp',
            size_hint_y=None
        ))
