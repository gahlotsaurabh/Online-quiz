from django.urls import path, include
from .views import (
                    user_login, quiz_list_and_create,
                    register, UserUpdate, StudentList
                    )
from django.conf.urls import url

app_name = 'admin_user'

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^user_login/$', user_login,name='user_login'),
    # url('', user_login,name='home'),
    path('quiz_list_and_create/<int:quiz_id>/', quiz_list_and_create,name='quiz_list_and_create'),
    path('register/', register,name='register'),
    path('<int:pk>/user_update',UserUpdate.as_view(), name='user_update'),
    path('students_list',StudentList.as_view(), name='students_list'),
]