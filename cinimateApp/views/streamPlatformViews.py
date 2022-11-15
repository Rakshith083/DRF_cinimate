from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from cinimateApp.models.streamPlatform import StreamPlatform
from cinimateApp.serializers.straemPlatformSerializer import StreamPlatformSerializer
from rest_framework import viewsets 

# Create your views here.
class StreeaPlatformListAV(APIView):
    def get(self,request):
        platforms=StreamPlatform.objects.all().filter(is_deleted=False)
        serializer=StreamPlatformSerializer(platforms,many=True,)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        if(isinstance(request.data,list)):
            serialiser=StreamPlatformSerializer(data=request.data,many=True)
        else:
            serialiser=StreamPlatformSerializer(data=request.data)
        if(serialiser.is_valid()):
            serialiser.save()
            return Response(serialiser.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serialiser.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class StreamPlatformAV(APIView):
    def get(self,request,id):
        try:
            platform=StreamPlatform.objects.filter(is_deleted=False).get(pk=id)
            serializer=StreamPlatformSerializer(platform)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except StreamPlatform.DoesNotExist:
            return Response({'Error':'Not found'},status=status.HTTP_404_NOT_FOUND)

    def put(self,request,id):
        try:
            platform=StreamPlatform.objects.filter(is_deleted=False).get(pk=id)
            serializer=StreamPlatformSerializer(platform,data=request.data)
            if(serializer.is_valid()):
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except StreamPlatform.DoesNotExist:
            return Response({'Error':'Not found'},status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,id):
        try:
            platform=StreamPlatform.objects.filter(is_deleted=False).get(pk=id)
            platform.delete()
            return Response({'message' : 'Content deleted successfully'},status=status.HTTP_204_NO_CONTENT)
        except StreamPlatform.DoesNotExist:
            return Response({'Error':'Not found'},status=status.HTTP_404_NOT_FOUND)

    def patch(self,request,id):
        try:
            platform=StreamPlatform.objects.get(pk=id)
            serializer=StreamPlatformSerializer(platform,data=request.data,partial=True)
            if(serializer.is_valid()):
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except StreamPlatform.DoesNotExist:
            return Response({'Error':'Not found'},status=status.HTTP_404_NOT_FOUND)

class StreamPlatformVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.filter(is_deleted=False,watchlist__is_deleted=False)
    serializer_class = StreamPlatformSerializer
    # def list(self, request):
    #     queryset = StreamPlatform.objects.all()
    #     serializer = StreamPlatformSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = StreamPlatform.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = StreamPlatformSerializer(user)
    #     return Response(serializer.data)
