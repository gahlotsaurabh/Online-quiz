from django.shortcuts import render
from .models import Question, Quiz, QuizResponse
from django.http import HttpResponseRedirect, HttpResponse,HttpResponseForbidden
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import QuizForm
from admin_user.forms import QuestionForm
from admin_user.views import admin_index
from django.views.generic import (ListView,DetailView,UpdateView,DeleteView)

@login_required
def quiz_response(request, quiz_id):
    # quiz_obj = Quiz.objects.get_or_404(quiz=quiz_id)
    quiz_question = Question.objects.filter(quiz=quiz_id)
    return render(request,'quiz/quiz_response.html',{'questions': quiz_question})

@login_required
def quiz_submit(request):
    if request.method =='POST':
        quiz_question = Question.objects.filter(quiz=int(request.POST['quiz']))
        correct_ans_count = 0
        for i in quiz_question:
            if request.POST[str(i.id)] == i.answer:
                correct_ans_count += 1
        quiz_obj = Quiz.objects.get(id=int(request.POST['quiz']))
        if QuizResponse.objects.filter(quiz=quiz_obj,user=request.user):
            attempted = QuizResponse.objects.filter(quiz=quiz_obj,user=request.user).first()
            QuizResponse.objects.filter(quiz=quiz_obj,user=request.user).update(
                is_passed=correct_ans_count*100 / quiz_question.count() > 60,
                attempts=attempted.attempts+1
            )
            return HttpResponseRedirect(reverse('student_index'))
        QuizResponse.objects.create(
            user=request.user, quiz=quiz_obj,
            is_passed=correct_ans_count*100 / quiz_question.count() > 60, attempts=1
            )
        return HttpResponseRedirect(reverse('student_index'))

@login_required
def quiz_create(request):
    form = QuizForm(request.POST)
    if request.method =='POST':
        if form.is_valid():
            post=form.save(commit=True)
            return HttpResponseRedirect(reverse('admin_index'))
        else:
            return render(request,'quiz/quiz_create.html',{'form': form})
    else:
        form = QuizForm()
        return render(request,'quiz/quiz_create.html',{'form':form}) 


class QuizReportList(ListView):
    template_name 	= 'quiz/quiz_report.html'
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return QuizResponse.objects.all()
        return QuizResponse.objects.filter(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class QuestionUpdate(UpdateView):
    form_class = QuestionForm
    template_name = 'quiz/edit_question.html'
    queryset = Question.objects.all()

    def get_success_url(self):
        self.object = self.get_object()
        return reverse('admin_user:quiz_list_and_create', kwargs={'quiz_id':self.object.quiz.id})


@method_decorator(login_required, name='dispatch')
class QuizDelete(DeleteView):
	queryset = Quiz.objects.all()

	def get_success_url(self):
		return reverse('admin_index')

@method_decorator(login_required, name='dispatch')
class QuestionDelete(DeleteView):
    queryset = Question.objects.all()

    def get_success_url(self):
        return reverse('admin_index')