import requests

headers = {'Authorization': 'token 1255eb41461c004a0c543501bc12b2fd85f2d453'}


url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes'

resultado = requests.delete(url=f'{url_base_cursos}6', headers=headers)


# testando o codigo http
assert resultado.status_code == 204


# Tamanho do conteudo retornado
assert len(resultado.text) == 0