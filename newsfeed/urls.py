from django.urls import path
from . import views
from .views import (
    NewsfeedListView,
    NewsfeedCreateView,
    NewsfeedDetailView,
    NewsfeedUpdateView,
    NewsfeedDeleteView,
    UserNewsfeedListView
)

urlpatterns = [
    path('', NewsfeedListView.as_view(), name='newsfeed-home'),
    path('user/<str:username>', UserNewsfeedListView.as_view(), name='user-posts'),

    path('about/', views.about, name='melodia-about'),
    path('post/<int:pk>/', NewsfeedDetailView.as_view(), name='newsfeed-detail'),
    path('post/new/', NewsfeedCreateView.as_view(), name='newsfeed-create'),
    path('post/<int:pk>/update/', NewsfeedUpdateView.as_view(), name='newsfeed-update'),
    path('post/<int:pk>/delete/', NewsfeedDeleteView.as_view(), name='newsfeed-delete'),
]