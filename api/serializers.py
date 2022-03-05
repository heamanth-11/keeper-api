from rest_framework import serializers
from .models import Notes, TrashNotes


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'


class TrashNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'

from django.contrib.auth.models import User


