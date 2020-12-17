from django.db import models

# Create your models here.
class Student(models.Model):
    stu_name = models.CharField(max_length=50)
    stu_grades = models.PositiveIntegerField()
    college = models.CharField(max_length=60)
    major = models.CharField(max_length=60)
    birthday = models.DateField()
    gendle = models.BooleanField()
    student_id = models.BigIntegerField()
    stu_password = models.CharField(max_length=60)

class Teacher(models.Model):
    teach_name = models.CharField(max_length=50)
    teach_gendle = models.BooleanField()
    teach_id = models.PositiveIntegerField()
    teache_age = models.PositiveIntegerField()
    subject = models.CharField(max_length=60)
    teach_password = models.CharField(max_length=60)