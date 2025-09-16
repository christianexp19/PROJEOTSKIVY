import tkinter as tk
from tkinter import messagebox

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - Desktop")
        self.root.geometry("400x500")
        self.root.configure(bg="#f4f6f9")
        self.root.resizable(False, False)

        # ======= Título =======
        tk.Label(root, text="🔑 Entrar", font=("Arial", 22, "bold"),
                 bg="#f4f6f9", fg="#333").pack(pady=25)

        # ======= Email =======
        self.criar_campo("Email:", "exemplo@exemplo.com")
        self.email_entry = self.entrada

        # ======= Senha =======
        self.criar_campo("Senha:", "", show="*")
        self.senha_entry = self.entrada

        # ======= Checkbox =======
        self.var_check = tk.BooleanVar()
        tk.Checkbutton(root, text="Não sou um robô", variable=self.var_check,
                       bg="#f4f6f9", font=("Arial", 11)).pack(pady=10)

        # ======= Botão Entrar =======
        self.botao_estilizado("Entrar", self.fazer_login, "#e63946").pack(pady=20)

        # ======= Links =======
        frame_links = tk.Frame(root, bg="#f4f6f9")
        frame_links.pack(pady=15)

        tk.Button(frame_links, text="Criar conta", font=("Arial", 10, "underline"),
                  fg="#0077b6", bg="#f4f6f9", bd=0, cursor="hand2",
                  command=self.criar_conta).grid(row=0, column=0, padx=25)

        tk.Button(frame_links, text="Recuperar senha", font=("Arial", 10, "underline"),
                  fg="#0077b6", bg="#f4f6f9", bd=0, cursor="hand2",
                  command=self.recuperar_senha).grid(row=0, column=1, padx=25)

        # Rodapé
        tk.Label(root, text="Sistema de Login - Desktop App", bg="#f4f6f9",
                 fg="#888", font=("Arial", 9)).pack(side="bottom", pady=15)

    # ======= Funções auxiliares =======
    def criar_campo(self, texto, placeholder, show=""):
        tk.Label(self.root, text=texto, font=("Arial", 12, "bold"),
                 bg="#f4f6f9", anchor="w").pack(fill="x", padx=40, pady=(10, 0))
        self.entrada = tk.Entry(self.root, font=("Arial", 12),
                                relief="solid", bd=1, show=show)
        self.entrada.insert(0, placeholder)
        self.entrada.pack(fill="x", padx=40, pady=5, ipady=6)

    def botao_estilizado(self, texto, comando, cor):
        btn = tk.Button(self.root, text=texto, command=comando,
                        bg=cor, fg="white", font=("Arial", 12, "bold"),
                        activebackground="#222", activeforeground="white",
                        relief="flat", width=15, height=2, cursor="hand2")
        return btn

    # ======= Funções principais =======
    def fazer_login(self):
        email = self.email_entry.get()
        senha = self.senha_entry.get()

        if not self.var_check.get():
            messagebox.showwarning("Aviso", "Marque a opção 'Não sou um robô'.")
            return

        if email == "admin@teste.com" and senha == "1234":
            messagebox.showinfo("Sucesso", "✅ Login realizado com sucesso!")
        else:
            messagebox.showerror("Erro", "❌ Email ou senha inválidos.")

    def criar_conta(self):
        messagebox.showinfo("Criar conta", "📌 Redirecionando para cadastro...")

    def recuperar_senha(self):
        messagebox.showinfo("Recuperar Senha", "📧 Enviamos instruções para seu e-mail.")

# ======= Executar =======
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
