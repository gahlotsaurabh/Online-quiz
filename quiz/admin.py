from django.contrib import admin
from .models import Quiz, Question, QuizResponse
# Register your models here.
admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(QuizResponse)