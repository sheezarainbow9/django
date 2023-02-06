from rest_framework import serializers
from .models import Aluno


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = [
            'nome',
            'telefone',
            'email',
            'data_nasc',
            'description',
            'created_at',
            'updated_at',
            'user'
        ]
