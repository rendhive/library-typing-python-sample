from typing import List

class Classroom:
    def __init__(self, students: List[str]) -> None:
        self.students = students

    def add_student(self, student: str) -> None:
        self.students.append(student)

classroom = Classroom(["Alice", "Bob"])
classroom.add_student("Charlie")
print(classroom.students)
# Fungsi: Mengelola daftar nama siswa dalam kelas.
# Kondisi: Ketika Anda ingin menjelaskan struktur kelas di Python.