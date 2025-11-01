from django.db import models

from django.contrib.auth.models import User


class Tarefa(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tarefas')

    titulo = models.CharField(max_length=255)

    descricao = models.TextField()

    tipo = models.CharField(max_length=50)

    dataCriacao = models.DateTimeField(auto_now_add=True)

    status = models.BooleanField(default=False)  # False = pendente, True = concluído


    def __str__(self):

        return f"{self.titulo} - {'Concluído' if self.status else 'Pendente'}"