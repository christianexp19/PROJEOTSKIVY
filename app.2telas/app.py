import random
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.core.window import Window

# Cor de fundo geral
Window.clearcolor = (0.1, 0.1, 0.1, 1)

# ----------------------------
# Lista de filmes por gênero
# ----------------------------
FILMES = {
    "Ação": ["Duna", "Mad Max: Estrada da Fúria", "John Wick", "Oppenheimer"],
    "Comédia": ["As Branquelas", "Deadpool", "Tudo em Todo Lugar ao Mesmo Tempo", "Se Beber, Não Case"],
    "Animação": ["Toy Story", "Divertida Mente", "Shrek", "Homem-Aranha no Aranhaverso"]
}

# ----------------------------
# Tela 1: Boas-vindas
# ----------------------------
class TelaBoasVindas(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", spacing=20, padding=40)

        self.label = Label(
            text="Digite seu nome para continuar:",
            font_size=20,
            color=(1, 1, 1, 1)
        )

        self.nome_input = TextInput(
            hint_text="Seu nome",
            multiline=False,
            size_hint=(1, 0.3)
        )

        self.botao = Button(
            text="Continuar",
            size_hint=(1, 0.3),
            background_color=(0.2, 0.6, 0.9, 1)
        )
        self.botao.bind(on_press=self.ir_para_tela_filmes)

        layout.add_widget(self.label)
        layout.add_widget(self.nome_input)
        layout.add_widget(self.botao)

        self.add_widget(layout)

    def ir_para_tela_filmes(self, instance):
        nome_usuario = self.nome_input.text.strip()
        if nome_usuario:
            self.manager.get_screen("tela_filmes").definir_usuario(nome_usuario)
            self.manager.current = "tela_filmes"
        else:
            self.label.text = "⚠️ Digite um nome antes de continuar!"


# ----------------------------
# Tela 2: Sugestão de Filmes
# ----------------------------
class TelaFilmes(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", spacing=20, padding=40)

        self.boas_vindas = Label(
            text="Bem-vindo!",
            font_size=22,
            color=(1, 1, 0.5, 1)
        )

        self.spinner = Spinner(
            text="Escolha um gênero",
            values=["Ação", "Comédia", "Animação"],
            size_hint=(1, 0.3)
        )

        self.botao = Button(
            text="Sugerir Filme",
            size_hint=(1, 0.3),
            background_color=(0.4, 0.8, 0.4, 1)
        )
        self.botao.bind(on_press=self.sortear_filme)

        self.resultado = Label(
            text="",
            font_size=20,
            color=(1, 1, 1, 1)
        )

        layout.add_widget(self.boas_vindas)
        layout.add_widget(self.spinner)
        layout.add_widget(self.botao)
        layout.add_widget(self.resultado)

        self.add_widget(layout)

    def definir_usuario(self, nome):
        self.boas_vindas.text = f"🎬 Bem-vindo, {nome}!"

    def sortear_filme(self, instance):
        genero = self.spinner.text
        if genero in FILMES:
            filme = random.choice(FILMES[genero])
            self.resultado.text = f"👉 Filme sugerido: {filme}"
        else:
            self.resultado.text = "⚠️ Escolha um gênero primeiro!"


# ----------------------------
# ScreenManager
# ----------------------------
class GerenciadorTelas(ScreenManager):
    pass


# ----------------------------
# App Principal
# ----------------------------
class FilmeApp(App):
    def build(self):
        sm = GerenciadorTelas()
        sm.add_widget(TelaBoasVindas(name="tela_boas_vindas"))
        sm.add_widget(TelaFilmes(name="tela_filmes"))
        return sm


if __name__ == "__main__":
    FilmeApp().run()
