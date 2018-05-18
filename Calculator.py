#kivy.require("1.9.0")
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.config import Config
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '450')
Config.set('kivy','window_icon','Calogo.png')
class CalcScreen(TextInput):
    pass

class CalculatorBody(FloatLayout):

    def calc(self,x):

         try:
             return str(eval(x))
         except:
             return "ERROR!"


class CalculatorApp(App):
    def build(self):
        return CalculatorBody()



Calc = CalculatorApp()

Calc.run()