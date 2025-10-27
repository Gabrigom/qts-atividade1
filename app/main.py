from fastapi import FastAPI, HTTPException, status
from app.models import Student, StudentCreate
from app.database import get_all_students, get_student_by_id, create_student

app = FastAPI(title="API de alunos", version="1.0.0")


@app.get("/")
def read_root():
    return {"message": "Api de Alunos está funcionando!"}


@app.get("/students", response_model=list[Student])
def list_students():
    """Retorna todos os alunos cadastrados"""
    return get_all_students()


@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    """Busca um aluno específico por ID"""
    student = get_student_by_id(student_id)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Aluno com id {student_id} não encontrado.",
        )
    return student


@app.post("/students", response_model=Student, status_code=status.HTTP_201_CREATED)
def add_student(student: StudentCreate):
    """Cria um novo aluno"""
    return create_student(name=student.name, email=student.email)
