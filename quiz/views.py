from django.shortcuts import render
from .models import Question, Quiz, QuizResponse
from django.http import HttpResponseRedirect, HttpResponse,HttpResponseForbidden
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def quiz_response(request, quiz_id):
    # quiz_obj = Quiz.objects.get_or_404(quiz=quiz_id)
    quiz_question = Question.objects.filter(quiz=quiz_id)
    print('------------>>', quiz_question)
    return render(request,'quiz/quiz_response.html',{'questions': quiz_question})