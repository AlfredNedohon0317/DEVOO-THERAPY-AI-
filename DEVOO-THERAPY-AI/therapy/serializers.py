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
        read_only_fields = ['user']

    def create(self, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            validated_data['user'] = request.user
        return super().create(validated_data)
