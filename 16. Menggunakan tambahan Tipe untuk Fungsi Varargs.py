from typing import List

def concatenate_strings(*args: str) -> str:
    return " ".join(args)

result = concatenate_strings("Hello", "world!", "This", "is", "Python.")
print(result)
# Fungsi: Menggabungkan beberapa string menjadi satu.
# Kondisi: Ketika Anda ingin menggabungkan input teks menjadi kalimat.