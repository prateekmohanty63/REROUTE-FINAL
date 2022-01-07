from rest_framework  import serializers
from .models import Events


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Events
        # fields=['id','title','author','email']     # Here add only those fields which is required to serialize
        fields='__all__'                             # this gives all the fields that are in the model
        

