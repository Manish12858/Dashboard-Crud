from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.
def add_show(req):
    if req.method=='POST':
        fm=StudentRegistration(req.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=pw)
            
            reg.save()
            return HttpResponseRedirect('/')
            # fm=StudentRegistration()
    else:
        fm=StudentRegistration()
    stud=User.objects.all()
    return render(req,'enroll/addandshow.html',{'form':fm,'stud':stud});


def update_data(req,id):
    if req.method=='POST':
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(req.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
    return render(req,'enroll/updatestudent.html',{'form':fm})


def delete_data(req,id):
    if req.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')