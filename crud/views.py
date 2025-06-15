from django.shortcuts import render,redirect
from . models import student

# Create your views here.
def home(request):
    return render(request,'home.html')

def create(request):
    return render(request,'create.html')

def read(request):
    studenttb = student.objects.all()
    return render(request,'read.html',{'studentdata':studenttb})
    
def registration(request):
    rollnum = request.POST['rollnumber']
    sname = request.POST['studentname']
    sbranch = request.POST['stubranch'] 
    sphone = request.POST['stuphone']
    semail = request.POST['stuemail']
    insert = student(rollno=rollnum,name=sname,branch=sbranch,phone=sphone,email=semail)
    insert.save()
    return redirect("/read/")
def delete(request,id):
    deleteid = student.objects.get(id=id)
    deleteid.delete()
    return redirect("/read/")
def edit(request,id):
    edittb = student.objects.get(id=id)
    return render(request,'edit.html',{'editdata':edittb})
def update(request,id):
    newroll = request.POST['rollnumber']
    newname = request.POST['studentname']
    newbranch = request.POST['stubranch']
    newemail =request.POST['stuemail']
    newphone = request.POST['stuphone']
    updateData = student.objects.get(id=id)
    updateData.rollno = newroll
    updateData.name = newname
    updateData.branch = newbranch
    updateData.phone = newphone
    updateData.email = newemail
    updateData.save()
    return redirect("/read/")