from django.urls import path

from property.api import (
    book_property,
    create_property,
    properties_list,
    property_details,
    property_reservations,
    toggle_favourite,
)

urlpatterns = [
    path("", properties_list, name="api_properties_list"),
    path("create/", create_property, name="create-property"),
    path("<uuid:pk>", property_details, name="ne"),
    path("<uuid:pk>/book/", book_property, name="book_property"),
    path("<uuid:pk>/toggle_favourite/", toggle_favourite, name="toggle_favourite"),
    
]
