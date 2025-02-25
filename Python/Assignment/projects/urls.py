from django.urls import path , include
from .views import ProjectList ,ProjectDetail ,ProjectMemberList ,ProjectMemberDetail , TaskList


urlpatterns = [
  path('', ProjectList.as_view() , name='project-list'), 
  path('<str:pk>/', ProjectDetail.as_view() , name='project-detail'), 
  path('group/members/', ProjectMemberList.as_view() , name='project-members'), 
  path('group/members/<str:pk>/', ProjectMemberDetail.as_view() , name='project-member-detail'), 
  path('<str:project_id>/tasks/', TaskList.as_view() , name='Task-List'), 
 
]
