from rest_framework.views import APIView
from rest_framework import status,viewsets
from rest_framework.response import Response
from watchlist.models import WatchList,Review,StreamPlatform
from watchlist.api.serializers import WatchListSerializer,ReviewSerializer,PlatformSerializer

# Watchlist 

class WatchListAV(APIView):
     def get(self, request):
          watchlist = WatchList.objects.all()
          serializer = WatchListSerializer(watchlist, many=True)
          return Response(serializer.data)

     def post(self,request):
          serializer = WatchListSerializer(data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          else:
               return Response(serializer.errors)


class WatchListDetailsAV(APIView):
     def get(self,request,pk):
          try:
               movies = WatchList.objects.get(pk=pk)
          except WatchList.DoesNotExist:
               return Response({"error":"Not Found!"},status=404)
          
          serialized = WatchListSerializer(movies)
          return Response(serialized.data)
     
     def put(self,request,pk):
          movies = WatchList.objects.get(pk=pk)
          serializer = WatchListSerializer(movies,data = request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=200)
          else:
               return Response(serializer.errors, status=400)
          
     def delete(self,request,pk):
          movies = WatchList.objects.get(pk=pk)
          movies.delete()
          return Response(status=204)
     
     
# Stream Platform 
     
class StreamPlatformAV(viewsets.ModelViewSet):
     serializer_class = PlatformSerializer
     queryset = StreamPlatform.objects.all()
     
     
# User Review