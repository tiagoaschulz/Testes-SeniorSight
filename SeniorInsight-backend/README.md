# SeniorInsight Backend API

Este é o backend para a aplicação SeniorInsight, desenvolvido com FastAPI e estruturado seguindo os princípios do Domain-Driven Design (DDD).

## Arquitetura do Projeto

A arquitetura é dividida em quatro camadas principais, cada uma com uma responsabilidade clara:

### 1. `app/domain` (Camada de Domínio)
- **Responsabilidade:** O coração da aplicação. Contém a lógica de negócio principal, as regras e as entidades. É a camada mais isolada e não depende de nenhuma outra.
- **Componentes:**
    - `models.py`: Define as entidades de domínio (ex: `Medication`, `Vital`) usando Pydantic. Representam os dados e suas validações intrínsecas.
    - `repository.py`: Define as interfaces (contratos) para os repositórios. Diz *o que* a aplicação precisa fazer em termos de persistência, mas não *como*.

### 2. `app/application` (Camada de Aplicação)
- **Responsabilidade:** Orquestrar os casos de uso da aplicação. Atua como um intermediário entre a camada de API e a camada de Domínio. Não contém lógica de negócio complexa, apenas coordena o fluxo.
- **Componentes:**
    - `services.py`: Contém os serviços da aplicação que executam os casos de uso (ex: `MedicationService`). Eles utilizam as entidades de domínio e os repositórios para realizar suas tarefas.

### 3. `app/infrastructure` (Camada de Infraestrutura)
- **Responsabilidade:** Implementar os detalhes técnicos, como acesso a banco de dados, comunicação com serviços externos, etc. Esta camada depende das interfaces definidas na camada de Domínio.
- **Componentes:**
    - `database.py`: Configuração da conexão com o banco de dados. Nesta versão inicial, simula um banco de dados em memória com os dados dos mocks.
    - `repositories.py`: Implementação concreta dos repositórios definidos em `domain/repository.py`. É aqui que os dados são efetivamente buscados ou salvos.

### 4. `app/api` (Camada de API)
- **Responsabilidade:** Expor a funcionalidade da aplicação para o mundo exterior através de uma API REST. Lida com as requisições HTTP, validação de dados de entrada e serialização dos dados de saída.
- **Componentes:**
    - `endpoints/`: Cada arquivo define os endpoints para um recurso específico (ex: `medications.py`). Eles recebem as requisições, chamam os serviços da camada de aplicação e retornam as respostas.

## Como Executar o Projeto

1.  **Crie um Ambiente Virtual:**
    ```bash
    python -m venv .venv
    ```

2.  **Ative o Ambiente Virtual:**
    - **Windows:**
      ```bash
      .venv\Scripts\activate
      ```
    - **macOS/Linux:**
      ```bash
      source .venv/bin/activate
      ```

3.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o Servidor:**
    A partir do diretório raiz (`SeniorInsight-backend`), execute o seguinte comando:
    ```bash
    uvicorn app.main:app --reload
    ```
    - `--reload`: Faz com que o servidor reinicie automaticamente após alterações no código.

5.  **Acesse a Documentação Interativa:**
    Com o servidor rodando, acesse uma das seguintes URLs no seu navegador:
    - **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
    - **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Endpoints da API

Todos os endpoints estão sob o prefixo `/v1`.

### Medications

- **`GET /v1/medications`**
  - **Descrição:** Retorna uma lista de todos os medicamentos cadastrados.

- **`POST /v1/medications`**
  - **Descrição:** Cria um novo medicamento.

- **`PATCH /v1/medications/{id}`**
  - **Descrição:** Atualiza um medicamento existente.

### History

- **`GET /v1/history`**
  - **Descrição:** Retorna uma lista de todos os eventos do histórico.

- **`POST /v1/history`**
  - **Descrição:** Cria um novo evento no histórico.

- **`PATCH /v1/history/{id}`**
  - **Descrição:** Atualiza um evento do histórico.

### Vitals

- **`GET /v1/vitals`**
  - **Descrição:** Retorna uma lista de todos os sinais vitais monitorados.

- **`POST /v1/vitals`**
  - **Descrição:** Cria um novo registro de sinal vital.
  
- **`PATCH /v1/vitals/{id}`**
  - **Descrição:** Atualiza um registro de sinal vital.


## Banco de Dados

A aplicação utiliza PostgreSQL como banco de dados, com a interação sendo gerenciada pelo SQLAlchemy.

### Tabelas

As seguintes tabelas são definidas no `orm_models.py`:

- **`medications`**: Armazena informações sobre os medicamentos.
  - `id`: Identificador único.
  - `name`: Nome do medicamento.
  - `dosage`: Dosagem.
  - `frequency`: Frequência de administração.
  - `last_dose_time`: Data e hora da última dose.
  - `status`: Status do medicamento (ex: "ok").

- **`history_events`**: Registra eventos históricos.
  - `id`: Identificador único.
  - `event_type`: Tipo de evento (ex: "medication").
  - `title`: Título do evento.
  - `event_time`: Data e hora do evento.
  - `description`: Descrição do evento.

- **`vitals`**: Guarda os sinais vitais do paciente.
  - `id`: Identificador único.
  - `title`: Nome do sinal vital (ex: "Heart Rate").
  - `value`: Valor medido.
  - `unit`: Unidade de medida (ex: "BPM").
  - `status`: Status do sinal vital (ex: "stable").
  - `recorded_at`: Data e hora da medição.

## Postman Collections

Para facilitar os testes da API, foram criadas collections do Postman que podem ser importadas. Os arquivos `.json` estão localizados na pasta `postman_collection`.

- `history.postman_collection.json`: Endpoints relacionados ao histórico.
- `medications.postman_collection.json`: Endpoints para gerenciamento de medicamentos.
- `vitals.postman_collection.json`: Endpoints para consulta de sinais vitais.
