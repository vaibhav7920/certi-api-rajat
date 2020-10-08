from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import HttpResponse
from generator.addName import gen_certificate
from django.core.files.storage import FileSystemStorage

from .models import Participant
from .serializers import ParticipantSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def participant_list(request):
    if request.method == 'GET':
        participant = Participant.objects.all()

        email = request.query_params.get('email', None)
        if email is not None:
            participant = participant.filter(email)
        data = participant.values_list('name')
        participant_serializer = ParticipantSerializer(participant, many=True)
        return JsonResponse(participant_serializer.data, safe=False)


    elif request.method == 'POST':
        participant_data = JSONParser().parse(request)
        participant_serializer = ParticipantSerializer(data=participant_data)
        if participant_serializer.is_valid():
            participant_serializer.save()
            return JsonResponse(participant_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(participant_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def certificate(request, email):
    try:
        participant = Participant.objects.get(email=email)
    except Participant.DoesNotExist:
        return JsonResponse({'message': 'The participant does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        gen_certificate(participant.name)
        fs = FileSystemStorage()
        with fs.open('certificate.pdf') as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
        return response

