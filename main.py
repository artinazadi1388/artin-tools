from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, RoundedRectangle, Rectangle, Line
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import NumericProperty

import random
import string
from datetime import date
import ast
import operator


# =========================================================
# COLORS
# =========================================================

BG = (0.025, 0.03, 0.045, 1)
CARD = (0.055, 0.065, 0.09, 1)
CARD2 = (0.08, 0.095, 0.13, 1)

BLUE = (0.08, 0.55, 1, 1)
PURPLE = (0.45, 0.25, 1, 1)
GREEN = (0.1, 0.75, 0.45, 1)
RED = (0.85, 0.2, 0.25, 1)

WHITE = (0.95, 0.97, 1, 1)
GRAY = (0.52, 0.56, 0.65, 1)


# =========================================================
# ROUNDED BUTTON
# =========================================================

class RoundedButton(Button):

    def __init__(self, bg_color=CARD2, **kwargs):

        super().__init__(**kwargs)

        self.background_normal = ""
        self.background_down = ""
        self.background_color = (0, 0, 0, 0)

        self.bg_color = bg_color

        with self.canvas.before:
            Color(*self.bg_color)
            self.rect = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[18]
            )

        self.bind(
            pos=self.update_rect,
            size=self.update_rect
        )

    def update_rect(self, *args):

        self.rect.pos = self.pos
        self.rect.size = self.size


# =========================================================
# SPLASH SCREEN
# =========================================================

class SplashScreen(Screen):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        with self.canvas.before:

            Color(*BG)

            self.background = Rectangle(
                pos=self.pos,
                size=self.size
            )

        self.bind(
            pos=self.update_background,
            size=self.update_background
        )

        layout = BoxLayout(
            orientation="vertical",
            padding=35,
            spacing=8
        )

        layout.add_widget(
            Label(
                text="NØX × ARTIN",
                font_size=18,
                bold=True,
                color=GRAY,
                size_hint_y=None,
                height=45
            )
        )

        layout.add_widget(
            Label(
                text="ARTIN",
                font_size=62,
                bold=True,
                color=BLUE
            )
        )

        layout.add_widget(
            Label(
                text="TOOLS",
                font_size=38,
                bold=True,
                color=WHITE
            )
        )

        layout.add_widget(
            Label(
                text="SMART TOOLS. SIMPLE LIFE.",
                font_size=14,
                color=GRAY,
                size_hint_y=None,
                height=35
            )
        )

        self.loading = Label(
            text="INITIALIZING",
            font_size=16,
            bold=True,
            color=BLUE,
            size_hint_y=None,
            height=50
        )

        layout.add_widget(self.loading)

        layout.add_widget(
            Label(
                text="VERSION 2.0",
                font_size=12,
                color=GRAY,
                size_hint_y=None,
                height=30
            )
        )

        self.add_widget(layout)

        self.loading_step = 0

        Clock.schedule_interval(
            self.animate_loading,
            0.35
        )

        Clock.schedule_once(
            self.go_home,
            7
        )

    def update_background(self, *args):

        self.background.pos = self.pos
        self.background.size = self.size

    def animate_loading(self, dt):

        dots = "." * (self.loading_step % 4)

        self.loading.text = "INITIALIZING" + dots

        self.loading_step += 1

    def go_home(self, dt):

        Clock.unschedule(
            self.animate_loading
        )

        self.manager.current = "home"


# =========================================================
# HOME
# =========================================================

class HomeScreen(Screen):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        with self.canvas.before:

            Color(*BG)

            self.background = Rectangle(
                pos=self.pos,
                size=self.size
            )

        self.bind(
            pos=self.update_background,
            size=self.update_background
        )

        main = BoxLayout(
            orientation="vertical",
            padding=22,
            spacing=12
        )

        main.add_widget(
            Label(
                text="ARTIN",
                font_size=42,
                bold=True,
                color=BLUE,
                size_hint_y=None,
                height=55
            )
        )

        main.add_widget(
            Label(
                text="TOOLS",
                font_size=25,
                bold=True,
                color=WHITE,
                size_hint_y=None,
                height=35
            )
        )

        main.add_widget(
            Label(
                text="SMART TOOLS. SIMPLE LIFE.",
                font_size=12,
                color=GRAY,
                size_hint_y=None,
                height=28
            )
        )

        tools = GridLayout(
            cols=2,
            spacing=12,
            padding=5
        )

        calculator = self.make_button(
            "CALCULATOR",
            BLUE
        )

        age = self.make_button(
            "AGE CALCULATOR",
            PURPLE
        )

        password = self.make_button(
            "PASSWORD",
            GREEN
        )

        converter = self.make_button(
            "CONVERTER",
            BLUE
        )

        calculator.bind(
            on_press=lambda x:
            self.open_screen("calculator")
        )

        age.bind(
            on_press=lambda x:
            self.open_screen("age")
        )

        password.bind(
            on_press=lambda x:
            self.open_screen("password")
        )

        converter.bind(
            on_press=lambda x:
            self.open_screen("converter")
        )

        tools.add_widget(calculator)
        tools.add_widget(age)
        tools.add_widget(password)
        tools.add_widget(converter)

        main.add_widget(tools)

        main.add_widget(
            Label(
                text="ARTIN TOOLS • v2.0",
                font_size=11,
                color=GRAY,
                size_hint_y=None,
                height=25
            )
        )

        self.add_widget(main)

    def update_background(self, *args):

        self.background.pos = self.pos
        self.background.size = self.size

    def make_button(self, text, color):

        return RoundedButton(
            text=text,
            font_size=17,
            bold=True,
            bg_color=(0.07, 0.085, 0.12, 1),
            color=WHITE
        )

    def open_screen(self, name):

        self.manager.current = name


