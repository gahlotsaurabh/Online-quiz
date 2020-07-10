from django.shortcuts import render
from quiz.models import Quiz
# Create your views here.
def student_index(request):
    if not request.user.is_staff:
        all_quiz = Quiz.objects.all()
    return render(request,'student/student_index.html',{'quiz': all_quiz})