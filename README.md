# 🎓 API de Alunos - FastAPI

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3.11+-blue.svg?style=for-the-badge&logo=python)
![Pytest](https://img.shields.io/badge/pytest-passing-green?style=for-the-badge&logo=pytest)
![CI](https://img.shields.io/badge/CI-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions)

> API REST simples para gerenciamento de alunos com FastAPI, testes automatizados e integração contínua.

---

## 🚀 Funcionalidades

- ✅ Listagem de todos os alunos
- ✅ Busca de aluno por ID
- ✅ Cadastro de novos alunos
- ✅ Validação automática de e-mails
- ✅ Banco de dados em memória
- ✅ Testes automatizados (Pytest)
- ✅ CI/CD com GitHub Actions

---

## 📋 Tecnologias

- **FastAPI** - Framework web moderno e rápido
- **Pydantic** - Validação de dados
- **Pytest** - Testes automatizados
- **Black** - Formatação de código
- **Flake8** - Análise de código (linting)
- **GitHub Actions** - Integração contínua

---

## 🏗️ Estrutura do Projeto

```
fastapi-students-api/
├── app/
│   ├── __init__.py
│   ├── main.py          # Rotas da API
│   ├── models.py        # Modelos de dados
│   └── database.py      # Banco de dados em memória
├── tests/
│   ├── __init__.py
│   └── test_main.py     # Testes automatizados
├── .github/
│   └── workflows/
│       └── ci.yml       # Pipeline de CI/CD
├── requirements.txt
└── README.md
```

---

## 🔧 Instalação e Execução

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/seu-usuario/fastapi-students-api.git
cd fastapi-students-api
```

### 2️⃣ Crie e ative o ambiente virtual

```bash
# Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Execute a aplicação

```bash
uvicorn app.main:app --reload
```

### 5️⃣ Acesse a documentação interativa

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## 🧪 Executar os Testes

```bash
# Executar todos os testes
pytest tests/ -v

# Executar com cobertura
pytest tests/ --cov=app
```

## 🔄 CI/CD Pipeline

O pipeline do GitHub Actions executa automaticamente:

1. **Black** - Verifica formatação do código
2. **Flake8** - Análise estática e linting
3. **Pytest** - Executa todos os testes

O pipeline é acionado em:

- Push para `main`/`master`
- Pull requests

---

## 🛠️ Comandos Extras

```bash
# Formatar código
black app/ tests/

# Verificar linting
flake8 app/ tests/ --max-line-length=88
```

---
