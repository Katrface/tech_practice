from django import forms

from .models import ArticleCard

class ArticleCardForm(forms.ModelForm):
    class Meta:
        model = ArticleCard
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'link': forms.TextInput(attrs={'class': 'form-control'}),
            'photo_link': forms.TextInput(attrs={'class': 'form-control'})
        }
