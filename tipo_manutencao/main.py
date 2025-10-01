# Sistema de Gerenciamento de Contatos - Versão 1.0

class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

class GerenciadorContatos:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)
        print(f"Contato '{contato.nome}' adicionado com sucesso.")

    def listar_contatos(self):
        print("\n--- Lista de Contatos ---")
        if not self.contatos:
            print("Nenhum contato cadastrado.")
        else:
            for contato in self.contatos:
                print(f"Nome: {contato.nome}, Telefone: {contato.telefone}, Email: {contato.email}")
        print("------------------------\n")

# Uso do gerenciador
gerenciador = GerenciadorContatos()
gerenciador.adicionar_contato(Contato("Ana Silva", "11987654321", "ana.silva@email.com"))
gerenciador.adicionar_contato(Contato("Bruno Santos", "21912345678", "bruno.santos@email.com"))
gerenciador.adicionar_contato(Contato("Carlos Oliveira", "31998765432", "carlos.oliveira@email.com"))
gerenciador.listar_contatos()
