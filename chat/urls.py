from django.urls import path

from chat.api import conversations_detail, conversations_list, conversations_start

urlpatterns = [
    path("", conversations_list, name="conversations_list"),
    path("start/<uuid:user_id>", conversations_start, name="conversations_start"),
    path(
        "<uuid:pk>",
        conversations_detail,
        name="conversations_detail",
    ),
]
