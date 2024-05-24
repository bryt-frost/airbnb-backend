from django.http import JsonResponse
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

from chat.models import Conversation
from chat.serializers import (
    ConversationDetailSerializer,
    ConversationListSerializer,
    ConversationMessageSerializer,
)
from useraccount.models import User


@api_view(["GET"])
def conversations_list(request):

    serializer = ConversationListSerializer(request.user.conversations.all(), many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(["GET"])
def conversations_detail(request, pk):
    conversation = request.user.conversations.get(pk=pk)
    messages_serializer = ConversationMessageSerializer(
        conversation.messages.all(), many=True
    )
    serializer = ConversationDetailSerializer(conversation, many=False)
    return JsonResponse(
        {"conversation": serializer.data, "messages": messages_serializer.data},
        safe=False,
    )


@api_view(["GET"])
def conversations_start(request, user_id):
    conversations = Conversation.objects.filter(users__in=[user_id]).filter(
        users__in=[request.user.id]
    )
    if conversations.count() > 0:
        conversation = conversations.first()
        return JsonResponse({"success": True, "conversation_id": conversation.id})
    else:
        user = User.objects.get(pk=user_id)
        conversation = Conversation.objects.create()
        conversation.users.add(request.user)
        conversation.users.add(user)
        return JsonResponse({"success": True, "conversation_id": conversation.id})
