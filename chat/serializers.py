from rest_framework import serializers

from chat.models import Conversation, ConversationMessage
from useraccount.serializers import UserDetailsSerializer


class ConversationListSerializer(serializers.ModelSerializer):
    users = UserDetailsSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ["id", "users", "modified_at"]


class ConversationDetailSerializer(serializers.ModelSerializer):
    users = UserDetailsSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields=["id", "users", "modified_at"]

class ConversationMessageSerializer(serializers.ModelSerializer):
    sent_to = UserDetailsSerializer(read_only=True)
    created_by = UserDetailsSerializer(read_only=True)

    class Meta:
        model = ConversationMessage
        fields = ["id", "body", "sent_to", "created_by", "created_at"]
