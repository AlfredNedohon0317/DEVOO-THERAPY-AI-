from rest_framework import viewsets
from .models import Therapist, Exercise, CommunityMessage
from .serializers import TherapistSerializer, ExerciseSerializer, CommunityMessageSerializer
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import logging

logger = logging.getLogger(__name__)

# ViewSets
class TherapistViewSet(viewsets.ModelViewSet):
    queryset = Therapist.objects.all()
    serializer_class = TherapistSerializer

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class CommunityMessageViewSet(viewsets.ModelViewSet):
    queryset = CommunityMessage.objects.all()
    serializer_class = CommunityMessageSerializer

# Signup view
@api_view(['POST'])
def signup(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    first_name = request.data.get('firstName')
    last_name = request.data.get('lastName')

    logger.debug("Received signup data: %s", request.data)

    if not username or not password or not email or not first_name or not last_name:
        logger.error("Missing fields: username=%s, password=%s, email=%s, firstName=%s, lastName=%s",
                     username, password, email, first_name, last_name)
        return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        validate_password(password)
    except ValidationError as e:
        logger.error("Password validation error: %s", e.messages)
        return Response({"error": e.messages}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        logger.info("User created successfully: %s", user)
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        logger.error("Error creating user: %s", str(e))
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
