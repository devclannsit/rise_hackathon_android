from django.shortcuts import render
from django.http.response import HttpResponseNotFound, HttpResponseRedirect,HttpResponse
from users.forms import FileForm,AdhaarForm,LoginForm
from users.models import Test,Adhaar,LoggedIn
import schemes

# Create your views here.
def home(request):
    '''form=FileForm()
    context={'form':form}
    return render(request, 'users/home.html',context)'''
    return render(request, "users/index.html")

def makeaccount(request):
    if request.method == "GET":
        print request
        data=request.GET["name"]
        p=Test(name=data)
        p.save()
        return "done"
def register(request):
    if request.POST:
        form = AdhaarForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login/')
        else:
            context={'form':form}
            return render(request, 'users/register.html',context)
            
    else:
        form = AdhaarForm()
        context={'form':form}
        return render(request, 'users/register.html',context)
def login(request):
    request.session['logged_user']=""
    if not request.POST:
        form=LoginForm()
        context={'form':form}
        return render(request, 'users/login.html',context)
    if request.POST:
        form=LoginForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data.get('uid')
            pincode=form.cleaned_data.get('pc')
            a=Adhaar.objects.get(uid__exact = name)
            if(a.pc==pincode):
                request.session['logged_user'] = name
                return HttpResponseRedirect('/profile/')
            else:
                return HttpResponseRedirect('/login/')
def profile(request):
    if request.session['logged_user'] != "":
        name=request.session['logged_user']
    
        a=Adhaar.objects.get(uid__exact=name)
        context={'a':a, 'schemes' : schemes.data}
        return render(request,'users/profile.html',context)
    else:
        return HttpResponseRedirect('/login/')
def logout(request):
    request.session['logged_user']=""
    del request.session['logged_user']
    return HttpResponseRedirect('/')
        
    
