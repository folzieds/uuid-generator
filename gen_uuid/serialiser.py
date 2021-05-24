from rest_framework import serializers
from .models import UUID

class UUIDSerializer(serializers.ModelSerializer):

    class Meta:
        model = UUID
        fields = '__all__'