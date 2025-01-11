from django.urls import path , include
from .views import CommentDetail

urlpatterns = [
    path('<str:pk>/', CommentDetail.as_view() , name='Comment-Detail'),
]
