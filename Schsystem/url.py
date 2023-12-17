from django.urls import path
from .views import *

urlpatterns = [
    # ? FOR ADMIN URLS
    path("Admin/Log/", AdminLoginView.as_view()),
    path("Admin/Create/", CreatAdminView.as_view()),
    path("Admin/Create_gruop/", CreateGroupView.as_view()),
    path("Admin/Search/", Admin_Searching_Students.as_view()),
    # ? FOR STUDENTS URLS
    path("Student/Log/", StudetnsLoginView.as_view()),
    path("Student/Create/", CreateStudentsView.as_view()),
    path('Students/Homework/<int:pk>/', HomeworkView.as_view()),
    # ? FOR TEACHERS URLS
    path("Teacher/Create/", CreateTeacherView.as_view()),
    path("Teacher/Log/", TeacherLoginView.as_view()),
    path("Teacher/Homework/<str:title>/", HomeworkChange.as_view()),
    path("Teacher/Exam/<str:title>/", ExamGet.as_view()),
    path("Teacher/Create/Homework/", CreateHomework.as_view()),
    path("Teacher/Create/Exam", CreateExam.as_view()),
]
