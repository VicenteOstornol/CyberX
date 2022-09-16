from django.forms import ModelForm

from .models import Computer

class ComputerForm(ModelForm):
    class Meta:
        model = Computer
        fields = '__all__'