from cryptography.fernet import Fernet
import Funcoes as func
import customtkinter as ctk

ctk.set_appearance_mode("dark")

class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("CipherHider")
        self.geometry("700x350")

        # configuração da grid principal
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(0, weight=1)

        # =============================
        # FRAME ESQUERDO (GERAR CHAVE)
        # =============================
        self.frame_esquerdo = ctk.CTkFrame(self)
        self.frame_esquerdo.grid(row=0, column=0, padx=10, pady=10, sticky="ns")

        titulo = ctk.CTkLabel(self.frame_esquerdo, text="Gerar chave")
        titulo.pack(pady=10)

        self.tipo = ctk.StringVar(value="ASE")

        self.radio_ase = ctk.CTkRadioButton(
            self.frame_esquerdo,
            text="ASE",
            variable=self.tipo,
            value="ASE"
        )
        self.radio_ase.pack(pady=5)

        self.radio_rsa = ctk.CTkRadioButton(
            self.frame_esquerdo,
            text="RSA",
            variable=self.tipo,
            value="RSA"
        )
        self.radio_rsa.pack(pady=5)

        self.btn_gerar = ctk.CTkButton(
            self.frame_esquerdo,
            text="Gerar chave",
            command=lambda: func.gerar_chave(self)
        )

        self.btn_gerar.pack(pady = 10)

        # =============================
        # FRAME DIREITO (CRIPTOGRAFIA)
        # =============================
        self.frame_direito = ctk.CTkFrame(self)
        self.frame_direito.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        label_msg = ctk.CTkLabel(self.frame_direito, text="Mensagem")
        label_msg.pack(pady=5)

        self.entry_msg = ctk.CTkEntry(self.frame_direito, width=400)
        self.entry_msg.pack(pady=5)

        label_key = ctk.CTkLabel(self.frame_direito, text="Chave")
        label_key.pack(pady=5)

        self.entry_key = ctk.CTkEntry(self.frame_direito, width=400)
        self.entry_key.pack(pady=5)

        self.btn_cripto = ctk.CTkButton(
            self.frame_direito,
            text="Criptografar",
            command=self.criptografar
        )
        self.btn_cripto.pack(pady=20)

    # =============================
    # FUNÇÕES
    # =============================

 
    def criptografar(self):

        msg = self.entry_msg.get()
        key = self.entry_key.get()

        f = Fernet(key.encode())
        token = f.encrypt(msg.encode())

        print("Mensagem criptografada:")
        print(token)


app = App()
app.mainloop()


# Cria objeto com a chave
# f = Fernet(key)
# print(key)
# token = f.encrypt(b"Apude e mulher")
# print(token)

# validation = input("Digite sua chave para descripitografar")

# if validation == key:
#     message = f.decrypt(token)
