from django.shortcuts import render, get_object_or_404
from .forms import QuestionForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse,HttpResponseForbidden
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.forms import modelformset_factory
from django.views.generic import (ListView,DetailView,UpdateView,DeleteView)
from .models import Profile
# from .filters import ProductFilter
from django.forms.models import model_to_dict
from django.contrib.auth.models import User

from quiz.models import Question, Quiz
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse,HttpResponseForbidden


def admin_index(request):
    if request.user.is_staff:
        all_quiz = Quiz.objects.all()
        return render(request,'admin_user/admin_index.html',{'quiz': all_quiz})
    return render(request,'admin_user/login.html')


def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username,password=password)
		if user:
			login(request,user)
			if user.is_staff:
				return HttpResponseRedirect(reverse('admin_index'))
			else:
				return HttpResponseRedirect(reverse('student_index'))
		else:
			print("someone tried to login and failed.!")
			print("they used username: {} and password:{}".format(username,password))
			return HttpResponse("Invalid login details given")
	else:
		return render(request,'admin_user/login.html',{})


@method_decorator(login_required, name='dispatch')
class QuizList(ListView):
    template_name 	= 'admin_user/admin_index.html'
    queryset 	  	= Quiz.objects.all()
    ordering 		= ['id']

@login_required
def quiz_list_and_create(request,quiz_id):
    if request.user.is_staff:
        form = QuestionForm(request.POST or None)
        if request.method == 'POST' and form.is_valid():
            form.save()
            form = QuestionForm()
        questions = Question.objects.filter(quiz=quiz_id)
        return render(request, 'admin_user/quiz_question_create.html', {'questions': questions, 'form': form})

def register(request):
	registered = False
	if request.method =='POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			if 'profile_pic' in request.FILES:
				print('found it')
				profile.profile_pic = request.FILES['profile_pic']
			profile.save()
			user_form = UserForm()
			profile_form = UserProfileForm()
			registered = True
		else:
			print(user_form.errors,profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	return render(request,'admin_user/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})


@login_required
def user_logout(request):
	logout(request)
	return render(request,'admin_user/login.html',{})

@method_decorator(login_required, name='dispatch')
class UserUpdate(UpdateView):
	form_class = UserProfileForm
	template_name = 'admin_user/registration.html'
	queryset = Profile.objects.all()

	def get_success_url(self,request):
		return render(request,'admin_user/login.html')
		# return reverse('chandler:user_list')
