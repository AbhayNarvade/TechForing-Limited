from django.urls import path , include
from .views import TaskDetail ,CommentList

urlpatterns = [
   path('<str:pk>/', TaskDetail.as_view(), name='task-detail'),
   path('<str:task_id>/comments/', CommentList.as_view(), name='Comment-List'),
]