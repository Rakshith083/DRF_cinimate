from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from cinimateApp.models.watchlist import WatchList
from cinimateApp.serializers.WatchlistSerializer import WatchlistSerializer

# Create your views here.
class WatchlistAV(APIView):

    def get(self,request):
        watchlist=WatchList.objects.all()
        serializer=WatchlistSerializer(watchlist,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        if(isinstance(request.data,list)):
            serialiser=WatchlistSerializer(data=request.data,many=True)
        else:
            serialiser=WatchlistSerializer(data=request.data)
        if(serialiser.is_valid()):
            serialiser.save()
            return Response(serialiser.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serialiser.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class WatchlistDetailsAV(APIView):
    def get(self,request,id):
        try:
            watchlist=WatchList.objects.get(pk=id)
            serializer=WatchlistSerializer(watchlist)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except WatchList.DoesNotExist:
            return Response({'Error':'Not found'},status=status.HTTP_404_NOT_FOUND)

    def put(self,request,id):
        try:
            watchlist=WatchList.objects.get(pk=id)
            serializer=WatchlistSerializer(watchlist,data=request.data)
            if(serializer.is_valid()):
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except WatchList.DoesNotExist:
            return Response({'Error':'Not found'},status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,id):
        try:
            watchlist=WatchList.objects.get(pk=id)
            watchlist.delete()
            return Response({'message' : 'Content deleted successfully'},status=status.HTTP_204_NO_CONTENT)
        except WatchList.DoesNotExist:
            return Response({'Error':'Not found'},status=status.HTTP_404_NOT_FOUND)

    def patch(self,request,id):
        try:
            watchlist=WatchList.objects.get(pk=id)
            serializer=WatchlistSerializer(watchlist,data=request.data,partial=True)
            if(serializer.is_valid()):
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except WatchList.DoesNotExist:
            return Response({'Error':'Not found'},status=status.HTTP_404_NOT_FOUND)

