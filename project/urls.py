from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from main.views import AlunoViewSet


router = routers.DefaultRouter()
router.register(r'aluno', AlunoViewSet)


urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('alunoapi/', include(router.urls)),
    path('aluno-auth/', include('rest_framework.urls')),

]
