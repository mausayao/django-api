import requests

#Get avaliações

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# acessando o status code
print(avaliacoes.status_code)

# acessando dados da resposta
print(avaliacoes.json())