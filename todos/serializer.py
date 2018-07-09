from rest_framework import serializers

from .models import Todo

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        