from django.db import models
from django.db.models.query import QuerySet
class Emp(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=50)
    loc = models.CharField(max_length=100)
    salary = models.IntegerField()

    def __str__(self):
        return self.objects

class Student(models.Model):
        sname=models.CharField(max_length=100)
        sloc = models.CharField(max_length=100)
        mobile = models.BigIntegerField()

        def __str__(self):
            return self.sname
class Courses(models.Model):
        abc=models.OneToOneField(Student, on_delete=models.CASCADE)
        cname=models.CharField(max_length=100)
        cfee=models.IntegerField()
        def __str__(self):
            return self.cname


# Create your models here.
