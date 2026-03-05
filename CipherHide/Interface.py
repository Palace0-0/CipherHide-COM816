from cryptography.fernet import Fernet
import Funcoes as func
import customtkinter as ctk

ctk.set_appearance_mode("dark")


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("CipherHider")
        self.geometry("700x500")

        # =============================
        # GRID PRINCIPAL
        # =============================

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(0, weight=1)

        # =============================
        # FRAME ESQUERDO
        # =============================

        self.frame_esquerdo = ctk.CTkFrame(self)
        self.frame_esquerdo.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")

        self.frame_esquerdo.grid_columnconfigure(0, weight=1)
        self.frame_esquerdo.grid_rowconfigure(4, weight=1)

        titulo = ctk.CTkLabel(self.frame_esquerdo, text="Gerar chave", font=("Arial", 14))
        titulo.grid(row=0, column=0, sticky="w", padx=20, pady=(10, 5))

        #Checkboxs
        self.tipo = ctk.StringVar(value="ASE")

        self.radio_ase = ctk.CTkRadioButton(
            self.frame_esquerdo,
            text="ASE",
            variable=self.tipo,
            value="ASE"
        )
        self.radio_ase.grid(row=1, column=0, columnspan=2, padx=20, pady=5, sticky="ew")

        self.radio_rsa = ctk.CTkRadioButton(
            self.frame_esquerdo,
            text="RSA",
            variable=self.tipo,
            value="RSA"
        )
        self.radio_rsa.grid(row=2, column=0, columnspan=2, padx=20, pady=5, sticky="ew")

        #Botão
        self.btn_gerar = ctk.CTkButton(
            self.frame_esquerdo,
            text="Gerar chave",
            command=self.gerar_chave
        )
        self.btn_gerar.grid(row=3, column=0, columnspan=2, padx=20, pady=(10, 5), sticky="ew")

        # =============================
        # FRAME DIREITO
        # =============================

        self.frame_direito = ctk.CTkFrame(self)
        self.frame_direito.grid(row=0, column=1, padx=15, pady=15, sticky="nsew")

        self.frame_direito.grid_columnconfigure((0, 1), weight=1)
        self.frame_direito.grid_rowconfigure(8, weight=1)

        largura = 450

        # Mensagem
        label_msg = ctk.CTkLabel(self.frame_direito, text="Mensagem")
        label_msg.grid(row=0, column=0, sticky="w", padx=20, pady=(20, 5))

        self.entry_msg = ctk.CTkEntry(self.frame_direito, width=largura)
        self.entry_msg.grid(row=1, column=0, columnspan=2, padx=20, sticky="ew")

        # Chave 1
        label_key1 = ctk.CTkLabel(self.frame_direito, text="Chave 1")
        label_key1.grid(row=2, column=0, sticky="w", padx=20, pady=(15, 5))

        self.entry_key1 = ctk.CTkEntry(self.frame_direito, width=largura)
        self.entry_key1.grid(row=3, column=0, columnspan=2, padx=20, sticky="ew")

        # Chave 2
        label_key2 = ctk.CTkLabel(self.frame_direito, text="Chave 2")
        label_key2.grid(row=4, column=0, sticky="w", padx=20, pady=(15, 5))

        self.entry_key2 = ctk.CTkEntry(self.frame_direito, width=largura)
        self.entry_key2.grid(row=5, column=0, columnspan=2, padx=20, sticky="ew")
    

        # BOTÕES

        self.btn_cripto = ctk.CTkButton(
            self.frame_direito,
            text="Criptografar",
            command= lambda: func.cripitografar(self)
        )

        self.btn_cripto.grid(row=6, column=0, pady=20, padx=(20, 10), sticky="e")

        self.btn_decripto = ctk.CTkButton(
            self.frame_direito,
            text="Decriptografar",
            command=self.descriptografar
        )

        self.btn_decripto.grid(row=6, column=1, pady=20, padx=(10, 20), sticky="w")

        # RESULTADO

        label_result = ctk.CTkLabel(self.frame_direito, text="Resultado")
        label_result.grid(row=7, column=0, sticky="w", padx=20)

        self.text_result = ctk.CTkTextbox(self.frame_direito, height=120)
        self.text_result.grid(row=8, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")

    # =============================
    # FUNÇÕES
    # =============================

    def gerar_chave(self):
        func.gerar_chave(self)

    def criptografar(self):

        msg = self.entry_msg.get()
        key = self.entry_key1.get()

        try:

            f = Fernet(key.encode())
            token = f.encrypt(msg.encode())

            self.text_result.delete("0.0", "end")
            self.text_result.insert("0.0", token.decode())

        except Exception as e:

            self.text_result.delete("0.0", "end")
            self.text_result.insert("0.0", f"Erro: {e}")

    def descriptografar(self):

        msg = self.entry_msg.get()
        key = self.entry_key1.get()

        try:

            f = Fernet(key.encode())
            texto = f.decrypt(msg.encode())

            self.text_result.delete("0.0", "end")
            self.text_result.insert("0.0", texto.decode())

        except Exception as e:

            self.text_result.delete("0.0", "end")
            self.text_result.insert("0.0", f"Erro: {e}")


app = App()
app.mainloop()