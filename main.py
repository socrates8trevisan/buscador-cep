from api import buscar_cep

def main():
    print("=== Buscador de CEP ===")
    cep = input("Digite o CEP: ")
    try:
        endereco = buscar_cep(cep)
        print("\n📍 Endereço encontrado:")
        print(f"  Logradouro : {endereco.get('logradouro', '-')}")
        print(f"  Bairro     : {endereco.get('bairro', '-')}")
        print(f"  Cidade     : {endereco.get('localidade', '-')}")
        print(f"  Estado     : {endereco.get('uf', '-')}")
    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro de conexão: {e}")

if __name__ == "__main__":
    main()