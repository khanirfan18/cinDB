from django.urls import path,include
from watchlist.api.views import WatchListAV,WatchListDetailsAV,StreamPlatformAV,ReviewList,ReviewDetail
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('platform',StreamPlatformAV,basename="stream-platform")


urlpatterns = [
    # show route
    path('show/',WatchListAV.as_view(),name='show'),
    path('show/<int:pk>',WatchListDetailsAV.as_view(),name='show-detail'),
    
    # platform route 
    path('',include(router.urls)), 
    
    # review route
    path('review/',ReviewList.as_view(), name='all-review'),
    path('review/<int:pk>',ReviewDetail.as_view(),name='review-detail'),
    
] 