from django.db import models

# Create your models here.

class Comentario(models.Model):
    nome = models.CharField('nome', max_length=20)
    comentario = models.TextField('comentario')
    aprovado = models.BooleanField('aprovado', default=False)

    def __str__(self):
        return f"{self.nome} - {self.publicado}"


