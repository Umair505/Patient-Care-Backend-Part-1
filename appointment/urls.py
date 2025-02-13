from django.urls import include,path
from rest_framework import routers
from . import views

router = routers.DefaultRouter() # wifi toiri korlam

router.register('',views.AppointmentViewSet) #Antenna

urlpatterns = [
     path('',include(router.urls))
]
