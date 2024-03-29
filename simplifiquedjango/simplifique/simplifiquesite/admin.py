from django.contrib import admin
from .models import Comentario

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'comentario')
    actions = ['aprovar_comentarios']

    def aprovar_comentarios(self, request, queryset):
        queryset.update(aprovado=True)
    
    aprovar_comentarios.short_description = 'Aprovar os comentários'

admin.site.register(Comentario, ComentarioAdmin)


    


