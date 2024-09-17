from django.forms import ModelForm
from main.models import AtributEntery

class AtributEntryForm(ModelForm):
    class Meta:
        model = AtributEntery
        fields = ["name", "quantity","price", "description"]