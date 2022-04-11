from django.contrib import admin
from .models import StudentsData

class AdminStudentsData(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','mobile','course','location','assignment1','assignment2','assignment3','assignment4']
admin.site.register(StudentsData,AdminStudentsData)
