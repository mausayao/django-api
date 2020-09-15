import requests

headers = {'Authorization': 'token 1255eb41461c004a0c543501bc12b2fd85f2d453'}


url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes'


novo_curso = {
    "titulo": "Gerencia agil de projetos com scrum",
    "url": "http://scrum.com.br"
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)

# Testando código http 201
assert resultado.status_code == 201

#  testando se o titulo do curso informado é o mesmo 
assert resultado.json()['titulo'] == novo_curso['titulo']