# =========================================================
# TOOL SCREEN
# =========================================================

class ToolScreen(Screen):

    def create_layout(self):

        return BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=12
        )

    def title_label(self, text):

        return Label(
            text=text,
            font_size=27,
            bold=True,
            color=BLUE,
            size_hint_y=None,
            height=50
        )

    def back_button(self):

        button = RoundedButton(
            text="←  BACK TO HOME",
            font_size=16,
            bold=True,
            bg_color=(0.07, 0.085, 0.12, 1),
            color=WHITE,
            size_hint_y=None,
            height=50
        )

        button.bind(
            on_press=self.go_home
        )

        return button

    def go_home(self, instance):

        self.manager.current = "home"


# =========================================================
# CALCULATOR
# =========================================================

class CalculatorScreen(ToolScreen):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        layout = self.create_layout()

        layout.add_widget(
            self.title_label("CALCULATOR")
        )

        self.display = TextInput(
            hint_text="0",
            multiline=False,
            readonly=True,
            font_size=30,
            halign="right",
            size_hint_y=None,
            height=75,
            background_color=(0.04, 0.05, 0.07, 1),
            foreground_color=WHITE
        )

        layout.add_widget(self.display)

        buttons = GridLayout(
            cols=4,
            spacing=8
        )

        keys = [
            "AC", "DEL", "%", "÷",
            "7", "8", "9", "×",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "0", ".", "(", ")",
            "="
        ]

        for key in keys:

            if key == "=":
                color = GREEN

            elif key in ["÷", "×", "-", "+"]:
                color = BLUE

            elif key in ["AC", "DEL", "%"]:
                color = PURPLE

            else:
                color = CARD2

            button = RoundedButton(
                text=key,
                font_size=22,
                bold=True,
                bg_color=color,
                color=WHITE
            )

            button.bind(
                on_press=self.button_pressed
            )

            buttons.add_widget(button)

        layout.add_widget(buttons)

        layout.add_widget(
            self.back_button()
        )

        self.add_widget(layout)

    def button_pressed(self, button):

        key = button.text

        if key == "AC":

            self.display.text = ""

        elif key == "DEL":

            self.display.text = \
                self.display.text[:-1]

        elif key == "=":

            self.calculate()

        elif key == "%":

            try:

                value = float(self.display.text)

                self.display.text = str(
                    value / 100
                )

            except:

                self.display.text = "ERROR"

        else:

            self.display.text += key

    def calculate(self):

        expression = self.display.text

        expression = expression.replace(
            "×", "*"
        )

        expression = expression.replace(
            "÷", "/"
        )

        try:

            result = safe_calculate(
                expression
            )

            self.display.text = str(result)

        except:

            self.display.text = "ERROR"


# =========================================================
# SAFE CALCULATOR ENGINE
# =========================================================

allowed_operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg
}


def safe_calculate(expression):

    tree = ast.parse(
        expression,
        mode="eval"
    )

    return calculate_node(
        tree.body
    )


def calculate_node(node):

    if isinstance(
        node,
        ast.Constant
    ):

        if isinstance(
            node.value,
            (int, float)
        ):

            return node.value

    if isinstance(
        node,
        ast.BinOp
    ):

        left = calculate_node(
            node.left
        )

        right = calculate_node(
            node.right
        )

        operation = allowed_operators.get(
            type(node.op)
        )

        if operation is None:
            raise ValueError()

        return operation(
            left,
            right
        )

    if isinstance(
        node,
        ast.UnaryOp
    ):

        value = calculate_node(
            node.operand
        )

        operation = allowed_operators.get(
            type(node.op)
        )

        if operation is None:
            raise ValueError()

        return operation(
            value
        )

    raise ValueError()


# =========================================================
# AGE CALCULATOR
# =========================================================

