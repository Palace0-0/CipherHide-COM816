import random
import string

def gerar_arquivo(nome, tamanho_kb):

    tamanho = tamanho_kb * 1024  # bytes

    caracteres = string.ascii_letters + string.digits + " "

    texto = ''.join(random.choices(caracteres, k=tamanho))

    with open(nome, "w", encoding="utf-8") as f:
        f.write(texto)

    print(f"{nome} criado com {tamanho_kb} KB")


# gerar arquivos
gerar_arquivo("texto_1kb.txt", 1)
#gerar_arquivo("texto_100kb.txt", 100)