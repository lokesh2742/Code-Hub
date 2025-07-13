from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
math=[
    {
        "question": "If sin(θ) = 3/5 and θ lies in the second quadrant, what is cos(θ)?",
        "options": ["4/5", "-4/5", "3/5", "-3/5"],
        "answer": "-4/5"
    },
    {
        "question": "What is the domain of the function f(x) = √(x^2 - 4)?",
        "options": ["x ∈ (-∞, -2] ∪ [2, ∞)", "x ∈ (-2, 2)", "x ∈ (−∞, ∞)", "x ∈ [−2, 2]"],
        "answer": "x ∈ (-∞, -2] ∪ [2, ∞)"
    },
    {
        "question": "What is the derivative of tan(x)?",
        "options": ["sec²(x)", "cosec²(x)", "cot(x)", "sin(x)"],
        "answer": "sec²(x)"
    },
    {
        "question": "If A and B are two sets such that n(A) = 10, n(B) = 15, and n(A ∪ B) = 20, what is n(A ∩ B)?",
        "options": ["5", "10", "20", "15"],
        "answer": "5"
    },
    {
        "question": "The distance between the points A(2, 3) and B(6, 7) is:",
        "options": ["4", "8", "√32", "2√5"],
        "answer": "2√5"
    },
    {
        "question": "If log₂(x) = 3, then x equals:",
        "options": ["6", "8", "9", "12"],
        "answer": "8"
    },
    {
        "question": "Which of the following is not a function?",
        "options": ["f(x) = x²", "f(x) = |x|", "f(x) = ±√x", "f(x) = x + 1"],
        "answer": "f(x) = ±√x"
    },
    {
        "question": "If f(x) = x² + 2x + 1, what is f(−1)?",
        "options": ["0", "1", "−2", "4"],
        "answer": "0"
    },
    {
        "question": "Which of the following statements is true for arithmetic progression?",
        "options": ["Common difference is constant", "Common ratio is constant", "Terms increase exponentially", "All terms are equal"],
        "answer": "Common difference is constant"
    },
    {
        "question": "If a = 3, d = 2, find the 10th term of the AP.",
        "options": ["21", "20", "19", "22"],
        "answer": "21"
    }
]
physics=[
    {
        "question": "What is the SI unit of electric charge?",
        "options": ["Coulomb", "Farad", "Volt", "Ohm"],
        "answer": "Coulomb"
    },
    {
        "question": "What is the force between two charges of +1 C each placed 1 m apart in vacuum?",
        "options": ["9 × 10^9 N", "1 N", "0 N", "9 × 10^6 N"],
        "answer": "9 × 10^9 N"
    },
    {
        "question": "What is the value of the permittivity of free space (ε₀)?",
        "options": ["8.85 × 10⁻¹² C²/N·m²", "9 × 10⁹ Nm²/C²", "1.6 × 10⁻¹⁹ C", "3 × 10⁸ m/s"],
        "answer": "8.85 × 10⁻¹² C²/N·m²"
    },
    {
        "question": "Which law states that the electric flux through a closed surface is proportional to the enclosed charge?",
        "options": ["Coulomb's Law", "Ampere's Law", "Gauss's Law", "Ohm's Law"],
        "answer": "Gauss's Law"
    },
    {
        "question": "The electric field inside a conductor in electrostatic equilibrium is:",
        "options": ["Maximum", "Zero", "Infinity", "Constant"],
        "answer": "Zero"
    },
    {
        "question": "Two point charges are placed at a distance. If the distance is doubled, the electrostatic force becomes:",
        "options": ["One-fourth", "Half", "Double", "Four times"],
        "answer": "One-fourth"
    },
    {
        "question": "What is the work done in moving a charge on an equipotential surface?",
        "options": ["Maximum", "Zero", "Equal to potential energy", "Infinite"],
        "answer": "Zero"
    },
    {
        "question": "The potential at a distance r from a point charge Q is given by:",
        "options": ["kQ/r", "kQ/r²", "Qr/k", "k/rQ"],
        "answer": "kQ/r"
    },
    {
        "question": "Which of the following is true for electric field lines?",
        "options": ["They never intersect", "They form closed loops", "They are circular", "They point from negative to positive"],
        "answer": "They never intersect"
    },
    {
        "question": "The unit of electric field is:",
        "options": ["N/C", "J/C", "C/N", "V/A"],
        "answer": "N/C"
    }
]
chemistry=[
    {
        "question": "What is the atomic number of Carbon?",
        "options": ["6", "12", "8", "14"],
        "answer": "6"
    },
    {
        "question": "Which of the following is an empirical formula?",
        "options": ["CH2O", "C6H12O6", "C2H6", "C3H8O3"],
        "answer": "CH2O"
    },
    {
        "question": "Which of the following quantum numbers is not possible?",
        "options": ["n = 2, l = 1, m = 0", "n = 3, l = 2, m = -2", "n = 1, l = 0, m = 1", "n = 4, l = 3, m = 2"],
        "answer": "n = 1, l = 0, m = 1"
    },
    {
        "question": "Which law states that mass can neither be created nor destroyed?",
        "options": ["Law of Conservation of Mass", "Law of Definite Proportions", "Law of Multiple Proportions", "Law of Reciprocal Proportions"],
        "answer": "Law of Conservation of Mass"
    },
    {
        "question": "The number of moles in 22.4 L of an ideal gas at STP is:",
        "options": ["1", "2", "0.5", "22.4"],
        "answer": "1"
    },
    {
        "question": "Which of the following elements has the highest electronegativity?",
        "options": ["Fluorine", "Oxygen", "Chlorine", "Nitrogen"],
        "answer": "Fluorine"
    },
    {
        "question": "What is the shape of an sp³ hybrid orbital?",
        "options": ["Tetrahedral", "Trigonal planar", "Linear", "Octahedral"],
        "answer": "Tetrahedral"
    },
    {
        "question": "Which of the following is an exothermic process?",
        "options": ["Combustion of methane", "Evaporation of water", "Melting of ice", "Boiling of alcohol"],
        "answer": "Combustion of methane"
    },
    {
        "question": "The radius of an atom increases as we move:",
        "options": ["Down a group", "Across a period (left to right)", "From metal to non-metal", "From cation to anion"],
        "answer": "Down a group"
    },
    {
        "question": "Which orbital has the highest energy in a multi-electron atom?",
        "options": ["3d", "4s", "3p", "2p"],
        "answer": "3d"
    }
]



