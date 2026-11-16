from rest_framework import serializers
from dailydo.models import ToDo

class ToDoSerializer(serializers.ModelSerializer):

    class Meta:

        model=ToDo

        fields="__all__"

        read_only_fields=["id","owner","created_at"]
