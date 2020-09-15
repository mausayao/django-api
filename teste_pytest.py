import requests

class TestCursos:
    headers = {
        'Authorization': 'Token 1255eb41461c004a0c543501bc12b2fd85f2d453'
    }

    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'


    def test_get_cursos(self):
        cursos = requests.get(url=self.url_base_cursos, headers=self.headers)
        assert cursos.status_code == 200

    def test_get_curso(self):
        curso = requests.get(url=f'{self.url_base_cursos}1', headers=self.headers)
        assert curso.status_code == 200

    def test_post_curso(self):
        novo_curso = {
            "titulo": "Gerencia agil de projetos com scrum",
            "url": "http://scrum.com.br"
        }

        resultado = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo_curso)
        assert resultado.status_code == 201
        assert resultado.json()['titulo'] == novo_curso['titulo']

    def test_put_curso(self):
        novo_curso = {
            "titulo": "Gerencia agil de projetos com scrum",
            "url": "http://scrum.com.br"
        }

        resultado = requests.put(url=f'{self.url_base_cursos}1', headers=self.headers, data=novo_curso)
        assert resultado.status_code == 200
        assert resultado.json()['titulo'] == novo_curso['titulo']

    def test_delete_curso(self):
        resultado = requests.delete(url=f'{self.url_base_cursos}1', headers=self.headers)
        assert resultado.status_code == 204
