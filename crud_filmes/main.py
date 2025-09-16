<<<<<<< HEAD
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty, StringProperty
from database import DatabaseManager

class FilmeItem(BoxLayout):
    filme_id = NumericProperty()
    titulo = StringProperty()
    genero = StringProperty()
    ano = NumericProperty()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 60
        self.spacing = 10
        
        self.add_widget(Label(text=self.titulo, size_hint_x=0.4))
        self.add_widget(Label(text=self.genero, size_hint_x=0.3))
        self.add_widget(Label(text=str(self.ano), size_hint_x=0.2))
        
        btn_editar = Button(text='Editar', size_hint_x=0.1)
        btn_editar.bind(on_release=lambda x: App.get_running_app().editar_filme(self.filme_id))
        self.add_widget(btn_editar)
        
        btn_excluir = Button(text='Excluir', size_hint_x=0.1)
        btn_excluir.bind(on_release=lambda x: App.get_running_app().deletar_filme(self.filme_id))
        self.add_widget(btn_excluir)

class CadastroScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        layout.add_widget(Label(text='Cadastro de Filme', font_size=24))
        
        form_layout = BoxLayout(orientation='vertical', spacing=10)
        
        form_layout.add_widget(Label(text='Título:'))
        self.titulo_input = TextInput(multiline=False, size_hint_y=None, height=40)
        form_layout.add_widget(self.titulo_input)
        
        form_layout.add_widget(Label(text='Gênero:'))
        self.genero_input = TextInput(multiline=False, size_hint_y=None, height=40)
        form_layout.add_widget(self.genero_input)
        
        form_layout.add_widget(Label(text='Ano:'))
        self.ano_input = TextInput(multiline=False, input_filter='int', size_hint_y=None, height=40)
        form_layout.add_widget(self.ano_input)
        
        layout.add_widget(form_layout)
        
        btn_layout = BoxLayout(size_hint_y=0.2, spacing=10)
        btn_salvar = Button(text='Salvar')
        btn_salvar.bind(on_release=lambda x: self.salvar_filme())
        btn_layout.add_widget(btn_salvar)
        
        btn_voltar = Button(text='Voltar para Lista')
        btn_voltar.bind(on_release=lambda x: App.get_running_app().mudar_tela('listagem'))
        btn_layout.add_widget(btn_voltar)
        
        layout.add_widget(btn_layout)
        self.add_widget(layout)
    
    def salvar_filme(self):
        titulo = self.titulo_input.text.strip()
        genero = self.genero_input.text.strip()
        ano_text = self.ano_input.text.strip()
        
        if titulo and genero and ano_text:
            try:
                ano = int(ano_text)
                app = App.get_running_app()
                app.db.adicionar_filme(titulo, genero, ano)
                
                self.titulo_input.text = ''
                self.genero_input.text = ''
                self.ano_input.text = ''
                
                app.mudar_tela('listagem')
                app.carregar_filmes()
            except ValueError:
                pass

class ListagemScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Busca
        busca_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        self.busca_input = TextInput(hint_text='Buscar por título...', multiline=False, size_hint_x=0.7)
        busca_layout.add_widget(self.busca_input)
        
        btn_buscar = Button(text='Buscar', size_hint_x=0.3)
        btn_buscar.bind(on_release=lambda x: self.buscar_filmes())
        busca_layout.add_widget(btn_buscar)
        self.layout.add_widget(busca_layout)
        
        # Lista de filmes
        self.scroll = ScrollView()
        self.filmes_container = GridLayout(cols=1, size_hint_y=None, spacing=5)
        self.filmes_container.bind(minimum_height=self.filmes_container.setter('height'))
        self.scroll.add_widget(self.filmes_container)
        self.layout.add_widget(self.scroll)
        
        # Botões
        btn_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        btn_novo = Button(text='Novo Filme')
        btn_novo.bind(on_release=lambda x: App.get_running_app().mudar_tela('cadastro'))
        btn_layout.add_widget(btn_novo)
        
        btn_ordenar = Button(text='Ordenar por Ano')
        btn_layout.add_widget(btn_ordenar)
        
        self.layout.add_widget(btn_layout)
        self.add_widget(self.layout)
    
    def on_enter(self):
        self.carregar_filmes()
    
    def carregar_filmes(self, busca=None):
        app = App.get_running_app()
        filmes = app.db.listar_filmes(busca)
        
        self.filmes_container.clear_widgets()
        
        # Cabeçalho
        header = BoxLayout(size_hint_y=None, height=40, orientation='horizontal', spacing=10)
        header.add_widget(Label(text='Título', size_hint_x=0.4))
        header.add_widget(Label(text='Gênero', size_hint_x=0.3))
        header.add_widget(Label(text='Ano', size_hint_x=0.2))
        header.add_widget(Label(text='Ações', size_hint_x=0.2))
        self.filmes_container.add_widget(header)
        
        # Filmes
        for filme in filmes:
            item = FilmeItem(filme_id=filme[0], titulo=filme[1], genero=filme[2], ano=filme[3])
            self.filmes_container.add_widget(item)
    
    def buscar_filmes(self):
        busca = self.busca_input.text.strip()
        self.carregar_filmes(busca if busca else None)

class EdicaoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.filme_id = None
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        layout.add_widget(Label(text='Editar Filme', font_size=24))
        
        form_layout = BoxLayout(orientation='vertical', spacing=10)
        
        form_layout.add_widget(Label(text='Título:'))
        self.titulo_edit = TextInput(multiline=False, size_hint_y=None, height=40)
        form_layout.add_widget(self.titulo_edit)
        
        form_layout.add_widget(Label(text='Gênero:'))
        self.genero_edit = TextInput(multiline=False, size_hint_y=None, height=40)
        form_layout.add_widget(self.genero_edit)
        
        form_layout.add_widget(Label(text='Ano:'))
        self.ano_edit = TextInput(multiline=False, input_filter='int', size_hint_y=None, height=40)
        form_layout.add_widget(self.ano_edit)
        
        layout.add_widget(form_layout)
        
        btn_layout = BoxLayout(size_hint_y=0.2, spacing=10)
        btn_atualizar = Button(text='Atualizar')
        btn_atualizar.bind(on_release=lambda x: self.atualizar_filme())
        btn_layout.add_widget(btn_atualizar)
        
        btn_cancelar = Button(text='Cancelar')
        btn_cancelar.bind(on_release=lambda x: App.get_running_app().mudar_tela('listagem'))
        btn_layout.add_widget(btn_cancelar)
        
        layout.add_widget(btn_layout)
        self.add_widget(layout)
    
    def on_pre_enter(self):
        if self.filme_id:
            app = App.get_running_app()
            filme = app.db.obter_filme(self.filme_id)
            if filme:
                self.titulo_edit.text = filme[1]
                self.genero_edit.text = filme[2]
                self.ano_edit.text = str(filme[3])
    
    def atualizar_filme(self):
        titulo = self.titulo_edit.text.strip()
        genero = self.genero_edit.text.strip()
        ano_text = self.ano_edit.text.strip()
        
        if titulo and genero and ano_text:
            try:
                ano = int(ano_text)
                app = App.get_running_app()
                app.db.editar_filme(self.filme_id, titulo, genero, ano)
                app.mudar_tela('listagem')
                app.carregar_filmes()
            except ValueError:
                pass

class MovieCRUDApp(App):
    def build(self):
        self.db = DatabaseManager()
        self.sm = ScreenManager()
        
        self.sm.add_widget(ListagemScreen(name='listagem'))
        self.sm.add_widget(CadastroScreen(name='cadastro'))
        self.sm.add_widget(EdicaoScreen(name='edicao'))
        
        return self.sm
    
    def mudar_tela(self, nome_tela, **kwargs):
        if nome_tela == "edicao" and 'filme_id' in kwargs:
            self.sm.get_screen('edicao').filme_id = kwargs['filme_id']
        self.sm.current = nome_tela
    
    def carregar_filmes(self):
        self.sm.get_screen('listagem').carregar_filmes()
    
    def editar_filme(self, filme_id):
        self.mudar_tela("edicao", filme_id=filme_id)
    
    def deletar_filme(self, filme_id):
        self.db.deletar_filme(filme_id)
        self.carregar_filmes()

if __name__ == '__main__':
=======
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty, StringProperty
from database import DatabaseManager

