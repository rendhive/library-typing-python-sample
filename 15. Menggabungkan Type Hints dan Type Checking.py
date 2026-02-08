from typing import List

def calculate_average(numbers: List[float]) -> float:
    return sum(numbers) / len(numbers)

avg = calculate_average([2.5, 3.5, 4.5])
print(f"Rata-rata: {avg}")
# Fungsi: Menghitung rata-rata dari angka dalam list.
# Kondisi: Ketika Anda ingin menganalisis data numerik.