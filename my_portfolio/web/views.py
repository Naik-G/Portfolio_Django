from django.shortcuts import render

# Create your views here.
def index(requests):
    return render(requests,'index.html')
    
def education(requests):
    return render(requests,'education.html')
    
def skills(requests):
    return render(requests,'skills.html')
    
def certification(requests):
    return render(requests,'certification.html')
    
def projects(requests):
    return render(requests,'projects.html')
    
