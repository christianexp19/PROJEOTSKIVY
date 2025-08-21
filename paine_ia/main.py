import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty, BooleanProperty

kivy.require('2.0.0')

class AiControlPanel(BoxLayout):
    """
    Widget principal do painel de controle da IA.
    Define as propriedades e a lógica de interação.
    """
    ai_status = StringProperty('IA: Offline')
    threat_level = NumericProperty(0)
    ai_online = BooleanProperty(False)

    def toggle_ai_status(self, instance, value):
        """Alterna o status online/offline da IA."""
        self.ai_online = value
        if self.ai_online:
            self.ai_status = 'IA: Online, aguardando comando...'
            self.threat_level = 20  # Nível de ameaça inicial quando a IA está online
        else:
            self.ai_status = 'IA: Offline'
            self.threat_level = 0  # Nível de ameaça zero quando a IA está offline

    def send_command(self, instance):
        """Processa e envia o comando para a IA."""
        command = self.ids.command_input.text

        if self.ai_online and command:
            if 'capturar robô' in command.lower():
                self.ai_status = 'IA: Ação de captura iniciada. Nível de ameaça: CRÍTICO'
                self.threat_level = 80
            elif 'desligar' in command.lower():
                self.ai_status = 'IA: Iniciando desligamento...'
                self.ids.ai_toggle.active = False
            else:
                self.ai_status = f'IA: Comando "{command}" executado com sucesso.'
                self.threat_level = 50
        elif not self.ai_online:
            self.ai_status = 'IA: Offline. Não é possível enviar comando.'
        else:
            self.ai_status = 'IA: Por favor, digite um comando.'
        
        # Limpa o campo de entrada após enviar o comando
        self.ids.command_input.text = ''

class AtlasApp(App):
    """Classe principal da aplicação Kivy."""
    def build(self):
        return AiControlPanel()

if __name__ == '__main__':
    AtlasApp().run()