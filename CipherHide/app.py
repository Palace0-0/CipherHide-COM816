from cryptography.fernet import Fernet
import customtkinter as ctk
import funcoes as func

ctk.set_appearance_mode('dark')

app = ctk.CTk()
app.title('CipherHide')
app.geometry('600x600')


botao = ctk.CTkButton(
    app,
    text='Gerar chave',
    command=lambda: func.gerarChave("ASE")
)

botao.pack(pady=10)

app.mainloop()
# Cria objeto com a chave
# f = Fernet(key)
# print(key)
# token = f.encrypt(b"Apude e mulher")
# print(token)

# validation = input("Digite sua chave para descripitografar")

# if validation == key:
#     message = f.decrypt(token)
