from django.urls import path
from restaurants.views import*

urlpatterns=[
    path('getPostRestaurant/',getPostRestaurant.as_view(),name='getPostRestaurant'),
    path('gByIDPuPatDel_Restaurant/<int:id>/',gByIDPuPatDel_Restaurant.as_view(),name='gByIDPuPatDel_Restaurant')
]