class AgeScreen(ToolScreen):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        layout = self.create_layout()

        layout.add_widget(
            self.title_label(
                "AGE CALCULATOR"
            )
        )

        self.year = TextInput(
            hint_text="Enter your birth year",
            input_filter="int",
            multiline=False,
            font_size=22,
            size_hint_y=None,
            height=60,
            background_color=(0.08, 0.09, 0.13, 1),
            foreground_color=WHITE
        )

        button = RoundedButton(
            text="CALCULATE AGE",
            font_size=19,
            bold=True,
            bg_color=PURPLE,
            color=WHITE,
            size_hint_y=None,
            height=55
        )

        button.bind(
            on_press=self.calculate_age
        )

        self.result_label = Label(
            text="YOUR AGE",
            font_size=27,
            bold=True,
            color=WHITE
        )

        layout.add_widget(self.year)
        layout.add_widget(button)
        layout.add_widget(self.result_label)
        layout.add_widget(
            self.back_button()
        )

        self.add_widget(layout)

    def calculate_age(self, instance):

        try:

            birth_year = int(
                self.year.text
            )

            current_year = date.today().year

            age = current_year - birth_year

            if age < 0:

                self.result_label.text = \
                    "INVALID YEAR"

            else:

                self.result_label.text = \
                    "YOU ARE " + str(age)

        except:

            self.result_label.text = \
                "ENTER A VALID YEAR"


# =========================================================
# PASSWORD GENERATOR
# =========================================================

class PasswordScreen(ToolScreen):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        layout = self.create_layout()

        layout.add_widget(
            self.title_label(
                "PASSWORD GENERATOR"
            )
        )

        self.length = TextInput(
            hint_text="Password length",
            input_filter="int",
            multiline=False,
            font_size=22,
            size_hint_y=None,
            height=60,
            background_color=(0.08, 0.09, 0.13, 1),
            foreground_color=WHITE
        )

        button = RoundedButton(
            text="GENERATE PASSWORD",
            font_size=18,
            bold=True,
            bg_color=BLUE,
            color=WHITE,
            size_hint_y=None,
            height=55
        )

        button.bind(
            on_press=self.generate_password
        )

        self.result_label = Label(
            text="YOUR PASSWORD",
            font_size=20,
            bold=True,
            color=WHITE
        )

        layout.add_widget(self.length)
        layout.add_widget(button)
        layout.add_widget(self.result_label)
        layout.add_widget(
            self.back_button()
        )

        self.add_widget(layout)

    def generate_password(self, instance):

        try:

            length = int(
                self.length.text
            )

            if length < 4:

                self.result_label.text = \
                    "MINIMUM: 4 CHARACTERS"

                return

            characters = (
                string.ascii_letters
                + string.digits
                + "!@#$%^&*"
            )

            password = ""

            for i in range(length):

                password += random.choice(
                    characters
                )

            self.result_label.text = password

        except:

            self.result_label.text = \
                "ENTER A VALID LENGTH"


# =========================================================
# UNIT CONVERTER
# =========================================================

class ConverterScreen(ToolScreen):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        layout = self.create_layout()

        layout.add_widget(
            self.title_label(
                "UNIT CONVERTER"
            )
        )

        self.value = TextInput(
            hint_text="Enter value",
            input_filter="float",
            multiline=False,
            font_size=22,
            size_hint_y=None,
            height=60,
            background_color=(0.08, 0.09, 0.13, 1),
            foreground_color=WHITE
        )

        km = RoundedButton(
            text="KM  →  MILES",
            font_size=18,
            bold=True,
            bg_color=BLUE,
            color=WHITE,
            size_hint_y=None,
            height=55
        )

        miles = RoundedButton(
            text="MILES  →  KM",
            font_size=18,
            bold=True,
            bg_color=PURPLE,
            color=WHITE,
            size_hint_y=None,
            height=55
        )

        km.bind(
            on_press=self.km_to_miles
        )

        miles.bind(
            on_press=self.miles_to_km
        )

        self.result_label = Label(
            text="RESULT",
            font_size=27,
            bold=True,
            color=WHITE
        )

        layout.add_widget(self.value)
        layout.add_widget(km)
        layout.add_widget(miles)
        layout.add_widget(self.result_label)
        layout.add_widget(
            self.back_button()
        )

        self.add_widget(layout)

    def km_to_miles(self, instance):

        try:

            km = float(
                self.value.text
            )

            miles = km * 0.621371

            self.result_label.text = \
                str(round(miles, 2)) + " MILES"

        except:

            self.result_label.text = \
                "ENTER A VALID NUMBER"

    def miles_to_km(self, instance):

        try:

            miles = float(
                self.value.text
            )

            km = miles * 1.60934

            self.result_label.text = \
                str(round(km, 2)) + " KM"

        except:

            self.result_label.text = \
                "ENTER A VALID NUMBER"


# =========================================================
# MAIN APP
# =========================================================

class ArtinTools(App):

    def build(self):

        Window.clearcolor = BG

        manager = ScreenManager()

        manager.add_widget(
            SplashScreen(name="splash")
        )

        manager.add_widget(
            HomeScreen(name="home")
        )

        manager.add_widget(
            CalculatorScreen(name="calculator")
        )

        manager.add_widget(
            AgeScreen(name="age")
        )

        manager.add_widget(
            PasswordScreen(name="password")
        )

        manager.add_widget(
            ConverterScreen(name="converter")
        )

        manager.current = "splash"

        return manager


ArtinTools().run()
