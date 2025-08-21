from kivy.app import App
from kivy.uix.label import Label


class HelloWorldApp(App):
    def build(self):
        # Cria um rótulo centralizado com a mensagem
        return Label(text="Hello, World!",
                     font_size=32,      # tamanho da fonte
                     halign="center",   # alinhamento horizontal
                     valign="middle")   # alinhamento vertical


if __name__ == "__main__":
    HelloWorldApp().run()
