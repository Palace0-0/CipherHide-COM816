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

    if tipo == "ASE":
        key = Fernet.generate_key().decode()

        self.entry_key1.delete(0, "end")
        self.entry_key2.delete(0, "end")
        self.entry_key1.insert(0, key)

        print("Chave simétrica gerada!")

        return key

    else:
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )

        public_key = private_key.public_key()
        self.entry_key1.delete(0, "end")
        self.entry_key2.delete(0, "end")
        self.entry_key1.insert(0, public_key)
        self.entry_key2.insert(0, private_key)


def cripitografar (self):
    msg = self.entry_msg.get()
    key1 = self.entry_key1.get()
    key2= self.entry_key2.get()

    if key2 == "":
        print("ASE")
    else:
        print("RSA")