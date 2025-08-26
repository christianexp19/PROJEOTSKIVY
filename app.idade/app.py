from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class IdadeApp(App):
    def build(self):
        # Layout principal
        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        # Campo para o nome
        self.nome_input = TextInput(
            hint_text="Digite seu nome",
            multiline=False,
            size_hint=(1, 0.2)
        )
        layout.add_widget(self.nome_input)

        # Campo para a idade
        self.idade_input = TextInput(
            hint_text="Digite sua idade",
            multiline=False,
            input_filter="int",  # só aceita números
            size_hint=(1, 0.2)
        )
        layout.add_widget(self.idade_input)

        # Botão
        botao = Button(
            text="Enviar",
            size_hint=(1, 0.2),
            background_color=(0.2, 0.6, 1, 1)  # azul
        )
        botao.bind(on_press=self.verificar_idade)
        layout.add_widget(botao)

        # Label para mostrar a mensagem
        self.resultado = Label(
            text="",
            font_size=18,
            size_hint=(1, 0.4)
        )
        layout.add_widget(self.resultado)

        return layout

    def verificar_idade(self, instance):
        nome = self.nome_input.text.strip()
        idade_texto = self.idade_input.text.strip()

        # Validação
        if not nome or not idade_texto:
            self.resultado.text = "⚠️ Por favor, preencha todos os campos."
            return

        try:
            idade = int(idade_texto)
        except ValueError:
            self.resultado.text = "⚠️ Digite um número válido para idade."
            return

        # Condições
        if idade < 18:
            self.resultado.text = f"Olá, {nome}! Você é menor de idade."
        elif idade >= 60:
            self.resultado.text = f"Olá, {nome}! Você é idoso e merece muito respeito ❤️."
        else:
            self.resultado.text = f"Olá, {nome}! Você é maior de idade."


if __name__ == "__main__":
    IdadeApp().run()
