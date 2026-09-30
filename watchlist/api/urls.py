from django.urls import path
from watchlist.api.views import index

urlpatterns = [
    path('/',index,name='index'),
]