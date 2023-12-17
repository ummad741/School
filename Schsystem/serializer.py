from rest_framework import serializers
from .models import *


#! FOR ADMINS SERIALIZERS START
class LoginAdminSrl(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ("admin_phone", "admin_pass")


class CreateAdminSrl(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = "__all__"


#! FOR STUNDETS SERIALIZERS START
class LoginStuSrl(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ("stu_id", "stu_pass")


class SearchStuSrl(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ('stu_name', "stu_lastname")


class CreateStuSrl(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"


#! FOR TEACHER SERIALIZERS START
class LoginTeachSrl(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = ("teach_phone", "teach_pass")


class CreateTeachSrl(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = "__all__"


class ForteachersGroup(serializers.Serializer):
    teach_name = serializers.CharField()
    teach_lastname = serializers.CharField()
    teach_category = serializers.CharField()
    group_count = serializers.CharField()


#! FOR GROUP SERIALIZERS START
class CreateGroupSrl(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class GroupIs_HaveSrl(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('group_name', 'group_time', 'group_category',
                  'group_age', 'group_teachers')


##!For Homework serializers ###

class ShowHomework(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = '__all__'


##!For Exam serializers ###

class CreateExam(serializers.Serializer):
    class Meta:
        model = Exam
        fields = "__all__"


class ShowExam(serializers.ModelSerializer):
    class Meta:
        model = ThemeExam
        fields = "__all__"
