from django.urls import path
from . import views

urlpatterns = [
    path('', views.postList, name="post-list"),
    path('<str:pk>/', views.postDetail, name="post-detail"),
    path('<str:pk>/comment/', views.postComment, name="post-comment"),
]
