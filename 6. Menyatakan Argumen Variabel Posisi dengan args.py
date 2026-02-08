from typing import Any

def print_all(*args: Any) -> None:
    for arg in args:
        print(arg)

print_all(1, "Hello", 3.14, [1, 2, 3])
# Fungsi: Menerima argumen posisi variabel dan mencetak semuanya.
# Kondisi: Ketika Anda ingin-menangani jumlah argumen yang tidak ditentukan.