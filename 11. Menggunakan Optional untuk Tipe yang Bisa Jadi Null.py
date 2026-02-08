from typing import Optional

def get_name(optional_name: Optional[str]) -> str:
    return optional_name if optional_name is not None else "Guest"

print(get_name("Alice"))
print(get_name(None))
# Fungsi: Mengembalikan nama atau "Guest" jika nama tidak disediakan.
# Kondisi: Ketika Anda ingin menangani argumen yang mungkin None.