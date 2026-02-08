from typing import Callable

def apply_function(func: Callable[[int], int], value: int) -> int:
    return func(value)

result = apply_function(lambda x: x * 2, 5)
print(result)
# Fungsi: Menerima fungsi dan nilai, lalu menerapkan fungsi ke nilai yang diberikan.
# Kondisi: Ketika Anda ingin meneruskan fungsi sebagai argumen.