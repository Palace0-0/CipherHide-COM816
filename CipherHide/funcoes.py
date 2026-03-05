from cryptography.fernet import Fernet

def gerarChave(tipo):

    #Gera uma chave simétrica
    if tipo == "ASE":
     key = Fernet.generate_key()
     print("Chave simétrica gerada!")
     return key