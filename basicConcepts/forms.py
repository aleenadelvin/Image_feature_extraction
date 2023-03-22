from django import forms

from .models import ImageData

class Form(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = ImageData