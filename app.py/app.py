from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView


class ToDoApp(App):
    def build(self):
        # Layout principal (vertical)
        self.layout_principal = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # Título
        titulo = Label(
            text="📋 Minha Lista de Tarefas",
            font_size=24,
            size_hint=(1, 0.2),
            bold=True,
            halign="center",
        )
        self.layout_principal.add_widget(titulo)

        # Campo de entrada
        self.input_tarefa = TextInput(
            hint_text="Digite uma nova tarefa",
            size_hint=(1, 0.2),
            multiline=False,
        )
        self.layout_principal.add_widget(self.input_tarefa)

        # Layout para botões
        layout_botoes = BoxLayout(size_hint=(1, 0.2), spacing=10)

        self.botao_adicionar = Button(text="Adicionar", background_color=(0, 0.6, 0, 1))
        self.botao_adicionar.bind(on_press=self.adicionar_tarefa)

        self.botao_limpar = Button(text="Limpar Lista", background_color=(0.8, 0, 0, 1))
        self.botao_limpar.bind(on_press=self.limpar_lista)

        layout_botoes.add_widget(self.botao_adicionar)
        layout_botoes.add_widget(self.botao_limpar)

        self.layout_principal.add_widget(layout_botoes)

        # Área de tarefas (com scroll)
        self.scroll = ScrollView(size_hint=(1, 0.6))
        self.lista_tarefas = BoxLayout(orientation="vertical", size_hint_y=None, spacing=5)
        self.lista_tarefas.bind(minimum_height=self.lista_tarefas.setter("height"))
        self.scroll.add_widget(self.lista_tarefas)

        self.layout_principal.add_widget(self.scroll)

        return self.layout_principal

    def adicionar_tarefa(self, instance):
        texto = self.input_tarefa.text.strip()
        if texto:  # Verifica se não está vazio
            nova_tarefa = Label(
                text=f"• {texto}",
                font_size=18,
                size_hint_y=None,
                height=40,
                halign="left",
                valign="middle",
            )
            nova_tarefa.bind(size=nova_tarefa.setter("text_size"))
            self.lista_tarefas.add_widget(nova_tarefa)
            self.input_tarefa.text = ""  # Limpa o campo após adicionar
        else:
            aviso = Label(
                text="⚠️ Insira uma tarefa válida!",
                color=(1, 0, 0, 1),
                font_size=16,
                size_hint_y=None,
                height=30,
            )
            self.lista_tarefas.add_widget(aviso)

    def limpar_lista(self, instance):
        self.lista_tarefas.clear_widgets()


if __name__ == "__main__":
    ToDoApp().run()
