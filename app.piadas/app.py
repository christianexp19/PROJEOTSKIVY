import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

# Cor de fundo da janela
Window.clearcolor = (0.15, 0.15, 0.2, 1)

# Lista de piadas em português
PIADAS = [
    "Por que o livro de matemática ficou triste? Porque tinha muitos problemas.",
    "Qual é o animal mais antigo do mundo? A zebra, porque é em preto e branco.",
    "O que o zero disse para o oito? Belo cinto!",
    "Por que o computador foi ao médico? Porque pegou um vírus.",
    "Qual é o cúmulo do basquete? Jogar a bola fora de casa.",
    "O que o tomate foi fazer no banco? Tirar extrato.",
    "Por que o lápis foi para o hospital? Porque estava sem ponta."
]

class PiadaApp(App):
    def build(self):
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        # Texto inicial
        self.label = Label(
            text="Clique no botão para ver uma piada 😂",
            font_size=20,
            halign="center",
            valign="middle"
        )
        self.label.bind(size=self.label.setter('text_size'))  # centralizar texto

        # Botão para mostrar piada
        self.button = Button(
            text="Mostrar Piada",
            size_hint=(1, 0.2),
            background_color=(0.2, 0.6, 0.9, 1)
        )
        self.button.bind(on_press=self.mostrar_piada)

        # Adiciona os widgets no layout
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.button)

        return self.layout

    def mostrar_piada(self, instance):
        # Sorteia uma piada da lista
        piada = random.choice(PIADAS)
        self.label.text = piada

if __name__ == "__main__":
    PiadaApp().run()
