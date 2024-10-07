from django.forms import ModelForm
from main.models import AtributEntery
from django.utils.html import strip_tags

class AtributEntryForm(ModelForm):
    class Meta:
        model = AtributEntery
        fields = ["name", "quantity", "price", "image_url", "description"]
    
    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)
    
    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)
    
