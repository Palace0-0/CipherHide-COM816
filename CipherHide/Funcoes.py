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

    # Chave Simétrica
    if tipo == "AES":

        #Gera uma chave aleatória e utiliza o decode para transformar em texto e não binário
        key = Fernet.generate_key().decode() 

        #Limpa os campos
        self.entry_key1.delete(0, "end")
        self.entry_key2.delete(0, "end")

        #Inseri a chave publica no primeiro campo
        self.entry_key1.insert(0, key)

        print("Chave simétrica gerada!")

        return key

    #Chave Assimétrica
    else:

        #Gera a chave privada, public_exponente é um variável referente ao calculo pro tras da cripitografia e key_size é o tamanho em bits
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )

        #A partir da chave privada gera a publica
        public_key = private_key.public_key()

        # Transformações das chaves para texto
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode()

        
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()#Chave não esta protegida por senha
        ).decode()

        #Limpeza e inserção de dados no campo
        self.entry_key1.delete(0, "end")
        self.entry_key2.delete(0, "end")

        self.entry_key1.insert(0, public_pem)
        self.entry_key2.insert(0, private_pem)

        print("Par de chaves RSA gerado!")


def cripitografar(self):

    #Buscando a mensager e a cahve para cripitografar
    msg = self.entry_msg.get()

    key = self.entry_key_use.get()
    
    inicio = time.time()

    # SIMÉTRICA
    if key[0] != "-":
        
        f = Fernet(key.encode()) #Transforma o texto em bytes e implementa fernet(AES + HMAC + timestamp)

        token = f.encrypt(msg.encode()) #mensagem vira bytes -> AES criptografa -> HMAC gera assinatura

        fim = time.time()
        tempo = fim - inicio
        print(f"Tempo AES: {tempo:.6f} segundos")

        #Imprime resultado da cripitografia
        self.entry_msg.delete(0, "end")
        self.result.delete(0, "end")

        self.result.insert(0, token.decode())

    #ASSIMÉTRICA
    else:
        
        #Transaforma o texto PEM devolta ao objeto RSA utilizavél
        public_key = serialization.load_pem_public_key(
            key.encode()
        )

        #Processo de cripitografia
        ciphertext = public_key.encrypt(
            msg.encode(),
            padding.OAEP( #Utilizase Optimal Asymmetric Encryption Padding pois RSA por padrão é vunerável
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        fim = time.time()
        tempo = fim - inicio
        print(f"Tempo RSA: {tempo:.6f} segundos")

        #Limpeza e inserção
        self.entry_msg.delete(0, "end")
        self.result.delete(0, "end") 

        self.result.insert(0, ciphertext.hex())


def decripitografar(self):

    #Buscando informações necessárias
    msg = self.entry_msg.get()

    key = self.entry_key_use.get()

    inicio = time.time()
    
    #SIMÉTRICA
    if key[0] != "-":

        f = Fernet(key.encode()) #Transforma a chave em bytes

        token = f.decrypt(msg.encode())#Fernet verifica assinatura HMAC -> valida intefridade -> Decripitografa

        fim = time.time()
        tempo = fim - inicio
        print(f"Tempo AES: {tempo:.6f} segundos")

        #Limpeza e inserção
        self.entry_msg.delete(0, "end")
        self.result.delete(0, "end")

        self.result.insert(0, token.decode())

    # ASSIMÉTRICA
    else:

        #Transforma chave privada em um objeto RSA utilizável
        private_key = serialization.load_pem_private_key(
            key.encode(),
            password=None #Aqui não coloca nada pois não passamos este parametro la em cima
        )

        #Transforma a mensagem de HEX para BYTES, pq o padrão PEM é HEX
        cipher = bytes.fromhex(msg)

        #Drcripitografa
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

        #Limpeza e inserção
        self.entry_msg.delete(0, "end")
        self.result.delete(0, "end")

        self.result.insert(0, ciphertext.decode())


# -----------------------------
# FUNÇÕES ESTEGANOGRAFIA
# -----------------------------

def selecionar_arquivos(self):
    
    #Gera e esconde a raiz do tkinter
    root = tkinter.Tk()
    root.withdraw()

    # Abre a janela para selecionar arquivo e retrona o caminho
    file_path = filedialog.askopenfilename(
        parent=root,
        initialdir=os.getcwd(),
        title="Please select a file",
        filetypes=[("Image files", "*.png"), ("Image files", "*.jpeg*"), ("All files", "*.*")]
    )

    #Se tiver um caminho então limpa e inseri
    if file_path:
        self.entry_imagem.delete(0,'end')
        self.entry_imagem.insert(0, file_path)
        
    else:
        print("No file selected.")


def esconder_imagem(self):

    #Buscando informações
    file_path = self.entry_imagem.get()
    msg = self.entry_secret.get()

    inicio = time.time()

    if msg != "":
        #Escondendo mensagem
        secret = lsb.hide(file_path, msg)

        #Mostra a tela para escolher onde sera salvo o arquivo
        save_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[
                ("PNG Image", "*.png"),
                ("All files", "*.*")
            ],
            title="Salvar imagem com mensagem secreta"
        )

        #Salvando na máquina do ser humano
        if save_path:
            secret.save(save_path)

    fim = time.time()
    tempo = fim - inicio
    print(f"Tempo Esteganografia (esconder): {tempo:.6f} segundos")

    #Limpeza e inserção
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