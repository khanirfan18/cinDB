from rest_framework.views import APIView
from rest_framework import status,viewsets
from rest_framework.response import Response
from watchlist.models import WatchList,Review,StreamPlatform
from watchlist.api.serializers import WatchListSerializer,ReviewSerializer,PlatformSerializer

# Review View imports
from rest_framework import mixins
from rest_framework import generics


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
     
     
# User Review - Mixins 

# class ReviewList(mixins.ListModelMixin, 
#                   mixins.CreateModelMixin, 
#                   generics.GenericAPIView):
     
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
   
   
# class ReviewDetail(mixins.RetrieveModelMixin, 
#                    generics.GenericAPIView):
#      queryset = Review.objects.all()
#      serializer_class = ReviewSerializer
     
#      def get(self, request, *args, **kwargs):
#           return self.retrieve(request, *args, **kwargs)



# User Review CreateAPI view 

class ReviewList(generics.ListCreateAPIView):
     queryset = Review.objects.all()
     serializer_class = ReviewSerializer
     
     
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
     queryset = Review.objects.all()
     serializer_class = ReviewSerializer 
     