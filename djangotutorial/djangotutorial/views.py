# first insert httpresponse 

from django.http import HttpResponse
from django.shortcuts import render
# define function
def aboutUs(request):
    return HttpResponse("Welcome to About us Page")

def course(request):
    return HttpResponse("<b>Welcome to course Page</b>")

def courseDetails(request,courseId):
    return HttpResponse("Welcome to "+courseId+"Page")

def homepage(request):
     data={
         "title":"Home page",
         "course":["c","c++","java","python"],
         "student":[{"name":"rni","phone_number":123},{"name":"dhruv","phone_number":567}],
         "number":[10,30,50,20]
     }
     return render(request,"index.html", data)

def about_page(request):
    return render (request,"about.html")