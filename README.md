# Password Manager

![Badge de Status](https://img.shields.io/badge/status-completo-brightgreen) ![Python](https://img.shields.io/badge/python-3.x-blue)

Solução criada com o intuito de facilitar o gerenciamento de nossas senhas! :ok_hand:

---

## :pushpin: Índice
1. [Sobre](#sobre)
2. [Instalação](#instalação)
3. [Como Usar](#como-usar)
4. [Tecnologias Utilizadas](#tecnologias-utilizadas)

---

## Sobre

Temos tantas coisas para lembrar hoje em dia, certo? Entre elas, a infinidade de senhas que precisamos para acessar diversos sites e serviços, cada uma exigindo combinações únicas e seguras. 

Este projeto foi criado justamente para auxiliar nisso. Com ele, você pode salvar suas senhas de forma segura, utilizando criptografia e chaves de acesso geradas "aleatoriamente" (só não se esqueça de guardá-las bem!). 
Este gerenciador ajuda a reduzir o estresse de memorizar senhas, garantindo que elas fiquem seguras e acessíveis apenas para você.

---

## Instalação

```bash
# Clone este repositório
git clone https://github.com/Marcos-Boas/Password-Manager.git

# Navegue até o diretório do projeto
cd Password-Manager

# Crie um ambiente virtual (opcional, mas recomendado)
python -m venv venv

# Caso de um erro no comando interior, tente essas alternativas e volte a tentar executá-lo
# Linux:                              # Windows:
source venv/bin/activate              venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```


## Como usar

```bash
# Execute o script principal do projeto
python templates/template.py
```


## Tecnologias Utilizadas

- **string**: Biblioteca nativa do Python para manipulação de strings.
- **secrets**: Gera números aleatórios criptograficamente seguros.
- **hashlib**: Oferece funções de hash, como MD5 e SHA-1, para criar resumos de mensagens.
- **base64**: Codifica e decodifica dados em Base16, Base32, Base64 e Base85.
- **pathlib**: Facilita a manipulação de diretórios e caminhos de arquivos.
- **cryptography (Fernet)**: Biblioteca externa que permite a criptografia de dados de forma segura.
