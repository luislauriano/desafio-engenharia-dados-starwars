# 🛠️ Pipeline de Dados Star Wars

Um pipeline **ETL em Python** que consome dados da **Star Wars API (SWAPI)** e os armazena em um banco de dados **PostgreSQL** para análise e exploração de dados.

Este projeto simula um fluxo simplificado de **Engenharia de Dados**, incluindo ingestão de dados via API, tratamento de paginação, limpeza de dados inconsistentes, armazenamento relacional e análise utilizando **SQL e Jupyter Notebook**.

---

# 🚀 Funcionalidades

- Extração de dados de múltiplos endpoints da SWAPI
- Tratamento automático de **paginação da API**
- Limpeza de valores inconsistentes como `"unknown"` e `"n/a"`
- Armazenamento estruturado em tabelas **PostgreSQL**
- Carga **idempotente** usando `ON CONFLICT` para evitar duplicações
- Separação do pipeline em camadas de **Extração e Carga**
- Análise de dados utilizando **SQL e Jupyter Notebook**
- Uso de **variáveis de ambiente** para configuração segura do banco

---

# 🧱 Estrutura do Projeto
```
desafio-engenharia-dados-starwars/
│
├── run_pipeline.py
├── requirements.txt
├── docker-compose.yml
├── .gitignore
├── README.md
│
├── data_pipeline/
│ ├── db_connection.py
│ ├── extract.py
│ ├── transform.py
│ └── load.py
│
├── database/
│ └── schema.sql
│
└── notebooks/
└── analise_exploratoria.ipynb
```
A estrutura do projeto foi organizada de forma modular para refletir um fluxo simples de engenharia de dados, separando claramente as responsabilidades de cada etapa do pipeline. A pasta data_pipeline contém os módulos responsáveis pela lógica de extração dos dados da API, conexão com o banco de dados e carga das informações no PostgreSQL. O arquivo run_pipeline.py atua como ponto de entrada do pipeline, orquestrando as etapas de extração e carga para os diferentes recursos da API. Scripts SQL utilizados para criação das tabelas ficam na pasta database, enquanto a pasta notebooks contém o notebook utilizado para realizar a análise exploratória e responder às perguntas propostas no desafio. Essa organização facilita a manutenção do código, a reutilização de componentes e reflete uma estrutura comum em projetos de pipelines de dados.

---

# 🔧 Tecnologias Utilizadas

- Python 3
- Requests
- PostgreSQL
- Psycopg2
- Pandas
- Jupyter Notebook
- python-dotenv

---

# 🧠 Fonte de Dados

Este projeto utiliza a API pública:

**Star Wars API (SWAPI)**  
https://swapi.dev/

Endpoints utilizados:

- `/people`
- `/planets`
- `/starships`
- `/films`

---

# ⚙️ Instruções de Instalação

## 1️⃣ Clonar o repositório

```
git clone <url-do-repositorio>
cd desafio-engenharia-dados-starwars
```

## 2️⃣ Criar ambiente virtual

```
python -m venv .venv
source .venv/bin/activate 
```
No Windows:

```
.venv\Scripts\activate
```
## 3️⃣ Instalar dependências

```
pip install -r requirements.txt
```
## 4️⃣ Configurar variáveis de ambiente
Crie um arquivo .env na raiz do projeto e adicione:
```
DB_HOST=localhost
DB_NAME=swapi
DB_USER=swapi
DB_PASSWORD=swapi
DB_PORT=5432
```
O arquivo .env não é versionado por segurança.

## 5️⃣ Banco de dados
O projeto utiliza um container PostgreSQL para garantir um ambiente isolado e reprodutível.

* Criação Automática: Ao executar ```docker-compose up -d```, o banco de dados swapi é inicializado automaticamente.
* Schema: As tabelas são criadas na primeira execução da pipeline ou podem ser inicializadas manualmente via:
```docker exec -i swapi_postgres psql -U swapi -d swapi < database/schema.sql```

---

# ▶️ Executar o Pipeline ETL
Para rodar o pipeline de ingestão de dados:
``` python run_pipeline.py ```
O pipeline irá:

* Extrair dados da API SWAPI
* Tratar paginação automaticamente
* Limpar valores inconsistentes
* Carregar os dados no PostgreSQL

---

# 📊 Análise de Dados
Abra a pasta de notebooks e acesse:
``` notebooks/swapi_analysis.ipynb ```
O notebook realiza análise exploratória e responde perguntas como:

Qual é o personagem que apareceu em mais filmes de Star Wars?
Quais são os planetas mais quentes do universo de Star Wars?
Quais são as naves espaciais mais rápida do universo de Star Wars?
Qual é a arma mais poderosa do universo de Star Wars?

---

# 🧪 Exemplo de Consulta SQL
Exemplo de consulta utilizada nas análises:
```
query_filmes = """
SELECT 
    episode_id AS episodio, 
    title AS titulo, 
    release_date AS lancamento
FROM films
ORDER BY episode_id;
"""

pd.read_sql(query_filmes, conn)
```
---

# 🎯 Aprendizados do Projeto

Este projeto demonstra conceitos importantes de Engenharia de Dados:

* Ingestão de dados via API
* Tratamento de paginação
* Estruturação de pipelines ETL
* Limpeza e padronização de dados
* Modelagem e carga de dados no PostgreSQL, garantindo integridade referencial e consultas performáticas via SQL
* Análise de dados com SQL
* Fluxos reprodutíveis de análise

---

# 📌 Observações

* Segurança: O arquivo .env está configurado no .gitignore para proteger as credenciais do banco de dados.
* Integridade: A carga de dados utiliza a cláusula SQL ON CONFLICT, garantindo que o pipeline possa ser executado múltiplas vezes sem duplicar registros no banco (idempotência).
* Consistência: Todas as transformações de tipos (strings para números) são aplicadas antes da carga final.

---