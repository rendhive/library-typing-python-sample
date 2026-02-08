from typing import Any

def print_details(**kwargs: Any) -> None:
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Bob", age=25, city="New York")
# Fungsi: Menerima argumen kata kunci yang tidak ditentukan dan mencetaknya.
# Kondisi: Ketika Anda ingin menerima argumen kata kunci yang beragam tanpa batasan.