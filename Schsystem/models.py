from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

# Chooses
dagre_poll = [
    ("WOMEN", "WOMEN"),
    ("MAN", "MAN"),
]
category = [
    ("FRONTEND", "FRONTEND"),
    ("BACKEND", "BACKEND")
]
stu_roll = [
    ("GAMER", "GAMER"),
    ("HACKER", "HACKER"),
    ("CODER", "CODER")
]
job = [
    ("TUTOR", "TUTOR"),
    ("INCTRUCTOR", "INCTRUCTOR"),
    ("MENTOR", "MENTOR")

]
teach_level = [
    ("JUNIOR", "JUINOR"),
    ("MIDDLE", "MIDDLE"),
    ("SENIOR", "SERIOR")
]
age = [
    ("YOUNG", "YOUNG"),  # 10-13
    ("OLDER", "OLDER"),  # 14-16
]
# Chooses end


# ADMIN MODELI
class Admin(models.Model):
    admin_name = models.CharField(max_length=100)
    admin_lastname = models.CharField(max_length=100)
    admin_age = models.IntegerField()
    admin_phone = models.CharField(max_length=100, unique=True)
    admin_pass = models.CharField(max_length=8, unique=True)
    admin_poll = models.CharField(
        choices=dagre_poll, blank=True, max_length=100
    )

    def __str__(self):
        return self.admin_name


# STUDENTS MODELI
class Students(models.Model):
    stu_name = models.CharField(max_length=100)
    stu_lastname = models.CharField(max_length=100)
    stu_age = models.IntegerField()
    stu_phone = models.CharField(max_length=100, unique=True)
    stu_parents_name = models.CharField(max_length=100)
    stu_parents_phone = models.CharField(max_length=100, unique=True)
    stu_id = models.CharField(max_length=100, unique=True)
    stu_pass = models.CharField(max_length=8, unique=True)
    stu_category = models.CharField(
        max_length=100, choices=category, blank=True
    )
    stu_roll = models.CharField(
        max_length=100, choices=stu_roll, blank=True
    )
    result = models.IntegerField(null=True)
    stu_coin = models.IntegerField(null=True)
    is_have = models.BooleanField(default=False)
    stu_paymant = models.BooleanField(default=False)

    def __str__(self):
        return self.stu_name


# TEACHERNI MODELI
class Teachers(models.Model):
    teach_name = models.CharField(max_length=100)
    teach_lastname = models.CharField(max_length=100)
    teach_age = models.IntegerField()
    teach_phone = models.CharField(max_length=100, unique=True)
    teach_pass = models.CharField(max_length=8, unique=True)
    teach_email = models.EmailField()
    teach_level = models.CharField(
        max_length=100, choices=teach_level, blank=True
    )
    tech_job = models.CharField(max_length=100, choices=job, blank=True)
    teach_category = models.CharField(
        max_length=100, choices=category, blank=True
    )
    teach_poll = models.CharField(
        max_length=100, choices=dagre_poll, blank=True
    )
    result = models.IntegerField(null=True)

    def __str__(self):
        return self.teach_name


# GROUP MODELI
class Group(models.Model):
    group_name = models.CharField(max_length=100, unique=True)
    group_time = models.TimeField()
    group_category = models.CharField(
        choices=category, blank=True, max_length=100
    )
    group_age = models.CharField(max_length=255, choices=age)
    group_teachers = models.ForeignKey(
        Teachers, on_delete=models.CASCADE)
    group_students = models.ManyToManyField(Students)

    def __str__(self):
        return self.group_name
