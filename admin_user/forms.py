from django import forms
from quiz.models import Quiz, Question
from .models import Profile
from django.contrib.auth.models import User
from django.forms.formsets import formset_factory
from datetime import date
	
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','first_name','last_name','password','email')
    
class UserProfileForm(forms.ModelForm):
    class Meta():
        model = Profile
        fields = ('country', 'birth_date', 'gender', 'phone', 'avatar')


class QuizForm(forms.ModelForm):
    class Meta():
        model = Quiz
        fields = ('name',)

    
class QuestionForm(forms.ModelForm):
    class Meta():
        model = Question
        fields = ('text', 'option1', 'option2', 'option3', 'option4', 'answer', 'quiz')
