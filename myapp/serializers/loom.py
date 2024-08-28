# serializers.py
from rest_framework import serializers
from ..models.loom import Loom

class LoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loom
        fields = '__all__'
