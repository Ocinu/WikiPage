from django import forms



class CreateNewPage(forms.Form):
    title = forms.CharField(max_length=250,
                            label="Назва сторінки",
                            widget=forms.TextInput(attrs={
                                "class": "form-control"}))
    content = forms.CharField(max_length=250,
                              label="Опис статті",
                              widget=forms.Textarea(attrs={
                                  "class": "form-control",
                                  "rows": 5}))


class EditPage(forms.Form):
    title = forms.CharField(max_length=250,
                            label="Назва сторінки",
                            widget=forms.TextInput(attrs={
                                "class": "form-control"}))
    content = forms.CharField(max_length=250,
                              label="Опис статті",
                              widget=forms.Textarea(attrs={
                                  "class": "form-control",
                                  "rows": 5}))
