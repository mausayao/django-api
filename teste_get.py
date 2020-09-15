import requests

headers = {'Authorization': 'token 1255eb41461c004a0c543501bc12b2fd85f2d453'}


url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes'


resultado = requests.get(url=url_base_cursos, headers=headers)
print(resultado.json())

# testando status code
assert resultado.status_code == 200

# testando a quantidade de registro
assert resultado.json()['count'] == 2

# testando o titutlo do primeiro curso esta correto
assert resultado.json()['results'][0]['titulo'] == 'titulo'