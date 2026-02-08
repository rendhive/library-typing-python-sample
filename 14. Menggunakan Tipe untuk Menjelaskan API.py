from typing import Dict, Any

def api_response() -> Dict[str, Any]:
    return {"status": "success", "data": {"id": 1, "name": "Alice"}}

response = api_response()
print(response)
# Fungsi: Mengembalikan struktur data yang mewakili respons dari API.
# Kondisi: Ketika Anda ingin mendokumentasikan hasil dari pemanggilan API dengan jelas.