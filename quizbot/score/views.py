from rest_framework import serializers
from quizbot.score.models import Score
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ScoreSerializers
from .models import Score
from rest_framework import status
from django.db.models import F

class UpdateScores(APIView):
    
    def post(self,request,formate=None,**kwargs):
        serializer = ScoreSerializers(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            points = serializer.validated_data['points']


            if Score.objects.filter(name=name).exists():
                serializer = Score.objects.get(name=name)
                serializer.points = F('points') + points
                
            serializer.save()

            return Response(None,status=status.HTTP_201_CREATED)

        return  Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class LeaderBoard(APIView):

    def get(self,request,formate=None,**kwargs):
        scores = Score.objects.all().order_by('-points')[:10]
        serializer = ScoreSerializers(scores,many=True)
        return Response(serializer.data)