from typing import List

def main_function() -> None:
    def nested_function(value: int) -> int:
        return value * 2

    print(nested_function(5))

main_function()
# Fungsi: Menunjukkan penggunaan type hints dalam fungsi bersarang.
# Kondisi: Ketika Anda ingin menggunakan fungsi dalam konteks yang lebih kecil.