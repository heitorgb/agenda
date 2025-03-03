from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True) #poder ficar em branco ou nulo
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(verbose_name='Data de Criação',auto_now=True) #vai inserir a hora atual 
    usuario = models.ForeignKey(User,on_delete=models.CASCADE) # se o usuário for excluido todos os eventos dele tbm serão

    class Meta:
        db_table = 'evento' # exigindo que a tabela se chama evento

    def __str__(self):
        return self.titulo    