from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(label='Pesquisar', max_length=100)
