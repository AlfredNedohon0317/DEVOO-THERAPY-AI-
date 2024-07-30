from rest_framework import serializers
from .models import Therapist, Exercise, CommunityMessage

class TherapistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Therapist
        fields = '__all__'

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class CommunityMessageSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = CommunityMessage
        fields = ['id', 'message', 'created_at', 'user']
        read_only_fields = ['id', 'created_at', 'user']
