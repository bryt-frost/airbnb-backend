from django.forms import ModelForm

from .models import Property


class PropertyForm(ModelForm):
    
    class  Meta:
        model = Property
        fields = [
            "title",
            "description",
            "category",
            "country",
            "country_code",
            "price_per_night",
            "bedrooms",
            "bathrooms",
            "guests",
            "image",
        ]
