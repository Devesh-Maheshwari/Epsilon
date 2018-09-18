from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home/homepage.html')
def about(request):
    return render(request,'home/aboutus.html')
def course(request):
    return render(request,'home/course.html')
def blog(request):
    return render(request,'home/blog.html')
def contact(request):
    return render(request,'home/contactus.html')