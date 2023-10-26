from django.urls import path
from .views import *

urlpatterns = [
    # ? FOR ADMIN URLS
    path("Admin/log/", AdminLoginView.as_view()),
    path("Admin/create/", CreatAdminView.as_view()),
    path("Admin/create_gruop/", CreateGroupView.as_view()),
    path("Admin/Search/", Admin_Searching_Students.as_view()),
    # ? FOR STUDENTS URLS
    path("Student/log/", StudetnsLoginView.as_view()),
    path("Student/create/", CreateStudentsView.as_view()),

    # ? FOR TEACHERS URLS
    path("Teacher/create/", CreateTeacherView.as_view()),
    path("Teacher/log/", TeacherLoginView.as_view()),
]
