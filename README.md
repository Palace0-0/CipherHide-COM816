# CipherHider

Aplicação desenvolvida em Python para demonstrar conceitos de **criptografia e esteganografia**, criada para a disciplina **Segurança de Sistemas (COM816)**.

---

# Como rodar o projeto

1. Instale as dependências necessárias:

pip install cryptography  
pip install customtkinter  
pip install stegano  

2. Execute o programa:

python Interface.py

Após iniciar a aplicação, a interface gráfica será aberta e permitirá utilizar as funções de criptografia e esteganografia.

---

# Informações da disciplina

Disciplina: Segurança de Sistemas  
Código: COM816  
Professor: Sérgio Yoshioka  

Aluno: Gabriel Palace Novaes Henrique  

---

# Módulos do sistema

O sistema foi dividido em três módulos principais.

## 1. Geração de chaves criptográficas

Responsável por gerar chaves para os algoritmos de criptografia.

Funcionalidades:

- geração de chave **simétrica (AES/Fernet)**
- geração de par de chaves **assimétricas (RSA)**

As chaves geradas podem ser utilizadas posteriormente nos processos de criptografia e descriptografia.

---

## 2. Criptografia e Decriptografia

Este módulo permite proteger e recuperar mensagens utilizando as chaves geradas.

Funcionalidades:

- criptografia de mensagens
- descriptografia de mensagens
- utilização de **chave simétrica**
- utilização de **chave pública e privada**
- medição de tempo de execução

Observação: o algoritmo RSA possui limitação de tamanho de mensagem, permitindo criptografar apenas textos pequenos.

---

## 3. Esteganografia

Este módulo permite esconder mensagens dentro de imagens.

Funcionalidades:

- selecionar imagem
- esconder mensagem na imagem
- salvar imagem com a mensagem oculta
- revelar mensagem escondida
- medição de tempo de execução

A implementação utiliza a biblioteca `stegano`.

---

# Estrutura do projeto

CipherHider  
│  
├── Interface.py  
├── Funcoes.py  
└── README.md  

Interface.py → responsável pela interface gráfica utilizando CustomTkinter  
Funcoes.py → contém as funções de geração de chaves, criptografia, descriptografia e esteganografia  

---

# Bibliotecas utilizadas

- cryptography  
- customtkinter  
- stegano  
- tkinter  
- time  
