from django.urls import path
from api import views
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    path('users', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('posts', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),   
]

urlpatterns= format_suffix_patterns(urlpatterns)