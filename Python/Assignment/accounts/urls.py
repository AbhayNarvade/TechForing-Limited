from django.urls import path , include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'Listofusers', UsersViewSetList, basename='user')

urlpatterns = [
   path('', include(router.urls)),
   path('<uuid:pk>/',userdata.as_view() ,name="user-detail"),
   path('register/' , register , name='register'),
   path('login/' , login , name='login'),
]
