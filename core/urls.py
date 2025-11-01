from django.contrib import admin

from django.urls import path, include

from rest_framework import routers

from tarefas.views import TarefaViewSet


router = routers.DefaultRouter()

router.register(r'tarefas', TarefaViewSet, basename='tarefas')


urlpatterns = [

    path('admin/', admin.site.urls),

    path('auth/', include('djoser.urls')),

    path('auth/', include('djoser.urls.jwt')),

    path('', include(router.urls)),

]