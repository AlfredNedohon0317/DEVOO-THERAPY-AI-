from rest_framework import serializers
from .models import Therapist, Exercise, CommunityMessage

class TherapistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Therapist
        fields = ['id', 'name', 'specialty', 'website', 'phone_number', 'location']

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'title', 'description', 'video_url', 'website_url']

class CommunityMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityMessage
        fields = ['id', 'message', 'created_at', 'user']
