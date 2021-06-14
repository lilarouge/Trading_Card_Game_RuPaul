from django.forms import ModelForm
from .models import *
 
class CreateADiscussion(ModelForm):
    class Meta:
        model= Discussion
        fields = ("topic", "text")
 
class CreateInComment(ModelForm):
    class Meta:
        model= Comment
        fields = ("content",)