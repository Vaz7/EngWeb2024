import json
import requests

# Função para carregar dados de um arquivo JSON e enviar para a API
def carregar_dados_para_api(arquivo_json, url_api):
    with open(arquivo_json, 'r') as json_file:
        try:
            data = json.load(json_file)
        except json.JSONDecodeError as e:
            print(f"Erro ao carregar arquivo JSON: {e}")
            return
        
        pessoas = data.get("pessoas")
        if not pessoas:
            print("Nenhuma pessoa encontrada nos dados JSON.")
            return

        for pessoa in pessoas:
            pessoa_id = pessoa.get("_id")
            if pessoa_id:
                # Construir a URL com o ID da pessoa
                url = f"{url_api}"
                # Enviar os dados para a API
                response = requests.post(url, json=pessoa)
                if response.status_code == 200:
                    print(f"Dados da pessoa {pessoa_id} carregados com sucesso para a API")
                else:
                    print(f"Erro ao carregar dados da pessoa {pessoa_id} para a API:", response.status_code)
                    print(response.text)
            else:
                print("BI da pessoa não encontrado nos dados:", pessoa)

# Exemplo de utilização
if __name__ == "__main__":
    # Defina o caminho para o arquivo JSON e a URL base da API
    arquivo_json = "datasets/dataset-extra3.json"  # Substitua pelo caminho real do arquivo JSON
    url_api_base = "http://localhost:7777/pessoas"  # URL base da API

    # Chame a função para carregar os dados para a API
    carregar_dados_para_api(arquivo_json, url_api_base)
