from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

KV = """
<CalcLayout>:
    orientation: "vertical"
    padding: 20
    spacing: 15

    canvas.before:
        Color:
            rgba: 0.07, 0.07, 0.1, 1
        Rectangle:
            pos: self.pos
            size: self.size

    Label:
        text: "[b]Simple Calculator[/b]"
        markup: True
        font_size: "28sp"
        size_hint_y: None
        height: "40dp"
        color: 1, 1, 1, 1

    BoxLayout:
        orientation: "vertical"
        size_hint_y: None
        height: "120dp"
        spacing: 8

        Label:
            text: "First number"
            size_hint_y: None
            height: "20dp"
            color: 0.8, 0.8, 0.9, 1

        TextInput:
            id: num1
            multiline: False
            size_hint_y: None
            height: "40dp"
            background_color: 0.18, 0.18, 0.25, 1
            foreground_color: 1, 1, 1, 1
            cursor_color: 1, 1, 1, 1

    BoxLayout:
        orientation: "vertical"
        size_hint_y: None
        height: "120dp"
        spacing: 8

        Label:
            text: "Second number"
            size_hint_y: None
            height: "20dp"
            color: 0.8, 0.8, 0.9, 1

        TextInput:
            id: num2
            multiline: False
            size_hint_y: None
            height: "40dp"
            background_color: 0.18, 0.18, 0.25, 1
            foreground_color: 1, 1, 1, 1
            cursor_color: 1, 1, 1, 1

    BoxLayout:
        size_hint_y: None
        height: "50dp"
        spacing: 10

        Button:
            text: "+"
            on_press: root.calculate("+")
            background_normal: ""
            background_color: 0.25, 0.45, 0.9, 1

        Button:
            text: "-"
            on_press: root.calculate("-")
            background_normal: ""
            background_color: 0.25, 0.45, 0.9, 1

        Button:
            text: "×"
            on_press: root.calculate("*")
            background_normal: ""
            background_color: 0.25, 0.45, 0.9, 1

        Button:
            text: "÷"
            on_press: root.calculate("/")
            background_normal: ""
            background_color: 0.25, 0.45, 0.9, 1

    Label:
        id: result_label
        text: "Result: "
        font_size: "20sp"
        color: 0.9, 0.9, 1, 1
"""


class CalcLayout(BoxLayout):
    def calculate(self, op):
        num1 = self.ids.num1.text.strip()
        num2 = self.ids.num2.text.strip()

        try:
            a = float(num1)
            b = float(num2)
        except ValueError:
            self.ids.result_label.text = "Result: invalid input"
            return

        if op == "+":
            res = a + b
        elif op == "-":
            res = a - b
        elif op == "*":
            res = a * b
        elif op == "/":
            if b == 0:
                self.ids.result_label.text = "Result: division by zero"
                return
            res = a / b
        else:
            self.ids.result_label.text = "Result: unknown op"
            return

        self.ids.result_label.text = f"Result: {res}"


class CalculatorApp(App):
    def build(self):
        Builder.load_string(KV)
        return CalcLayout()


if __name__ == "__main__":
    CalculatorApp().run()
