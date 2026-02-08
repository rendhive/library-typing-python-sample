from typing import TypeVar, List

T = TypeVar('T')

def first_item(items: List[T]) -> T:
    return items[0]

print(first_item([1, 2, 3]))
print(first_item(["cat", "dog", "bird"]))
# Fungsi: Mengambil item pertama dari list generik.
# Kondisi: Ketika Anda ingin menjelaskan bahwa fungsi tersebut dapat bekerja dengan banyak tipe data.