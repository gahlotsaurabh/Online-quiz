from django.urls import path
from django.conf.urls import include
from admin_user import urls
from .views import (
                    quiz_response, quiz_submit, quiz_create,
                    QuizReportList, QuestionUpdate, QuizDelete,
                    QuestionDelete
                    )
from django.conf.urls import url

app_name = 'quiz'

urlpatterns = [
    path('quiz-time/<int:quiz_id>', quiz_response, name='quiz-time'),
    path('quiz_submit/', quiz_submit, name='quiz_submit'),
    path('create_quiz/', quiz_create, name='create_quiz'),
    path('report/', QuizReportList.as_view(), name='report'),
    path('<int:pk>/question_update', QuestionUpdate.as_view(), name='question_update'),
    path('<int:pk>/quiz_delete',QuizDelete.as_view(),name='quiz_delete'),
    path('<int:pk>/question_delete',QuestionDelete.as_view(),name='question_delete'),
]