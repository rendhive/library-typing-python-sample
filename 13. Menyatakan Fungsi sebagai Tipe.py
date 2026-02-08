from typing import Callable

def greeting_function() -> None:
    print("Hello, World!")

def run_function(func: Callable[[], None]) -> None:
    func()

run_function(greeting_function)
# Fungsi: Menerima fungsi tanpa argumen dan menjalankannya.
# Kondisi: Ketika Anda ingin meneruskan fungsi sebagai argumen.