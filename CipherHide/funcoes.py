from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes


def estado_campo(self, estado):

    if estado == 1:
        self.entry_key1.configure(state="readonly")
        self.entry_key2.configure(state="readonly")
    else:
        self.entry_key1.configure(state="normal")
        self.entry_key2.configure(state="normal")


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
    

    # 🔐 SIMÉTRICA
    if key[0] != "-":
        
        f = Fernet(key.encode())

        token = f.encrypt(msg.encode())

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

        self.entry_msg.delete(0, "end")
        self.result.delete(0, "end") 

        self.result.insert(0, ciphertext.hex())

def decripitografar(self):

    msg = self.entry_msg.get()

    key = self.entry_key_use.get()

    
    if key[0] != "-":

        f = Fernet(key.encode())

        token = f.decrypt(msg.encode())

        self.entry_msg.delete(0, "end")
        self.result.delete(0, "end")

        self.result.insert(0, token.decode())

    
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

        self.entry_msg.delete(0, "end")
        self.result.delete(0, "end")

        self.result.insert(0, ciphertext.decode())