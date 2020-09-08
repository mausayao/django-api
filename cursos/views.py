from django.db.migrations import serializer
from django.template.context_processors import request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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

    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Criou com sucesso"}, status=status.HTTP_201_CREATED)

        



class AvaliacaoAPIView(APIView):
    """
    API de Avaliação
    """
    
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)