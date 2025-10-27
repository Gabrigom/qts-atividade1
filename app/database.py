from app.models import Student

# Simulação de banco de dados em memória
students_db = [
    Student(id=1, name="Vinicius Gabriel Miranda Gomes", email="vinny.gab18@gmail.com")
]


def get_all_students():
    return students_db


def get_student_by_id(student_id: int):
    for student in students_db:
        if student.id == student_id:
            return student
    return None


def create_student(name: str, email: str):
    new_id = max([s.id for s in students_db], default=0) + 1
    new_student = Student(id=new_id, name=name, email=email)
    students_db.append(new_student)
    return new_student