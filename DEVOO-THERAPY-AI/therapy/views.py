from rest_framework import viewsets
from .models import Therapist, Exercise, CommunityMessage
from .serializers import TherapistSerializer, ExerciseSerializer, CommunityMessageSerializer

class TherapistViewSet(viewsets.ModelViewSet):
    queryset = Therapist.objects.all()
    serializer_class = TherapistSerializer

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class CommunityMessageViewSet(viewsets.ModelViewSet):
    queryset = CommunityMessage.objects.all()
    serializer_class = CommunityMessageSerializer
