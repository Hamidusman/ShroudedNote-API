from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'note', 'receipient', 'created_at']
        read_only_fields = ['id', 'created_at', 'receipient']

    def create(self, validated_data):
        return Note.objects.create(**validated_data)
