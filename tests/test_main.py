from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


# Testes de Sucesso
def test_read_root():
    """Testa se a rota raiz está funcionando"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Api de Alunos está funcionando!"}


def test_list_students_success():
    """Testa listagem de todos os alunos - Sucesso"""
    response = client.get("/students")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 1


def test_get_student_by_id_success():
    """Testa busca de aluno por ID - Sucesso"""
    response = client.get("/students/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "name" in data
    assert "email" in data


def test_create_student_success():
    """Testa criação de novo aluno - Sucesso"""
    new_student = {"name": "Maria Silva", "email": "maria.silva@example.com"}
    response = client.post("/students", json=new_student)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == new_student["name"]
    assert data["email"] == new_student["email"]
    assert "id" in data


# Testes de Falha Esperada
def test_get_student_not_found():
    """Testa busca de aluno inexistente - Falha Esperada"""
    response = client.get("/students/9999")
    assert response.status_code == 404
    assert "não encontrado" in response.json()["detail"].lower()
