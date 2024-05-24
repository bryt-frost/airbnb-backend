from attr import fields
from rest_framework import serializers

from useraccount.serializers import UserDetailsSerializer
from .models import Property, Reservation


class PropertiesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ["id", "image_url", "price_per_night", "title"]


class PropertyDetailSerializer(serializers.ModelSerializer):
    landlord = UserDetailsSerializer(read_only=True)

    class Meta:
        model = Property
        fields = [
            "id",
            "image_url",
            "price_per_night",
            "title",
            "description",
            "bedrooms",
            "bathrooms",
            "guests",
            "landlord",
        ]


class ReservationsListSerializer(serializers.ModelSerializer):
    property=PropertiesListSerializer(read_only=True,many=False)
    class Meta:
        model = Reservation
        fields = "__all__"
