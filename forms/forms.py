from django.forms import ModelForm
from django import forms
from .models import Student
from forms.models import *
# from formValidationApp.models import *


# class InputForm(forms.Form):
#     first_name = forms.CharField(max_length=200)
#     last_name = forms.CharField(max_length=200)
#     roll_number = forms.IntegerField(widget=forms.TextInput())
#     password = forms.CharField(widget=forms.PasswordInput())
#     date = forms.DateField(widget=forms.SelectDateWidget)
#


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {'password': forms.PasswordInput()}


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["username", "gender", "text"]

    def clean(self):

        super(PostForm, self).clean()

        username = self.cleaned_data.get('username')
        text = self.cleaned_data.get('text')

        if len(username) < 5:
            self._errors['username'] = self.error_class([
                'Minimum 5 characters required'])
        if len(text) < 10:
            self._errors['text'] = self.error_class([
                'Post Should Contain a minimum of 10 characters'])

        return self.cleaned_data
