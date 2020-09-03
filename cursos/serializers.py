from rest_framework import serializers

from cursos.models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    extra_kwargs = {
        'email': {'write_only': True}
    }

    model = Avaliacao

    fields = (
        'id',
        'curso',
        'nome',
        'email',
        'comentario',
        'avaliacao',
        'criacao',
        'ativo'
    )


class CursoSerializer(serializers.ModelSerializer):
    model = Curso
    fields = (
        'id',
        'titulo',
        'url',
        'criacao',
        'ativo'
    )