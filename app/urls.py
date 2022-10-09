from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
urlpatterns = [
    path('snippet/',  SnippetList.as_view()),
    path('snippet/<int:pk>/', SnippetDetail.as_view()),
    # for users section
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)