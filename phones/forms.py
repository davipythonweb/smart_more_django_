from django import forms
from phones.models import Phone

class PhoneModelForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = '__all__'
        
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 2500:
            self.add_error('value', 'valor de iphone deve ser de R$2.500.' )
            
    def clean_release_year(self):
        release_year = self.cleaned_data.get('release_year')
        if release_year < 2018:
            self.add_error('release_year', 'Não é possivel cadastrar iphones laçados antes de 2018.')
            
            
            