from rest_framework.views import APIView
from rest_framework.response import Response


from cursos.models import Curso, Avaliacao
from cursos.serializers import CursoSerializer, AvaliacaoSerializer


class CursoAPIView(APIView):
    """
    API Curso View
    """

    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)

        return Response(serializer.data)


class AvaliacaoAPIView(APIView):
    """
    API de Avaliação
    """
    
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)