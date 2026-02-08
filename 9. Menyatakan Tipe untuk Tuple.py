from typing import Tuple

def get_coordinates() -> Tuple[float, float]:
    return (1.5, 2.5)

x, y = get_coordinates()
print(f"Koordinat: ({x}, {y})")
# Fungsi: Mengembalikan tuple yang mewakili koordinat.
# Kondisi: Ketika Anda ingin mengembalikan beberapa nilai dengan tipe data tertentu.