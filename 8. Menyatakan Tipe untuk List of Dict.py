from typing import List, Dict

def get_users() -> List[Dict[str, Union[str, int]]]:
    return [
        {"name": "Charlie", "age": 32},
        {"name": "Diana", "age": 27}
    ]

users = get_users()
print(users)
# Fungsi: Mengembalikan list dari dictionary yang mewakili pengguna.
# Kondisi: Ketika Anda perlu menerangkan struktur data yang lebih kompleks.