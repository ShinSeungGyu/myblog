from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.PostListView.as_view(),  name='post_list'),
]
