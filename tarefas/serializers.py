from rest_framework import serializers

from .models import Tarefa


class TarefaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Tarefa

        fields = ['id', 'usuario', 'titulo', 'descricao', 'tipo', 'dataCriacao', 'status']

        read_only_fields = ['id', 'dataCriacao', 'usuario']


    def validate(self, data):

        for field in ['titulo', 'descricao', 'tipo']:

            valor = data.get(field) or ''

            if not valor.strip():

                raise serializers.ValidationError({field: f'{field} não pode estar vazio.'})

        return data