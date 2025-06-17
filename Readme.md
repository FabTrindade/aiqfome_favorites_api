# aiqfome_favorites_api

API RESTful para cadastro e gerenciamento de favoritos de clientes, construída com FastAPI, utilizando banco de dados PostgreSQL e SQLAlchemy ORM.

---

## Descrição breve

Este projeto é uma API de Favoritos de Clientes, onde é possível criar clientes, cadastrar produtos favoritos para esses clientes e listar os favoritos existentes.

A segurança de acesso é feita através de um token de autenticação simples, utilizando um header HTTP com um token definido via variável de ambiente.

---

## Tecnologias utilizadas

| Tecnologia         | Por quê?                                                          |
| :----------------- | :---------------------------------------------------------------- |
| **Python 3.x** | Linguagem base para desenvolvimento rápido de APIs.               |
| **FastAPI** | Framework moderno, rápido, com tipagem forte e documentação automática. |
| **Uvicorn** | Servidor ASGI de alto desempenho para executar a API FastAPI.     |
| **SQLAlchemy** | ORM para abstração de acesso ao banco de dados relacional.        |
| **PostgreSQL** | Banco de dados relacional robusto e open-source.                  |
| **Pydantic** | Validação de dados de entrada usando data models.                 |
| **dotenv** (python-dotenv) | Carregar as variáveis de ambiente a partir de um arquivo `.env`. |

---

## Como criar o banco de dados no PostgreSQL

Acesse o terminal do PostgreSQL ou use alguma ferramenta como pgAdmin.

Execute o comando SQL:

```sql
CREATE DATABASE aiqfome;
```

Obs: Por padrão, o projeto espera um banco com o nome aiqfome, mas você pode ajustar a variável de ambiente se quiser outro nome.


## Como configurar a variável de ambiente (.env)
Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:

```
DATABASE_URL=postgresql://<seu_usuario>:<sua_senha>@localhost:5432/aiqfome
API_TOKEN=seutokenseguro
```
## Como criar o ambiente virtual Python
Passo a passo:

1) Abra o terminal na raiz do projeto.

2) Crie o ambiente virtual:

Windows:
```Bash

python -m venv venv
```
Linux/macOS:
```Bash
python3 -m venv venv
```
3) Ative o ambiente virtual:

Windows:
```Bash
venv\Scripts\activate
```
Linux/macOS:
```Bash
source venv/bin/activate
```
4) Instale as dependências com o ambiente virtual ativado:

```Bash
pip install -r requirements.txt
```

## Como rodar a API utilizando o Uvicorn
Com o ambiente virtual ativado e as dependências instaladas, execute:

```Bash
uvicorn app.main:app --reload
```
O --reload ativa o modo de recarga automática para desenvolvimento.

A API ficará disponível em:

http://127.0.0.1:8000

## Testando a API
### Acessando a documentação interativa
Após iniciar a API, você pode acessar a documentação gerada automaticamente pelo FastAPI nos seguintes endereços:

Swagger UI: http://127.0.0.1:8000/docs#/

Redoc: http://127.0.0.1:8000/redoc

---

### Testando com o Postman

#### Configuração da aba Authorization:
No Postman, em cada requisição:

Vá em:

Authorization -> Type: Bearer Token
Token: Coloque o valor da variável API_TOKEN que você configurou no .env.

Exemplos de URLs para testar os endpoints:

| Método | Endpoint                          | Descrição                             |
|--------|---------------------------------|-------------------------------------|
| POST   | /clients/                       | Criar um novo cliente                |
| POST   | /clients/{client_id}/favorites/ | Adicionar um produto favorito para o cliente |
| GET    | /clients/{client_id}/favorites/ | Listar os favoritos de um cliente específico  |



#### Exemplo prático de requisição no Postman:

**Criar Cliente:**
```
URL:
http://127.0.0.1:8000/clients/
Method: POST

Authorization: Bearer Token (conforme explicado acima)

Body (JSON):

JSON

{
  "name": "João Silva",
  "email": "joao.silva@example.com"
}
```
**Cadastrar Produto Favorito para um Cliente:**

```
URL:
http://127.0.0.1:8000/clients/1/favorites/
(Substitua 1 pelo ID real do cliente que você criou)

Method: POST

Authorization: Bearer Token

Body (JSON):

JSON

{
  "product_id": 123
}
```
**Listar Favoritos de um Cliente:**
```
URL:
http://127.0.0.1:8000/clients/1/favorites/
(Substitua 1 pelo ID do cliente)

Method: GET

Authorization: Bearer Token
```

⚠️ Observação Importante: Autenticação
Todas as requisições que exigem autenticação precisam do header Authorization com o token definido no .env.

Exemplo:

Se o token enviado for incorreto ou ausente, a API retornará:

```JSON
{
  "detail": "Invalid or missing token"
}
```
## ✅ Funcionalidades principais
* Criar cliente

* Adicionar produto favorito ao cliente

* Listar favoritos de um cliente específico

* Autenticação via token simples
