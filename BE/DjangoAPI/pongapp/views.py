from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Player, Tournament
from .serializers import PlayerSerializer, TournamentSerializer

# Create your views here.
@api_view(['GET'])
def getPlayers(request):
    players = Player.objects.all()
    serializer = PlayerSerializer(players, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPlayer(request, pk):
    players = Player.objects.get(id=pk)
    serializer = PlayerSerializer(players, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getTournaments(request):
    tournaments = Tournament.objects.all()
    serializer = TournamentSerializer(tournaments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTournament(request, pk):
    tournaments = Tournament.objects.get(id=pk)
    serializer = TournamentSerializer(tournaments, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addPlayer(request):
    serializer = PlayerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)    

@api_view(['POST'])
def addTournament(request):
    serializer = TournamentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updatePlayer(request, pk):
    player = Player.objects.get(id=pk)
    serializer = PlayerSerializer(instance=player, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateTournament(request, pk):
    tournament = Tournament.objects.get(id=pk)
    serializer = TournamentSerializer(instance=tournament, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deletePlayer(request, pk):
    player = Player.objects.get(id=pk)
    player.delete()
    return Response('Player deleted')

@api_view(['DELETE'])
def deleteTournament(request, pk):
    tournament = Tournament.objects.get(id=pk)
    tournament.delete()
    return Response('Tournament deleted')