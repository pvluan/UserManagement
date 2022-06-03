from rest_framework import serializers
from .models import UserInfo

class AddUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserInfo
        fields = ["userName"]