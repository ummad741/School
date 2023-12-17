from django.contrib import admin
from .models import (Admin, Students, Teachers, Group, Homework, Exam)

admin.site.register(Admin)
admin.site.register(Students)
admin.site.register(Teachers)
admin.site.register(Group)
admin.site.register(Homework)
admin.site.register(Exam)
