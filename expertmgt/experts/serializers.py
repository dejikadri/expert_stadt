from rest_framework import serializers
from .models import Expert


class ExpertSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expert
        # fields = ('first_name', 'last_name')
        fields = '__all__'
