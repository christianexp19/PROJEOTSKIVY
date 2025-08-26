from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.label import Label

class IdadeLayout(BoxLayout):
    nome_input = ObjectProperty(None)
    idade_input = ObjectProperty(None)
    resultado = ObjectProperty(None)
    historico = ObjectProperty(None)

    def verificar_idade(self):
        nome = self.nome_input.text.strip()
        idade = self.idade_input.text.strip()

        if not nome or not idade:
            mensagem = "[color=#FFA500]⚠️ Por favor, preencha todos os campos.[/color]"
        else:
            try:
                idade = int(idade)
                if idade < 18:
                    mensagem = f"[color=#FF4444]{nome}, você é menor de idade.[/color]"
                else:
                    mensagem = f"[color=#44AA44]{nome}, você é maior de idade.[/color]"
            except ValueError:
                mensagem = "[color=#FFA500]⚠️ Idade inválida. Digite apenas números.[/color]"

        self.resultado.text = mensagem

        self.historico.add_widget(Label(
            text=mensagem,
            markup=True,
            font_size='14sp',
            size_hint_y=None,
            height=30
        ))

class IdadeApp(App):
    def build(self):
        return IdadeLayout()

if __name__ == "__main__":
    IdadeApp().run()
