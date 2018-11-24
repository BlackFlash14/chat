from django.urls import path
from .views import Rooms
urlpatterns = [
    path('/room/', Rooms.as_view())
]
