from rest_framework import serializers
from pocket.manager.models import Activity


class ActivitySerializer(serializers.ModelSerializer):

    class Meta():
        model = Activity
        fields = ['name', 'amount', 'date', 'type']


