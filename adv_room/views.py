from django.http import HttpResponse
from django.template import loader


from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from django.http import Http404
from django.views import View

from .models import Room, Player
from .serializers import RoomSerializer, PlayerSerializer


def index(request):
    player_detail = Player.objects
    template = loader.get_template('adv_room/index.html')
    context = {
        'player_detail': player_detail,
    }
    return HttpResponse(player_detail)

    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

class room_view(generics.ListCreateAPIView):
    queryset = Room.objects.all().order_by('id')
    serializer_class = RoomSerializer

    # def get_msg_room(self, request):
    #     return HttpResponse('result')
    
    # def get(self,request):
    #     pass

class player_view(View):
    def get_msg_player(self, request):
        return HttpResponse('player result')

