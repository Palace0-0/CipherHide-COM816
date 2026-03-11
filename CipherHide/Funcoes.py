from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import tkinter
from tkinter import filedialog
import os
from stegano import lsb
import time

# -----------------------------
# FUNÇÕES CRIPITOGRAFIA
# -----------------------------

def gerar_chave(self):

    tipo = self.tipo.get()

    # 🔐 Criptografia Simétrica
    if tipo == "AES":

        key = Fernet.generate_key().decode()

        self.entry_key1.delete(0, "end")
        self.entry_key2.delete(0, "end")

        self.entry_key1.insert(0, key)

        print("Chave simétrica gerada!")

        return key

    # 🔐 Criptografia Assimétrica
    else:

        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )

        public_key = private_key.public_key()

        # serializar chave pública
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode()

        # serializar chave privada
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ).decode()

        self.entry_key1.delete(0, "end")
        self.entry_key2.delete(0, "end")

        self.entry_key1.insert(0, public_pem)
        self.entry_key2.insert(0, private_pem)

        print("Par de chaves RSA gerado!")


def cripitografar(self):

    msg = self.entry_msg.get()

    key = self.entry_key_use.get()
    
    inicio = time.time()

    # 🔐 SIMÉTRICA
    if key[0] != "-":
        
        f = Fernet(key.encode())

        token = f.encrypt(msg.encode())

        fim = time.time()
        tempo = fim - inicio
        print(f"Tempo AES: {tempo:.6f} segundos")

        self.entry_msg.delete(0, "end")
        self.result.delete(0, "end")

        self.result.insert(0, token.decode())

    # 🔐 ASSIMÉTRICA
    else:
        
        public_key = serialization.load_pem_public_key(
            key.encode()
        )

        ciphertext = public_key.encrypt(
            msg.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        fim = time.time()
        tempo = fim - inicio
        print(f"Tempo RSA: {tempo:.6f} segundos")

        self.entry_msg.delete(0, "end")
        self.result.delete(0, "end") 

        self.result.insert(0, ciphertext.hex())


def decripitografar(self):

    msg = self.entry_msg.get()

    key = self.entry_key_use.get()

    inicio = time.time()
    
    # 🔐 SIMÉTRICA
    if key[0] != "-":

        f = Fernet(key.encode())

        token = f.decrypt(msg.encode())

        fim = time.time()
        tempo = fim - inicio
        print(f"Tempo AES: {tempo:.6f} segundos")

        self.entry_msg.delete(0, "end")
        self.result.delete(0, "end")

        self.result.insert(0, token.decode())

    # 🔐 ASSIMÉTRICA
    else:

        private_key = serialization.load_pem_private_key(
            key.encode(),
            password=None
        )

        cipher = bytes.fromhex(msg)

        ciphertext = private_key.decrypt(
            cipher,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        fim = time.time()
        tempo = fim - inicio
        print(f"Tempo RSA: {tempo:.6f} segundos")

        self.entry_msg.delete(0, "end")
        self.result.delete(0, "end")

        self.result.insert(0, ciphertext.decode())


# -----------------------------
# FUNÇÕES ESTEGANOGRAFIA
# -----------------------------

def selecionar_arquivos(self):
    
    root = tkinter.Tk()
    root.withdraw()

    # Abre a janela para selecionar arquivo e retrona o caminho
    file_path = filedialog.askopenfilename(
        parent=root,
        initialdir=os.getcwd(),
        title="Please select a file",
        filetypes=[("Image files", "*.png"), ("Image files", "*.jpeg*"), ("All files", "*.*")]
    )

    if file_path:
        self.entry_imagem.delete(0,'end')
        self.entry_imagem.insert(0, file_path)
        
    else:
        print("No file selected.")


def esconder_imagem(self):

    file_path = self.entry_imagem.get()
    msg = self.entry_secret.get()

    inicio = time.time()

    if msg != "":
        secret = lsb.hide(file_path, msg)

        save_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[
                ("PNG Image", "*.png"),
                ("All files", "*.*")
            ],
            title="Salvar imagem com mensagem secreta"
        )

        if save_path:
            secret.save(save_path)

    fim = time.time()
    tempo = fim - inicio
    print(f"Tempo Esteganografia (esconder): {tempo:.6f} segundos")

    file_path = self.entry_imagem.get()
    msg = self.entry_secret.delete(0, 'end')


def revelar_imagem(self):
    
    file_path = self.entry_imagem.get()

    inicio = time.time()

    msg = lsb.reveal(file_path)

    fim = time.time()
    tempo = fim - inicio
    print(f"Tempo Esteganografia (revelar): {tempo:.6f} segundos")
    
    self.result_esteg.delete(0, 'end')
    self.result_esteg.insert(0, msg)