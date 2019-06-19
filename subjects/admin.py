from django.contrib import admin
from .models import Student, Courses


class AdminStudent(admin.ModelAdmin):
    list_display = ['sname', 'sloc', 'mobile']


class AdminCourses(admin.ModelAdmin):
    list_display = ['cname', 'cfee']


admin.site.register(Student, AdminStudent)
admin.site.register(Courses, AdminCourses)


# Register your models here.
