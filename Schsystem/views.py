# RESTFRAMEWORK AND DRF_YASG IMPORTING FOR USE
from django.shortcuts import render
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
# LOCAL IMPORTING
from .serializer import *
from .models import *

# views here.

##! FOR ADMIN VIEWS START ##!


class AdminLoginView(APIView):
    queryset = Admin.objects.all()
    serializer = LoginAdminSrl()

    @swagger_auto_schema(request_body=LoginAdminSrl)
    def post(self, request):
        admin_phone = request.data.get("admin_phone")
        admin_pass = request.data.get("admin_pass")
        admin = Admin.objects.filter(
            admin_phone=admin_phone, admin_pass=admin_pass
        ).first()
        if admin:
            serializer = CreateAdminSrl(admin)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CreatAdminView(APIView):
    queryset = Admin.objects.all()
    serializer = CreateAdminSrl()
    parser_classes = [MultiPartParser, ]

    @swagger_auto_schema(request_body=CreateAdminSrl)
    def post(self, request):
        admin_phone = request.data.get("admin_phone")
        admin_age = request.data.get("admin_age")
        admin_pass = request.data.get("admin_pass")

        ### VALIDATION ###
        if not admin_phone:
            return Response({"MSG": "ERROR TELL"})
        if int(admin_age) < 20:
            return Response({"MSG": "Older 20 years"})
        if len(admin_pass) != 8:
            return Response({"MSG": "USE 8 LETTERS"})
        ### CREATE ADMIN ###
        admin_srl = CreateAdminSrl(data=request.data)
        if admin_srl.is_valid():
            admin_srl.save()
            return Response(admin_srl.data)
        else:
            return Response({"MSG": "VALID"})


class CreateGroupView(APIView):
    queryset = Group.objects.all()
    serializer = CreateGroupSrl()

    ###  FOR GROUP VIEWS AND THIS VIEWS FOR ADMIN USING  ###
    @swagger_auto_schema(request_body=CreateGroupSrl)
    def post(self, request):
        category = request.data.get('group_category')
        teachers = Teachers.objects.filter(teach_category=category).all()

        teacher_data = []

        for teacher in teachers:
            group_count = Group.objects.filter(
                group_teachers=teacher.id).count()
            teacher_data.append({
                "teach_name": teacher.teach_name,
                "teach_lastname": teacher.teach_lastname,
                "teach_category": teacher.teach_category,
                "group_count": group_count,
            })

        srl_for_teach = ForteachersGroup(teacher_data, many=True)
        age = request.data.get('group_age')
        if age == 'YOUNG':
            #  yosh bilan group borligi yoki yoqliginu tekishiradigan filter
            students = Students.objects.filter(
                stu_age__gte=10, stu_age__lt=14, is_have=False
            )  # ? lookup filters __gte va __lt katta bosa , kichik bolsa
            srl_for_stu = CreateStuSrl(students, many=True)
            return Response({"Teachers": srl_for_teach.data, "Students": srl_for_stu.data})
        elif age == 'OLDER':
            #  yosh bilan group borligi yoki yoqliginu tekishiradigan filter
            students1 = Students.objects.filter(
                stu_age__gte=14, stu_age__lt=17, is_have=False
            )
            srl_for_stu = CreateStuSrl(students1, many=True)
            return Response({"Teachers": srl_for_teach.data, "Students": srl_for_stu.data})
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class Admin_Searching_Students(APIView):
    queryset = Students.objects.all()
    queryset2 = Group.objects.all()
    request_srl = SearchStuSrl()
    data_srl = CreateStuSrl()

    ### SEARCHING STUDENT FROM ADMIN ###
    @swagger_auto_schema(request_body=SearchStuSrl)
    def post(self, request):
        name = request.data.get("stu_name")
        last_name = request.data.get("stu_lastname")

        if last_name == "Null":
            students = Students.objects.filter(stu_name=name)
            if students.exists():
                serializer = CreateStuSrl(students, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            student = Students.objects.filter(
                stu_name=name, stu_lastname=last_name).first()  # studentni fliter qiladi
            if not student:
                return Response(status=status.HTTP_404_NOT_FOUND)

            # gruppasini filter qiladi
            student_id = student.id
            group = Group.objects.filter(group_students=student_id).first()

            # studentni serializerlari
            srl_data_srl = CreateStuSrl(student)
            srl_group_srl = GroupIs_HaveSrl(group)

            return Response({"Students": srl_data_srl.data, "Group": srl_group_srl.data})


##! ADMIN END ###


##! FOR STUNDETS VIEWS START ##!

class StudetnsLoginView(APIView):
    queryset = Students.objects.all()
    serializer = LoginStuSrl()

    @swagger_auto_schema(request_body=LoginStuSrl)
    def post(self, request):
        student_id = request.data.get("stu_id ")
        student_pass = request.data.get("stu_pass")
        stu_user = Students.objects.filter(
            stu_id=student_id, stu_pass=student_pass
        ).first()
        if stu_user:
            serializer = LoginStuSrl(stu_user)
            return Response(serializer, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CreateStudentsView(APIView):
    queryset = Students.objects.all()
    serializer = CreateStuSrl()
    parser_classes = [MultiPartParser, ]

    @swagger_auto_schema(request_body=CreateStuSrl,)
    def post(self, request):
        re_age = int(request.data.get("stu_age"))
        ### VALIDATION ###
        if 10 <= re_age <= 16:
            re_phone = request.data.get("stu_phone")

            if not re_phone:
                return Response({"MSG": "Phone cannot be null"}, status=status.HTTP_400_BAD_REQUEST)

            re_pass = request.data.get("stu_pass")
            if len(re_pass) != 8:
                return Response({"MSG": "Password should be 8 characters long"}, status=status.HTTP_400_BAD_REQUEST)
            ### CREATE STUDENTS ###
            stu_srl = CreateStuSrl(data=request.data)
            if stu_srl.is_valid():
                return Response({"MSG": "Successfully"}, status=status.HTTP_200_OK)
            else:
                return Response(stu_srl.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"MSG": "Age should be between 10 and 16"}, status=status.HTTP_400_BAD_REQUEST)


##! STUDENTS END ###


##! FOR TEACHERS VIEWS START ###

class TeacherLoginView(APIView):
    queryset = Teachers.objects.all()
    serializer = LoginTeachSrl()

    @swagger_auto_schema(request_body=LoginTeachSrl)
    def post(self, request):
        teacher_phone = request.data.get("teach_phone")
        teacher_pass = request.data.get("teach_pass")
        teacher = Teachers.objects.filter(
            teach_phone=teacher_phone, teach_pass=teacher_pass
        ).first()

        if teacher:
            serializer = CreateTeachSrl(teacher)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CreateTeacherView(APIView):
    queryset = Teachers
    serializer = CreateTeachSrl()

    parser_classes = [MultiPartParser,]

    @swagger_auto_schema(request_body=CreateTeachSrl)
    def post(self, request):
        teach_age = request.data.get("teach_age")
        teach_pass = request.data.get("teach_pass")
        ### VALIDATION ###
        if int(teach_age) < 20:
            return Response({"MSG": "Bigger than 20"})
        if teach_pass != 8:
            return Response({"MSG": "USE 8 LETTERS"})
        ### CREATE TEACHERS ###
        teach_srl = CreateTeachSrl(data=request.data)
        if teach_srl.is_valid():
            return Response({"MSG": "succsessfuly"}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

##! TEACHER END ###
