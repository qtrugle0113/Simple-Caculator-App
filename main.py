from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class CalculatorApp(App):

    def build(self):
        layout = BoxLayout(padding=10, orientation='vertical')
        self.display = Button(text='0', font_size=40, size_hint=(1, 1),
                              background_color=(1, 1, 1, 1),
                              color=(0, 0, 0, 1), disabled=True)
        layout.add_widget(self.display)
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', '+'],
        ]
        for row in buttons:
            row_layout = BoxLayout()
            for label in row:
                button = Button(text=label, font_size=40, size_hint=(.25, 1))
                button.bind(on_press=self.button_pressed)
                row_layout.add_widget(button)
            layout.add_widget(row_layout)

        # Add Clear, Backspace, and = buttons in a horizontal box
        buttons_layout = BoxLayout()
        clear_button = Button(text='Clear', font_size=40, size_hint=(.25, 1))
        clear_button.bind(on_press=self.clear)
        buttons_layout.add_widget(clear_button)

        backspace_button = Button(text='<<', font_size=40, size_hint=(.25, 1))
        backspace_button.bind(on_press=self.backspace)
        buttons_layout.add_widget(backspace_button)

        equals_button = Button(text='=', font_size=40, size_hint=(.5, 1))
        equals_button.bind(on_press=self.calculate)
        buttons_layout.add_widget(equals_button)

        layout.add_widget(buttons_layout)
        return layout

    def button_pressed(self, instance):
        if self.display.text == '0' or self.display.text == 'Error':
            self.display.text = ''
        self.display.text += instance.text

    def clear(self, instance):
        self.display.text = '0'

    def backspace(self, instance):
        self.display.text = self.display.text[:-1]
        if self.display.text == '':
            self.display.text = '0'

    def calculate(self, instance):
        try:
            self.display.text = str(eval(self.display.text))
        except:
            self.display.text = 'Error'


if __name__ == '__main__':
    CalculatorApp().run()
