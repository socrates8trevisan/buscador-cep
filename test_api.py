import pytest
from unittest.mock import patch, Mock
from api import buscar_cep

def test_buscar_cep_valido():
    mock_response = Mock()
    mock_response.json.return_value = {
        "cep": "01001-000",
        "logradouro": "Praça da Sé",
        "bairro": "Sé",
        "localidade": "São Paulo",
        "uf": "SP"
    }
    mock_response.raise_for_status = Mock()

    with patch("api.requests.get", return_value=mock_response):
        resultado = buscar_cep("01001000")
        assert resultado["localidade"] == "São Paulo"
        assert resultado["uf"] == "SP"

def test_buscar_cep_invalido():
    mock_response = Mock()
    mock_response.json.return_value = {"erro": True}
    mock_response.raise_for_status = Mock()

    with patch("api.requests.get", return_value=mock_response):
        with pytest.raises(ValueError):
            buscar_cep("00000000")