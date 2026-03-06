import customtkinter as ctk
import Funcoes as func

ctk.set_appearance_mode("dark")


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("CipherHider")
        self.geometry("900x600")

        # =============================
        # GRID PRINCIPAL
        # =============================

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(0, weight=1)

        # =============================
        # FRAME ESQUERDO (GERAR CHAVE)
        # =============================

        self.frame_esquerdo = ctk.CTkFrame(self)
        self.frame_esquerdo.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")

        self.frame_esquerdo.grid_columnconfigure(0, weight=1)

        titulo = ctk.CTkLabel(self.frame_esquerdo, text="Gerar Chaves", font=("Arial", 16))
        titulo.grid(row=0, column=0, padx=20, pady=15)

        # tipo de criptografia
        self.tipo = ctk.StringVar(value="AES")

        self.radio_aes = ctk.CTkRadioButton(
            self.frame_esquerdo,
            text="AES (Simétrica)",
            variable=self.tipo,
            value="AES"
        )
        self.radio_aes.grid(row=1, column=0, padx=20, pady=5, sticky="w")

        self.radio_rsa = ctk.CTkRadioButton(
            self.frame_esquerdo,
            text="RSA (Assimétrica)",
            variable=self.tipo,
            value="RSA"
        )
        self.radio_rsa.grid(row=2, column=0, padx=20, pady=5, sticky="w")

        # chave pública / simétrica
        label_chave1 = ctk.CTkLabel(self.frame_esquerdo, text="Chave 1")
        label_chave1.grid(row=3, column=0, sticky="w", padx=20, pady=(20,5))

        self.entry_key1 = ctk.CTkEntry(self.frame_esquerdo)
        self.entry_key1.grid(row=4, column=0, padx=20, sticky="ew")

        # chave privada
        label_chave2 = ctk.CTkLabel(self.frame_esquerdo, text="Chave 2")
        label_chave2.grid(row=5, column=0, sticky="w", padx=20, pady=(20,5))

        self.entry_key2 = ctk.CTkEntry(self.frame_esquerdo)
        self.entry_key2.grid(row=6, column=0, padx=20, sticky="ew")

        # botão gerar
        self.btn_gerar = ctk.CTkButton(
            self.frame_esquerdo,
            text="Gerar chave",
            command=self.gerar_chave
        )
        self.btn_gerar.grid(row=7, column=0, padx=20, pady=25, sticky="ew")

        # =============================
        # FRAME DIREITO
        # =============================

        self.frame_direito = ctk.CTkFrame(self)
        self.frame_direito.grid(row=0, column=1, padx=15, pady=15, sticky="nsew")

        self.frame_direito.grid_rowconfigure(0, weight=1)
        self.frame_direito.grid_rowconfigure(1, weight=1)
        self.frame_direito.grid_columnconfigure(0, weight=1)

        # =============================
        # MÓDULO CRIPTOGRAFIA
        # =============================

        self.frame_crypto = ctk.CTkFrame(self.frame_direito)
        self.frame_crypto.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.frame_crypto.grid_columnconfigure((0,1), weight=1)

        titulo_crypto = ctk.CTkLabel(
            self.frame_crypto,
            text="Criptografia",
            font=("Arial",16)
        )
        titulo_crypto.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        largura = 400

        # mensagem
        label_msg = ctk.CTkLabel(self.frame_crypto, text="Mensagem")
        label_msg.grid(row=1, column=0, padx=20, pady=(10,5), sticky="w")

        self.entry_msg = ctk.CTkEntry(self.frame_crypto, width=largura)
        self.entry_msg.grid(row=2, column=0, columnspan=2, padx=20, sticky="ew")

        # chave usada
        label_key = ctk.CTkLabel(self.frame_crypto, text="Chave utilizada")
        label_key.grid(row=3, column=0, padx=20, pady=(15,5), sticky="w")

        self.entry_key_use = ctk.CTkEntry(self.frame_crypto, width=largura)
        self.entry_key_use.grid(row=4, column=0, columnspan=2, padx=20, sticky="ew")

        # botões
        self.btn_cripto = ctk.CTkButton(
            self.frame_crypto,
            text="Criptografar",
            command=lambda: func.cripitografar(self)
        )
        self.btn_cripto.grid(row=5, column=0, pady=20, padx=(20,10), sticky="e")

        self.btn_decripto = ctk.CTkButton(
            self.frame_crypto,
            text="Decriptografar",
            command=lambda: func.decripitografar(self)
        )
        self.btn_decripto.grid(row=5, column=1, pady=20, padx=(10,20), sticky="w")

        # resultado
        label_result = ctk.CTkLabel(self.frame_crypto, text="Resultado")
        label_result.grid(row=6, column=0, padx=20, sticky="w")

        self.result = ctk.CTkEntry(self.frame_crypto)
        self.result.grid(row=7, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

        # =============================
        # MÓDULO ESTEGANOGRAFIA
        # =============================

        self.frame_esteg = ctk.CTkFrame(self.frame_direito)
        self.frame_esteg.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.frame_esteg.grid_columnconfigure((0,1), weight=1)

        titulo_esteg = ctk.CTkLabel(
            self.frame_esteg,
            text="Esteganografia",
            font=("Arial",16)
        )
        titulo_esteg.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        # imagem
        label_img = ctk.CTkLabel(self.frame_esteg, text="Imagem")
        label_img.grid(row=1, column=0, padx=20, pady=(10,5), sticky="w")

        self.entry_imagem = ctk.CTkEntry(self.frame_esteg)
        self.entry_imagem.grid(row=2, column=0, columnspan=2, padx=20, sticky="ew")

        # mensagem secreta
        label_secret = ctk.CTkLabel(self.frame_esteg, text="Mensagem secreta")
        label_secret.grid(row=3, column=0, padx=20, pady=(15,5), sticky="w")

        self.entry_secret = ctk.CTkEntry(self.frame_esteg)
        self.entry_secret.grid(row=4, column=0, columnspan=2, padx=20, sticky="ew")

        # botões
        self.btn_esconder = ctk.CTkButton(
            self.frame_esteg,
            text="Esconder mensagem"
        )
        self.btn_esconder.grid(row=5, column=0, pady=20, padx=(20,10), sticky="e")

        self.btn_revelar = ctk.CTkButton(
            self.frame_esteg,
            text="Revelar mensagem"
        )
        self.btn_revelar.grid(row=5, column=1, pady=20, padx=(10,20), sticky="w")

        # resultado
        label_esteg_result = ctk.CTkLabel(self.frame_esteg, text="Resultado")
        label_esteg_result.grid(row=6, column=0, padx=20, sticky="w")

        self.result_esteg = ctk.CTkEntry(self.frame_esteg)
        self.result_esteg.grid(row=7, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

    # =============================
    # FUNÇÕES
    # =============================

    def gerar_chave(self):
        func.gerar_chave(self)


app = App()
app.mainloop()