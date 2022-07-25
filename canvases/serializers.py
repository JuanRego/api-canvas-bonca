from rest_framework import serializers

from .models import Canvas

class CanvasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Canvas
        fields = "__all__"
        
    def create(self, validated_data: dict) -> Canvas:
        canvas, _ = Canvas.objects.get_or_create(**validated_data)
        
        return canvas
    

    