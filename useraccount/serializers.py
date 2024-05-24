from attr import fields
from rest_framework import serializers

from useraccount.models import User


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "name", "avatar_url"]