KV = """
ScreenManager:
    Home:
    Maths:
    Physics:
    Chemistry:
    QuizScreen:
<Home>:
    name: 'home'
    MDNavigationDrawer:
        id: nav_drawer

        MDBoxLayout:
            orientation: "vertical"
            spacing: "8dp"
            padding: "8dp"
            pos_hint: {'center_x': 0.0,'center_y': 1.1}
            MDLabel:
                text: "Choose Theme"
                font_style: "H6"
                size_hint_y: None
                height: self.texture_size[1]

            MDList:

                OneLineIconListItem:
                    text: "Light Theme"
                    on_release:
                        app.change_theme("Light")
                        nav_drawer.set_state("close")
                    IconLeftWidget:
                        icon: "white-balance-sunny"

                OneLineIconListItem:
                    text: "Dark Theme"
                    on_release:
                        app.change_theme("Dark")
                        nav_drawer.set_state("close")
                    IconLeftWidget:
                        icon: "weather-night"
    MDBoxLayout:
        orientation: 'vertical'
        pos_hint: {'center_x': 0.5,'center_y': 0.8}
        spacing: '70dp'
        padding: '10dp'
        MDTopAppBar:
            title: "Choose a subject"
            left_action_items: [["menu",lambda x: nav_drawer.set_state("open")]]
        MDRaisedButton:
            text: "Maths"
            pos_hint: {'center_x': 0.5}
            on_release: 
                app.root.current = 'maths'
                app.root.transition.direction = 'left'
        MDRaisedButton:
            text: "Physics"
            pos_hint: {'center_x': 0.5}
            on_release: 
                app.root.current = 'physics'
                app.root.transition.direction = 'left'
        MDRaisedButton:
            text: "Chemistry"
            pos_hint: {'center_x': 0.5}
            on_release:
                app.root.current = 'chemistry'
                app.root.transition.direction = 'left'

<Maths>:
    name: 'maths'
    MDBoxLayout:
        orientation: 'vertical'
        spacing: '40dp'
        MDTopAppBar:
            title: "Maths"
            left_action_items: [["arrow-left", lambda x: app.back()]]
            halign: 'center'
        MDLabel:
            text: "You will get +4 for every correct answer and -1 for every wrong answer"
            halign: 'center'
            font_style: 'H5'
            size_hint_y: None
            height: self.texture_size[1]
        MDTextField:
            id: textin
            hint_text: "Enter number of questions"
            helper_text: "Not more than 10"
            helper_text_mode: "on_focus"
            halign: 'center'
            size_hint_x: 0.5
            pos_hint: {'center_x': 0.5,'center_y': 0.0}
        MDRaisedButton:
            text: "Start Quiz"
            pos_hint: {'center_x': 0.5}
            on_release: app.squiz('maths')
        MDLabel:
            text: ''
            halign: 'center'

<Physics>:
    name: 'physics'
    MDBoxLayout:
        orientation: 'vertical'
        spacing: '40dp'
        MDTopAppBar:
            title: "Physics"
            left_action_items: [["arrow-left", lambda x: app.back()]]
            halign: 'center'
        MDLabel:
            text: "You will get +4 for every correct answer and -1 for every wrong answer"
            halign: 'center'
            font_style: 'H5'
            size_hint_y: None
            height: self.texture_size[1]
        MDTextField:
            id: textin
            hint_text: "Enter number of questions"
            helper_text: "Not more than 10"
            helper_text_mode: "on_focus"
            halign: 'center'
            size_hint_x: 0.5
            pos_hint: {'center_x': 0.5,'center_y': 0.0}
        MDRaisedButton:
            text: "Start Quiz"
            pos_hint: {'center_x': 0.5}
            on_release: app.squiz('physics')
        MDLabel:
            text: ''
            halign: 'center'

<Chemistry>:
    name: 'chemistry'
    MDBoxLayout:
        orientation: 'vertical'
        spacing: '40dp'
        MDTopAppBar:
            title: "Chemistry"
            halign: 'center'
            left_action_items: [["arrow-left", lambda x: app.back()]]
        MDLabel:
            text: "You will get +4 for every correct answer and -1 for every wrong answer"
            halign: 'center'
            font_style: 'H5'
            size_hint_y: None
            height: self.texture_size[1]
        MDTextField:
            id: textin
            hint_text: "Enter number of questions"
            helper_text: "Not more than 10"
            helper_text_mode: "on_focus"
            halign: 'center'
            size_hint_x: 0.5
            pos_hint: {'center_x': 0.5,'center_y': 0.0}
        MDRaisedButton:
            text: "Start Quiz"
            pos_hint: {'center_x': 0.5}
            on_release: app.squiz('chemistry')
        MDLabel:
            text: ''
            halign: 'center'
<QuizScreen>:
    name: 'quiz'
    MDLabel:
        text: ""
"""

