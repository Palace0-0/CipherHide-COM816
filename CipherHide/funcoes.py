from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

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
        self.entry_key.delete(0, "end")
        self.entry_key.insert(0, public_key)
        print(private_key)
        print("Gerar chave RSA ainda não implementado")

