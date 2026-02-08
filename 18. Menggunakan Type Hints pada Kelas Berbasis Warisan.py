from typing import List

class Animal:
    def sound(self) -> str:
        return "Some sound"

class Cat(Animal):
    def sound(self) -> str:
        return "Meow"

def make_animal_sound(animal: Animal) -> None:
    print(animal.sound())

cat = Cat()
make_animal_sound(cat)
# Fungsi: Menangani polymorphism dengan type hints pada kelas warisan.
# Kondisi: Ketika Anda ingin menggunakan tipe umum untuk fungsi yang menerima beberapa subclass.