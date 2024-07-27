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
import openai
import os

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


# OpenAI ChatGPT response generation
@api_view(['POST'])
def generate_response(request):
    prompt = request.data.get('prompt')
    ai_name = "DEVOO"  # Example AI name

    if not prompt:
        logger.error("No prompt provided in request")
        return Response({"error": "No prompt provided"}, status=status.HTTP_400_BAD_REQUEST)

    openai.api_key = os.getenv("OPENAI_API_KEY")

    try:
        logger.debug("Sending request to OpenAI with prompt: %s", prompt)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        ai_response = response.choices[0].message['content'].strip()
        logger.debug("Received response from OpenAI: %s", ai_response)
        # Adding the AI name in the first person
        return Response({"response": f"{ai_response}"}, status=status.HTTP_200_OK)
    except openai.error.OpenAIError as e:
        logger.error("OpenAI API error: %s", str(e))
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.error("General error: %s", str(e))
        return Response({"error": "An unexpected error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Update account view
@api_view(['PUT'])
def update_account(request):
    user = request.user
    email = request.data.get('email')
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')

    if email:
        user.email = email
    if first_name:
        user.first_name = first_name
    if last_name:
        user.last_name = last_name

    user.save()

    return Response({"message": "Account updated successfully"}, status=status.HTTP_200_OK)

# Delete account view
@api_view(['DELETE'])
def delete_account(request):
    user = request.user
    user.delete()
    return Response({"message": "Account deleted successfully"}, status=status.HTTP_200_OK)
