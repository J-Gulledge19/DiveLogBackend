from .models import Dives
from rest_framework import serializers

# Our Divelog Serializer
class DivesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Dives
        # the fields that should be included in the serialized output
        fields = ['id', 'location', 'date', 'image', 'description']