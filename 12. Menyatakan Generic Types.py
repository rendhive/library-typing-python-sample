from typing import Generic, TypeVar

T = TypeVar('T')

class Box(Generic[T]):
    def __init__(self, content: T) -> None:
        self.content = content

    def get_content(self) -> T:
        return self.content

box = Box("Hello")
print(box.get_content())
# Fungsi: Menyatakan kelas generik yang dapat menerima berbagai tipe isi.
# Kondisi: Ketika Anda ingin mengembangkan kelas dengan fungsionalitas yang fleksibel.