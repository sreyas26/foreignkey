from django.db import models

# Create your models here.

class Course(models.Model):
    course_name=models.CharField(max_length=255)
    fee=models.IntegerField()
    
    def __str__(self):
        return self.course_name

class Student(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE, null=True)
    student_name=models.CharField(max_length=255)
    student_address=models.CharField(max_length=255)
    student_age=models.IntegerField(null=True,blank=True)
    joining_date=models.DateField() 
    
    def __str__(self):
        return self.student_name