class Home(Screen):
    pass

class Maths(Screen):
    pass

class Physics(Screen):
    pass

class Chemistry(Screen):
    pass
class QuizScreen(Screen):
    pass
class MyApp(MDApp):
    def build(self):
        self.index=0
        self.score=0
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)
    def back(self):
        if self.root.current == "maths" or "physics" or "chemistry" or "quiz":
            self.root.current = "home"
            self.root.transition.direction = "right"
    def change_theme(self, theme_name):
        self.theme_cls.theme_style = theme_name
    def show(self):
        screen = self.root.get_screen("quiz")
        screen.clear_widgets()
        ques=self.quiz_data[self.index]["question"]
        options=self.quiz_data[self.index]["options"]
        lay=MDBoxLayout(orientation='vertical', spacing='50dp', padding='10dp')
        label=MDLabel(text=ques, halign='center', font_style='H5', size_hint_y=None, height='48dp')
        lay.add_widget(label)
        for i in range(4):
            btn = MDRaisedButton(text=options[i], size_hint_y=None, height='48dp',pos_hint={'center_x': 0.5},on_release=lambda x, opt=options[i]: self.check(opt))
            lay.add_widget(btn)
        screen.add_widget(lay)
    def squiz(self,subject):
        if subject == 'maths':
            self.quiz_data = math
        elif subject == 'physics':
            self.quiz_data = physics
        elif subject == 'chemistry':
            self.quiz_data = chemistry
        self.root.current = 'quiz'
        self.root.transition.direction = 'left'
        input_screen = self.root.get_screen(subject)
        self.text = input_screen.ids.textin.text
        self.sub=subject
        self.show()
    def check(self,answer):
        if answer ==self.quiz_data[self.index]["answer"]:
            self.score += 4
        else:
            self.score-=1
        self.next()
    def next(self):
        self.index += 1
        if self.index <= int(self.text) -1:
            self.show()
        else:
            screen = self.root.get_screen("quiz")
            screen.clear_widgets()
            label = MDLabel(text=f"Quiz Completed! Your score is: {self.score}/{int(self.text)*4}", halign='center', font_style='H5', size_hint_y=None, height='48dp',pos_hint={'center_y': 0.5})
            btn= MDRaisedButton(text="Back to Home", size_hint_y=None, height='48dp', pos_hint={'center_x': 0.5,'center_y': 0.4}, on_release=lambda x: self.back())
            screen.add_widget(btn)
            screen.add_widget(label)
            self.index = 0
            self.score = 0
if __name__ == '__main__':
    MyApp().run()