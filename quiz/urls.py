from django.urls import path
from django.conf.urls import include
from admin_user import urls
from .views import quiz_response
from django.conf.urls import url

app_name = 'quiz'

urlpatterns = [
    path('quiz-time/<int:quiz_id>', quiz_response, name='quiz-time'),
]