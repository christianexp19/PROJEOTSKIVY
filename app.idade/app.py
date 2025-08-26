from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

# ----------------------------
# Constantes para mensagens
# ----------------------------
MSG_CAMPOS_VAZIOS = "⚠️ Por favor, preencha todos os campos."
MSG_NUMERO_INVALIDO = "⚠️ Digite um número válido para idade."
MSG_IDADE_INVALIDA = "⚠️ Idade deve ser maior que 0 e menor que 130."
MSG_INICIAL = "Digite seu nome e idade, depois clique em Enviar."

# ----------------------------
# Regras de Negócio
# ----------------------------
def classificador_idade(nome: str, idade: int) -> str:
    """Retorna mensagem personalizada de acordo com a idade."""
    if idade < 18:
        return f"Olá, {nome}! Você é menor de idade."
    elif idade >= 60:
        return f"Olá, {nome}! Você é idoso e merece muito respeito ❤️."
    else:
        return f"Olá, {nome}! Você é maior de idade."


def validar_dados(nome: str, idade_texto: str) -> str:
    """Valida os dados recebidos e retorna a mensagem correspondente."""
    if not nome or not idade_texto:
        return MSG_CAMPOS_VAZIOS

    try:
        idade = int(idade_texto)
    except ValueError:
        return MSG_NUMERO_INVALIDO

    if idade <= 0 or idade > 130:
        return MSG_IDADE_INVALIDA

    return classificador_idade(nome, idade)


# ----------------------------
# Classe Principal
# ----------------------------
class IdadeLayout(BoxLayout):
    def verificar_idade(self):
        nome = self.ids.nome_input.text.strip()
        idade_texto = self.ids.idade_input.text.strip()
        self.ids.resultado.text = validar_dados(nome, idade_texto)


class IdadeApp(App):
    def build(self):
        self.title = "App de Idade e Acesso"
        return IdadeLayout()


if __name__ == "__main__":
    IdadeApp().run()
