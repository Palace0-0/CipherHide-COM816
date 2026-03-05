from cryptography.fernet import Fernet

def gerar_chave(self):

    tipo = self.tipo.get()

    if tipo == "ASE":
        key = Fernet.generate_key().decode()

        self.entry_key.delete(0, "end")
        self.entry_key.insert(0, key)

        print("Chave simétrica gerada!")

        return key

    else:
        print("Gerar chave RSA ainda não implementado")