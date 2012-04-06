from django.forms import ModelForm, HiddenInput, TextInput, BooleanField
from places.models import PlaceType, Place

class PlaceTypeForm(ModelForm):
    """
    PlaceType model form
    """
    class Meta:
        model = PlaceType
        exclude = ('slug', )

class PlaceForm(ModelForm):
    """
    Place model form, used in formset
    """
    class Meta:
        model = Place
        # used to hide position input in the place form
        widgets = {
            # below, position field class used to link widget w/ field
            'position':HiddenInput(attrs={'class':'marker'}), 
            'comment':TextInput(attrs={'placeholder': 'Comment', 'class':'span3'}),
            'title':TextInput(attrs={'placeholder': 'Title', 'class':'input-medium'}),
        }