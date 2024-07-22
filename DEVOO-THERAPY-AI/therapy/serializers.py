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
    class Meta:
        model = CommunityMessage
        fields = '__all__'
