from django.db import router
from django.urls import path

from rest_framework.routers import SimpleRouter

from cursos.views import (
    CursoAPIView,
    CursosAPIView, 
    AvaliacaoAPIView, 
    AvaliacoesAPIView,
    CursoViewSet,
    AvaliacaoViewSet)


router = SimpleRouter()

# Api v2
router.register('cursos', CursoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)

# Api v1
urlpatterns = [
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('cursos/<int:pk>/', CursoAPIView.as_view(), name='curso'),
    path('cursos/<int:curso_pk>/avaliacoes/', AvaliacoesAPIView.as_view(), name='curso_avaliacoes'),
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='curso_avaliacao'),
    
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='avaliacao'),
]