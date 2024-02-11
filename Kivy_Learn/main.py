from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config

Config.set('graphics', 'width', f'{9*50}')
Config.set('graphics', 'height', f'{16*50}')

class MainWidget(Widget):
    print("here in widgets!")

class TheLabApp(App):
    print("here in app!")

TheLabApp().run()