import requests

def buscar_cep(cep: str) -> dict:
    cep = cep.replace("-", "").strip()
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    data = response.json()
    if "erro" in data:
        raise ValueError(f"CEP '{cep}' não encontrado.")
    return data