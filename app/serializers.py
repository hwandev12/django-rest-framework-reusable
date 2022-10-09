from rest_framework import serializers
from .models import Snippet
from django.contrib.auth import get_user_model

User = get_user_model()

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
    
    class Meta:
        model = Snippet
        fields = ['url', 'id', 'title', 'code', 'linenos', 'language', 'style', 'owner', 'highlight']
        
class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']
