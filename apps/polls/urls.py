from django.urls import path
from .views import PollsDashboardView, PollCreateView, PollListView, PollDetailView, AlreadyVotedView

app_name = "polls"

urlpatterns = [
    path('home/', PollsDashboardView.as_view(), name = "home"),
    path('create/', PollCreateView.as_view(), name='poll_create'),
    path('list/', PollListView.as_view(), name='poll_list'),
    path('poll/<int:pk>/', PollDetailView.as_view(), name='poll_detail'),
    path('already_voted/', AlreadyVotedView.as_view(), name='already_voted'),
]