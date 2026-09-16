from django.http import HttpResponse
from django.shortcuts import render
from students.models import Student
from django.views import View  


class ShowStudentsView(View):
    def get(self, request, *args, **kwargs):
        students = Student.objects.all()
        
        result = ""
        for s in students:
            result += s.name + "<br>"
            
        return HttpResponse(result)

# # Create your views here.
# def show_students(request):
