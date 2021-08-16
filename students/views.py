from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from students.forms import SignupForm


# Create your views here.
def indexView(request):
    return render(request,'index.html')
def dashboardView(request):
    return render(request,'dashboard.html')
def coursesView(request):
    return render(request,'courses.html')
def accountingView(request):
    return render(request,'accounting.html')
def softdevView(request):
    return render(request,'softdev.html')
def ITView(request):
    return render(request,'IT.html')
def csView(request):
    return render(request,'cs.html')
def statView(request):
    return render(request,'stat.html')
def GDcoursedetailsView(request):
    return render(request,'GDcoursedetails.html')
def aboutView(request):
    return render(request,'about.html')
def contactView(request):
    return render(request,'contact.html')
def trainersView(request):
    return render(request,'trainers.html')
def registerView(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            user= form.cleaned_data.get('POST')
            raw_password = form.cleaned_data.get('password1')
            email=form.cleaned_data.get('email')
            course=form.cleaned_data.get('course')
            user=  authenticate(username=user,password=raw_password,email=email,course=course)
            login(request,user)
            return redirect('dashboard_url')
    else:
        form = SignupForm()
    return render(request, 'registration/register.html',{'form':form})