import requests

headers = {'Authorization': 'token 1255eb41461c004a0c543501bc12b2fd85f2d453'}


url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes'


curso_atualizado = {
    "titulo": "Novo curso de scrum",
    "url": "http://teste-scrum.com.br"
}



curso = requests.get(url=f'{url_base_cursos}6/', headers=headers)

print(curso.json())


resultado = requests.put(url=f'{url_base_cursos}6/', headers=headers, data=curso_atualizado)

# testando o codigo http
assert resultado.status_code == 200


#  testando se o titulo do curso informado é o mesmo 
assert resultado.json()['titulo'] == curso_atualizado['titulo']