from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
import random

class FilmeLayout(BoxLayout):
    nome_input = ObjectProperty(None)
    resultado = ObjectProperty(None)
    capa_filme = ObjectProperty(None)
    historico_label = ObjectProperty(None)
    historico = []

    filmes = [
        {"titulo": "Duna", "ano": 2021, "genero": "Ficção Científica", "imagem": "duna.jpg"},
        {"titulo": "Tudo em Todo Lugar ao Mesmo Tempo", "ano": 2022, "genero": "Ação/Comédia", "imagem": "tudo_em_todo_lugar.jpg"},
        {"titulo": "Oppenheimer", "ano": 2023, "genero": "Drama Histórico", "imagem": "oppenheimer.jpg"},
        {"titulo": "Barbie", "ano": 2023, "genero": "Comédia/Fantasia", "imagem": "barbie.jpg"},
        {"titulo": "A Baleia", "ano": 2022, "genero": "Drama", "imagem": "a_baleia.jpg"},
        {"titulo": "Os Banshees de Inisherin", "ano": 2022, "genero": "Drama/Comédia", "imagem": "banshees.jpg"},
        {"titulo": "Top Gun: Maverick", "ano": 2022, "genero": "Ação", "imagem": "top_gun.jpg"},
        {"titulo": "RRR", "ano": 2022, "genero": "Ação/Aventura", "imagem": "rrr.jpg"},
        {"titulo": "Aftersun", "ano": 2022, "genero": "Drama", "imagem": "aftersun.jpg"},
        {"titulo": "O Menu", "ano": 2022, "genero": "Suspense/Sátira", "imagem": "o_menu.jpg"}
    ]

    def sugerir_filme(self):
        nome = self.nome_input.text.strip()
        if not nome:
            self.resultado.text = "[color=#FF6347]⚠️ Por favor, digite seu nome.[/color]"
            self.capa_filme.source = ""
            return

        filme = random.choice(self.filmes)
        mensagem = (
            f"[color=#00CED1]Olá, {nome}![/color]\n"
            f"[color=#FFD700]🎬 Sua sugestão de filme é:[/color]\n"
            f"[b]{filme['titulo']}[/b] ({filme['ano']}) - [i]{filme['genero']}[/i]"
        )
        self.resultado.text = mensagem
        self.capa_filme.source = f"assets/{filme['imagem']}"

        # Atualiza histórico
        entrada = f"{filme['titulo']} ({filme['ano']})"
        self.historico.append(entrada)
        if len(self.historico) > 5:
            self.historico.pop(0)
        self.historico_label.text = "📜 Histórico:\n" + "\n".join(self.historico)

class FilmeApp(App):
    def build(self):
        return FilmeLayout()

if __name__ == "__main__":
    FilmeApp().run()
