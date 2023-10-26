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

# class Admin_dash(serializers.ModelSerializer):


#! ADMIN END


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


# class StudentsAgeSrl(serializers.ModelSerializer):
#     class Meta:
#         model = Students
#         fields = ("stu_age", )

#! STUDENT END


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


#! TEACHERS END


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

#! GROUP END
