# Santander Dev Week 2023 – ETL com Python e IA Generativa

## 📌 Visão Geral

Este projeto foi desenvolvido como parte do desafio **Santander Dev Week 2023**, com o objetivo de demonstrar, de forma prática, a implementação de um **pipeline ETL (Extract, Transform, Load)** utilizando **Python** e **IA Generativa**.

O foco principal do desafio não é a ferramenta em si, mas o **entendimento do fluxo de dados**, desde a extração, passando pela transformação com Inteligência Artificial, até o carregamento do resultado final.

> ⚠️ Observação importante: a API oficial do desafio estava indisponível no momento do desenvolvimento. Por isso, foi adotada uma abordagem alternativa utilizando arquivos CSV locais, conforme orientação da própria DIO.

---

## 🎯 Objetivo do Projeto

* Ler dados de usuários a partir de um arquivo CSV (**Extract**)
* Enriquecer esses dados com mensagens de marketing personalizadas geradas por IA (**Transform**)
* Salvar o resultado final em um novo arquivo CSV (**Load**)

---

## 🧠 Conceitos Aplicados

* ETL (Extract, Transform, Load)
* Manipulação de dados com **Pandas**
* Integração com **OpenAI API** (IA Generativa)
* Tratamento de exceções e fallback automático
* Organização de código em camadas
* Boas práticas de estrutura de projeto em Python

---

## 🗂️ Estrutura do Projeto

```
santander-dev-week-etl/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── etl/
│   │   ├── __init__.py
│   │   ├── extract.py
│   │   ├── transform.py
│   │   └── load.py
│   └── services/
│       ├── __init__.py
│       └── openai_service.py
├── data/
│   ├── users.csv
│   └── users_with_messages.csv
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🔄 Fluxo ETL

### 1️⃣ Extract

Os dados são extraídos de um arquivo CSV local contendo informações básicas dos usuários.

Arquivo de entrada (`data/users.csv`):

```csv
name,account,card
João,12345,9999
Maria,67890,8888
Carlos,54321,7777
```

A leitura é feita utilizando a biblioteca **Pandas**.

---

### 2️⃣ Transform

Nesta etapa, os dados são enriquecidos com uma nova coluna chamada `message`.

Para cada usuário:

* É enviada uma requisição para a **OpenAI API**
* A IA gera uma mensagem curta e personalizada sobre a importância dos investimentos

#### ⚠️ Fallback automático

Caso a API da OpenAI atinja limite de uso ou esteja indisponível, o sistema gera automaticamente uma mensagem padrão.

Esse comportamento garante que o pipeline **nunca falhe**.

---

### 3️⃣ Load

O resultado final é salvo em um novo arquivo CSV (`data/users_with_messages.csv`), mantendo os dados originais intactos.

Exemplo de saída:

```csv
name,account,card,message
João,12345,9999,"João, investir hoje é o caminho para um futuro financeiro mais seguro."
Maria,67890,8888,"Maria, investir hoje é o caminho para um futuro financeiro mais seguro."
Carlos,54321,7777,"Carlos, investir hoje é o caminho para um futuro financeiro mais seguro."
```

---

## ▶️ Como Executar o Projeto

### Pré-requisitos

* Python **3.9+**
* Conta na OpenAI (opcional, caso queira usar IA real)

---

### 1️⃣ Criar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
```

---

### 2️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
OPENAI_API_KEY=sk-sua-chave-aqui
```

> 🔒 Nunca versionar esse arquivo

---

### 4️⃣ Executar o ETL

```bash
python -m app.main
```

---

## 🧪 Validação do Funcionamento

* Verifique se o arquivo `data/users_with_messages.csv` foi criado
* Confirme a presença da coluna `message`
* Verifique se os dados originais foram preservados

---

## 🚀 Diferenciais do Projeto

* ✔ Arquitetura limpa e modular
* ✔ Separação clara das etapas ETL
* ✔ Fallback automático para falha da IA
* ✔ Código simples, legível e extensível
* ✔ Pronto para evolução (API, banco de dados, Docker, etc.)

---

## 📈 Possíveis Evoluções Futuras

* Expor o pipeline via **FastAPI**
* Documentação com Swagger (caso vire API)
* Persistência em banco de dados
* Containerização com Docker

---

## 🏁 Conclusão

Este projeto foi desenvolvido como parte do **desafio prático do bootcamp Santander Dev Week 2023**, com o objetivo de aplicar conceitos de ETL, manipulação de dados com Python e integração com IA Generativa.

---

📌 **Autor:** Kleber
📌 **Tecnologias:** Python, Pandas, OpenAI API
📌 **Desafio:** Santander Dev Week 2023
