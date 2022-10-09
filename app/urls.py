from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
urlpatterns = [
    path('', api_root,),
    path('snippet/',  SnippetList.as_view(), name='snippet-list'),
    path('snippet/<int:pk>/', SnippetDetail.as_view(), name='snippet-detail'),
    # for users section
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('snippet/<int:pk>/highlight/',
         SnippetHighlight.as_view(), name='snippet-highlight')
]

urlpatterns = format_suffix_patterns(urlpatterns)
