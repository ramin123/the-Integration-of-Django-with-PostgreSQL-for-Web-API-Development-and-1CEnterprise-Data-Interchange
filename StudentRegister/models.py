from django.db import models

# Create your models here.
class Student(models.Model):
    Admission_Number = models.CharField(max_length=50, verbose_name='Admission Number')
    First_Name = models.CharField(max_length=50, verbose_name='First Name')
    Last_Name = models.CharField(max_length=50, verbose_name='Lat Name')
    Date_Of_Birth = models.DateField(max_length=50, verbose_name='Date Of Birth', null=True)
    Date_Joined = models.DateField(verbose_name='Date Joined', null=True)
    Faculty = models.CharField(max_length=50, verbose_name='Faculty')
    Department = models.CharField(max_length=50, verbose_name='Department')
    Course_Name = models.CharField(max_length=50, verbose_name='Course Name')
    Year_Of_Study = models.CharField(max_length=50, verbose_name='Year of Study')
    Unit_Name = models.CharField(max_length=50, verbose_name='Unit Name')
    Grade = models.CharField(max_length=50, verbose_name='Grade')
    send = models.CharField(max_length=50, verbose_name='Grade')

    def __str__(self):
        return self.id