from django.contrib import admin

from chat.models import Conversation, ConversationMessage

admin.site.register([Conversation, ConversationMessage])
