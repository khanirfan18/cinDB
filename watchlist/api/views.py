from rest_framework.decorators import api_view
from rest_framework.response import Response
from watchlist.models import WatchList,Review,StreamPlatform
from watchlist.api.serializers import WatchListSerializer,ReviewSerializer,PlatformSerializer





@api_view(['GET','POST'])
def index(request):
     if request.method == 'GET':
          watchlist = WatchList.objects.all()
          serializer = WatchListSerializer(watchlist,many=True)
          return Response(serializer.data)
     
     
     if request.method == 'POST':
          serializer = WatchListSerializer(data=request.data)
          if serializer.is_valid():     
               serializer.save()
               return Response(serializer.data, status=201)
          
          return Response(serializer.errors, status=400)