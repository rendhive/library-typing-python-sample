from typing import Type

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

def create_person(name: str, age: int) -> Type[Person]:
    return Person(name, age)

person = create_person("Eve", 28)
print(f"Nama: {person.name}, Usia: {person.age}")
# Fungsi: Mengembalikan instance dari kelas Person.
# Kondisi: Ketika Anda ingin menerangkan tipe hasil dari fungsi yang mengembalikan objek.