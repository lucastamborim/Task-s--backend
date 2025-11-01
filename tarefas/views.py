from rest_framework import viewsets, permissions, filters

from .models import Tarefa

from .serializers import TarefaSerializer

from django_filters.rest_framework import DjangoFilterBackend


class TarefaViewSet(viewsets.ModelViewSet):

    serializer_class = TarefaSerializer

    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]

    filterset_fields = ['tipo', 'status']

    ordering_fields = ['dataCriacao']

    ordering = ['-dataCriacao']


    def get_queryset(self):

        return Tarefa.objects.filter(usuario=self.request.user)


    def perform_create(self, serializer):

        serializer.save(usuario=self.request.user)