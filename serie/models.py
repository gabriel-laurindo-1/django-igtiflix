from django.db import models

# Create your models here.
class Serie(models.Model):
    idGenero = models.ForeignKey("genero.Genero", on_delete=models.PROTECT, verbose_name='Gênero')
    nome = models.CharField(max_length=50, verbose_name='Nome')

    def __str__(self):
        return self.nome