import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.core.window import Window

# Cor de fundo geral
Window.clearcolor = (0.1, 0.1, 0.1, 1)  # cinza escuro


class FilmeApp(App):
    def build(self):
        self.genero_escolhido = None  # armazena o gênero selecionado

        layout = BoxLayout(orientation="vertical", padding=25, spacing=15)

        # Campo para nome
        self.nome_input = TextInput(
            hint_text="Digite seu nome",
            multiline=False,
            size_hint=(1, 0.15),
            background_color=(0.2, 0.2, 0.2, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(1, 1, 1, 1),
            font_size=20
        )
        layout.add_widget(self.nome_input)

        # Label instruções
        layout.add_widget(Label(
            text="Escolha um gênero de filme:",
            size_hint=(1, 0.1),
            color=(1, 1, 1, 1),
            font_size=20
        ))

        # Seleção de gêneros com ToggleButton
        genero_layout = BoxLayout(size_hint=(1, 0.15), spacing=15)
        self.botoes_genero = []
        cores_genero = {
            "Ação": (0.8, 0.2, 0.2, 1),
            "Comédia": (0.2, 0.7, 0.2, 1),
            "Animação": (0.2, 0.5, 0.9, 1)
        }
        for genero in ["Ação", "Comédia", "Animação"]:
            btn = ToggleButton(
                text=genero,
                group="generos",
                font_size=18,
                background_normal="",
                background_color=cores_genero[genero],
                color=(1, 1, 1, 1)
            )
            btn.bind(on_press=self.set_genero)
            genero_layout.add_widget(btn)
            self.botoes_genero.append(btn)
        layout.add_widget(genero_layout)

        # Botão para sugerir filme
        btn_sugerir = Button(
            text="🎬 Sugerir Filme",
            size_hint=(1, 0.15),
            font_size=20,
            background_normal="",
            background_color=(0.1, 0.6, 1, 1),
            color=(1, 1, 1, 1)
        )
        btn_sugerir.bind(on_press=self.sugerir_filme)
        layout.add_widget(btn_sugerir)

        # Botão para limpar
        btn_limpar = Button(
            text="🧹 Limpar",
            size_hint=(1, 0.15),
            font_size=20,
            background_normal="",
            background_color=(1, 0.3, 0.3, 1),
            color=(1, 1, 1, 1)
        )
        btn_limpar.bind(on_press=self.limpar)
        layout.add_widget(btn_limpar)

        # Label de saída (resultado) - com markup habilitado
        self.resultado = Label(
            text="",
            size_hint=(1, 0.3),
            color=(1, 1, 0.6, 1),
            font_size=22,
            markup=True  #  permite usar [b] e [i]
        )
        layout.add_widget(self.resultado)

        return layout

    # Define o gênero escolhido
    def set_genero(self, instance):
        self.genero_escolhido = instance.text

    # Lógica de sugestão de filme
    def sugerir_filme(self, instance):
        nome = self.nome_input.text.strip()

        # Listas de filmes por gênero (nome + ano)
        filmes_acao = [("Matrix", 1999), ("John Wick", 2014), ("Mad Max: Estrada da Fúria", 2015)]
        filmes_comedia = [("As Branquelas", 2004), ("Se Beber, Não Case", 2009), ("Ace Ventura", 1994)]
        filmes_animacao = [("Toy Story", 1995), ("Shrek", 2001), ("Divertida Mente", 2015)]

        if nome == "":
            self.resultado.text = " Por favor, digite seu nome."
            return

        if not self.genero_escolhido:
            self.resultado.text = " Selecione um gênero antes."
            return

        if self.genero_escolhido == "Ação":
            filme, ano = random.choice(filmes_acao)
        elif self.genero_escolhido == "Comédia":
            filme, ano = random.choice(filmes_comedia)
        elif self.genero_escolhido == "Animação":
            filme, ano = random.choice(filmes_animacao)
        else:
            self.resultado.text = " Erro inesperado."
            return

        # Mensagem com negrito e itálico
        self.resultado.text = f"🎥 Olá, [b]{nome}[/b]! Sua sugestão de [b]{self.genero_escolhido}[/b] é: [i]{filme} ({ano})[/i]."

    # Limpa os campos
    def limpar(self, instance):
        self.nome_input.text = ""
        self.resultado.text = ""
        self.genero_escolhido = None
        for btn in self.botoes_genero:
            btn.state = "normal"


if __name__ == "__main__":
    FilmeApp().run()
