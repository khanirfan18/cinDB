from django.urls import path,include
from watchlist.api.views import WatchListAV,WatchListDetailsAV,StreamPlatformAV
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('platform',StreamPlatformAV,basename="stream-platform")


urlpatterns = [
    path('show/',WatchListAV.as_view(),name='show'),
    path('show/<int:pk>',WatchListDetailsAV.as_view(),name='show-detail'),
    path('',include(router.urls)), 
    
] 