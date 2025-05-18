import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import math  

kivy.require('1.11.1')

class CalculatorApp(App):
    def build(self):
     
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)


        name_label = Label(text="Hani Hamadi", font_size=30, size_hint=(1, 0.2))
        main_layout.add_widget(name_label)


        self.result = TextInput(font_size=32, readonly=True, halign="right", multiline=False, size_hint=(1, 0.2))
        main_layout.add_widget(self.result)

        buttons_layout = GridLayout(cols=5, spacing=10, size_hint=(1, 0.6))

        buttons = [
            ('7', self.add_to_expression), ('8', self.add_to_expression), ('9', self.add_to_expression), ('/', self.add_to_expression), ('√', self.sqrt),
            ('4', self.add_to_expression), ('5', self.add_to_expression), ('6', self.add_to_expression), ('*', self.add_to_expression), ('^', self.pow),
            ('1', self.add_to_expression), ('2', self.add_to_expression), ('3', self.add_to_expression), ('-', self.add_to_expression), ('log', self.log),
            ('C', self.clear), ('0', self.add_to_expression), ('=', self.calculate), ('+', self.add_to_expression), ('sin', self.sin),
            ('cos', self.cos), ('tan', self.tan), ('exp', self.exp), ('pi', self.pi)
        ]

        for text, action in buttons:
            button = Button(text=text, on_press=action)
            buttons_layout.add_widget(button)

        main_layout.add_widget(buttons_layout)
        return main_layout

    def add_to_expression(self, instance):
        self.result.text += instance.text

    def clear(self, instance):
        self.result.text = ""

    def calculate(self, instance):
        try:
         
            expression = self.result.text
         
            result = str(eval(expression))
            self.result.text = result
        except Exception as e:
            self.result.text = "Error"

    def sqrt(self, instance):
        try:
            value = float(self.result.text)
            self.result.text = str(math.sqrt(value)) 
        except ValueError:
            self.result.text = "Error"

    def pow(self, instance):
        try:
          
            parts = self.result.text.split('^')
            if len(parts) == 2:
                base = float(parts[0])
                exponent = float(parts[1])
                self.result.text = str(math.pow(base, exponent))  
        except ValueError:
            self.result.text = "Error"

    def log(self, instance):
        try:
            value = float(self.result.text)
            self.result.text = str(math.log(value)) 
        except ValueError:
            self.result.text = "Error"

    def sin(self, instance):
        try:
            value = math.radians(float(self.result.text))  
            self.result.text = str(math.sin(value)) 
        except ValueError:
            self.result.text = "Error"

    def cos(self, instance):
        try:
            value = math.radians(float(self.result.text)) 
            self.result.text = str(math.cos(value)) 
        except ValueError:
            self.result.text = "Error"

    def tan(self, instance):
        try:
            value = math.radians(float(self.result.text))
            self.result.text = str(math.tan(value))  
        except ValueError:
            self.result.text = "Error"

    def exp(self, instance):
        try:
            value = float(self.result.text)
            self.result.text = str(math.exp(value)) 
        except ValueError:
            self.result.text = "Error"

    def pi(self, instance):
        self.result.text = str(math.pi)  

if __name__ == '__main__':
    CalculatorApp().run()
