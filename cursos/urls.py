from unicodedata import name
from django.urls import path
from cursos.views import CursoAPIView, AvaliacaoAPIView


urlpatterns = [
    path('cursos/', CursoAPIView.as_view(), name='cursos'),
    path('avaliacoes', AvaliacaoAPIView.as_view(), name='avaliacoes')
]