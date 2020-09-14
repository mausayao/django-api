from rest_framework import serializers

from cursos.models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
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
            'ativo',
        )
    
    def validate_avaliacao(self, valor):
        if valor in range(1, 6):
            return valor
        raise serializers.ValidationError('A avaliação precisa ser um número inteiro entre 1 e 5')


class CursoSerializer(serializers.ModelSerializer):
    # nested relationship
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # Hyperlinked related field
    # avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')

    # Primary key related field
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes'
        )