class FilmeItem(BoxLayout):
    filme_id = NumericProperty()
    titulo = StringProperty()
    genero = StringProperty()
    ano = NumericProperty()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 60
        self.spacing = 10
        
        self.add_widget(Label(text=self.titulo, size_hint_x=0.4))
        self.add_widget(Label(text=self.genero, size_hint_x=0.3))
        self.add_widget(Label(text=str(self.ano), size_hint_x=0.2))
        
        btn_editar = Button(text='Editar', size_hint_x=0.1)
        btn_editar.bind(on_release=lambda x: App.get_running_app().editar_filme(self.filme_id))
        self.add_widget(btn_editar)
        
        btn_excluir = Button(text='Excluir', size_hint_x=0.1)
        btn_excluir.bind(on_release=lambda x: App.get_running_app().deletar_filme(self.filme_id))
        self.add_widget(btn_excluir)

class CadastroScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        layout.add_widget(Label(text='Cadastro de Filme', font_size=24))
        
        form_layout = BoxLayout(orientation='vertical', spacing=10)
        
        form_layout.add_widget(Label(text='Título:'))
        self.titulo_input = TextInput(multiline=False, size_hint_y=None, height=40)
        form_layout.add_widget(self.titulo_input)
        
        form_layout.add_widget(Label(text='Gênero:'))
        self.genero_input = TextInput(multiline=False, size_hint_y=None, height=40)
        form_layout.add_widget(self.genero_input)
        
        form_layout.add_widget(Label(text='Ano:'))
        self.ano_input = TextInput(multiline=False, input_filter='int', size_hint_y=None, height=40)
        form_layout.add_widget(self.ano_input)
        
        layout.add_widget(form_layout)
        
        btn_layout = BoxLayout(size_hint_y=0.2, spacing=10)
        btn_salvar = Button(text='Salvar')
        btn_salvar.bind(on_release=lambda x: self.salvar_filme())
        btn_layout.add_widget(btn_salvar)
        
        btn_voltar = Button(text='Voltar para Lista')
        btn_voltar.bind(on_release=lambda x: App.get_running_app().mudar_tela('listagem'))
        btn_layout.add_widget(btn_voltar)
        
        layout.add_widget(btn_layout)
        self.add_widget(layout)
    
    def salvar_filme(self):
        titulo = self.titulo_input.text.strip()
        genero = self.genero_input.text.strip()
        ano_text = self.ano_input.text.strip()
        
        if titulo and genero and ano_text:
            try:
                ano = int(ano_text)
                app = App.get_running_app()
                app.db.adicionar_filme(titulo, genero, ano)
                
                self.titulo_input.text = ''
                self.genero_input.text = ''
                self.ano_input.text = ''
                
                app.mudar_tela('listagem')
                app.carregar_filmes()
            except ValueError:
                pass

class ListagemScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Busca
        busca_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        self.busca_input = TextInput(hint_text='Buscar por título...', multiline=False, size_hint_x=0.7)
        busca_layout.add_widget(self.busca_input)
        
        btn_buscar = Button(text='Buscar', size_hint_x=0.3)
        btn_buscar.bind(on_release=lambda x: self.buscar_filmes())
        busca_layout.add_widget(btn_buscar)
        self.layout.add_widget(busca_layout)
        
        # Lista de filmes
        self.scroll = ScrollView()
        self.filmes_container = GridLayout(cols=1, size_hint_y=None, spacing=5)
        self.filmes_container.bind(minimum_height=self.filmes_container.setter('height'))
        self.scroll.add_widget(self.filmes_container)
        self.layout.add_widget(self.scroll)
        
        # Botões
        btn_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        btn_novo = Button(text='Novo Filme')
        btn_novo.bind(on_release=lambda x: App.get_running_app().mudar_tela('cadastro'))
        btn_layout.add_widget(btn_novo)
        
        btn_ordenar = Button(text='Ordenar por Ano')
        btn_layout.add_widget(btn_ordenar)
        
        self.layout.add_widget(btn_layout)
        self.add_widget(self.layout)
    
    def on_enter(self):
        self.carregar_filmes()
    
    def carregar_filmes(self, busca=None):
        app = App.get_running_app()
        filmes = app.db.listar_filmes(busca)
        
        self.filmes_container.clear_widgets()
        
        # Cabeçalho
        header = BoxLayout(size_hint_y=None, height=40, orientation='horizontal', spacing=10)
        header.add_widget(Label(text='Título', size_hint_x=0.4))
        header.add_widget(Label(text='Gênero', size_hint_x=0.3))
        header.add_widget(Label(text='Ano', size_hint_x=0.2))
        header.add_widget(Label(text='Ações', size_hint_x=0.2))
        self.filmes_container.add_widget(header)
        
        # Filmes
        for filme in filmes:
            item = FilmeItem(filme_id=filme[0], titulo=filme[1], genero=filme[2], ano=filme[3])
            self.filmes_container.add_widget(item)
    
    def buscar_filmes(self):
        busca = self.busca_input.text.strip()
        self.carregar_filmes(busca if busca else None)

class EdicaoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.filme_id = None
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        layout.add_widget(Label(text='Editar Filme', font_size=24))
        
        form_layout = BoxLayout(orientation='vertical', spacing=10)
        
        form_layout.add_widget(Label(text='Título:'))
        self.titulo_edit = TextInput(multiline=False, size_hint_y=None, height=40)
        form_layout.add_widget(self.titulo_edit)
        
        form_layout.add_widget(Label(text='Gênero:'))
        self.genero_edit = TextInput(multiline=False, size_hint_y=None, height=40)
        form_layout.add_widget(self.genero_edit)
        
        form_layout.add_widget(Label(text='Ano:'))
        self.ano_edit = TextInput(multiline=False, input_filter='int', size_hint_y=None, height=40)
        form_layout.add_widget(self.ano_edit)
        
        layout.add_widget(form_layout)
        
        btn_layout = BoxLayout(size_hint_y=0.2, spacing=10)
        btn_atualizar = Button(text='Atualizar')
        btn_atualizar.bind(on_release=lambda x: self.atualizar_filme())
        btn_layout.add_widget(btn_atualizar)
        
        btn_cancelar = Button(text='Cancelar')
        btn_cancelar.bind(on_release=lambda x: App.get_running_app().mudar_tela('listagem'))
        btn_layout.add_widget(btn_cancelar)
        
        layout.add_widget(btn_layout)
        self.add_widget(layout)
    
    def on_pre_enter(self):
        if self.filme_id:
            app = App.get_running_app()
            filme = app.db.obter_filme(self.filme_id)
            if filme:
                self.titulo_edit.text = filme[1]
                self.genero_edit.text = filme[2]
                self.ano_edit.text = str(filme[3])
    
    def atualizar_filme(self):
        titulo = self.titulo_edit.text.strip()
        genero = self.genero_edit.text.strip()
        ano_text = self.ano_edit.text.strip()
        
        if titulo and genero and ano_text:
            try:
                ano = int(ano_text)
                app = App.get_running_app()
                app.db.editar_filme(self.filme_id, titulo, genero, ano)
                app.mudar_tela('listagem')
                app.carregar_filmes()
            except ValueError:
                pass

class MovieCRUDApp(App):
    def build(self):
        self.db = DatabaseManager()
        self.sm = ScreenManager()
        
        self.sm.add_widget(ListagemScreen(name='listagem'))
        self.sm.add_widget(CadastroScreen(name='cadastro'))
        self.sm.add_widget(EdicaoScreen(name='edicao'))
        
        return self.sm
    
    def mudar_tela(self, nome_tela, **kwargs):
        if nome_tela == "edicao" and 'filme_id' in kwargs:
            self.sm.get_screen('edicao').filme_id = kwargs['filme_id']
        self.sm.current = nome_tela
    
    def carregar_filmes(self):
        self.sm.get_screen('listagem').carregar_filmes()
    
    def editar_filme(self, filme_id):
        self.mudar_tela("edicao", filme_id=filme_id)
    
    def deletar_filme(self, filme_id):
        self.db.deletar_filme(filme_id)
        self.carregar_filmes()

if __name__ == '__main__':
>>>>>>> a7aec5f38ed1b4deb063b16a25b4fccfbcb7daec
    MovieCRUDApp().run()