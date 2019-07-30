from django.http import HttpResponse


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from django.http import Http404

from .models import Room, Player
from .serializers import RoomSerializer, PlayerSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the adv_room index.")
