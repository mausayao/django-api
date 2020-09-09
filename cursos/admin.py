from django.contrib import admin
from cursos.models import Curso, Avaliacao


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'url', 'criacao', 'atualizacao', 'ativo', )


@admin.register(Avaliacao)
class AvalicaoAdmin(admin.ModelAdmin):
    list_display = ('curso', 'nome', 'email', 'criacao', 'atualizacao', 'ativo',)