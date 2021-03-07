from django.shortcuts import render
from . import models , forms
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

# Create your views here.
def home (request):
    contex ={}

    return render (request , 'users/home.html' , contex)

def ostads (request):
    contex ={}

    return render (request , 'users/ostads.html' , contex)


def students (request):
    contex ={}

    return render (request , 'users/students.html' , contex)


def students_tamrin (request):
    tamrin = models.Tamrin.objects.all()
    contex ={'tamrin' : tamrin}

    return render (request , 'users/students_tamrin.html' , contex)

def students_videos (request):
    videos = models.Videos.objects.all()
    contex ={'videos' : videos}

    return render (request , 'users/students_videos.html' , contex)

def ostads_tamrin (request):
    tamrin = models.Tamrin.objects.all()
    contex ={'tamrin' : tamrin}

    return render (request , 'users/ostads_tamrin.html' , contex)



def ostads_tamrin_javab (request,javab_id):

    javab=models.Javab.objects.filter(tamrin=models.Tamrin.objects.get(id=javab_id))
  
    contex={'javab':javab}
    return render (request , 'users/ostads_tamrin_javab.html' , contex)


def ostads_videos (request):
    videos = models.Videos.objects.all()
    contex ={'videos' : videos}

    return render (request , 'users/ostads_videos.html' , contex)


def student_tamrin_upload (request):
    form = forms.student_tamrin_upload
    if request.method == 'POST':
        form = forms.student_tamrin_upload(request.POST , request.FILES)
        if form.is_valid ():
            form.save()
            return HttpResponse ("tamrin ba movafaghiat upload shod")

    contex ={'form' : form}


    return render (request , 'users/ostads_tamrin_upload.html' , contex)

def ostads_tamrin_upload (request):
    form = forms.Ostads_tamrin_upload
    if request.method == 'POST':
        form = forms.Ostads_tamrin_upload(request.POST , request.FILES)
        if form.is_valid ():
            form.save()
            return HttpResponse ("tamrin upload shod")

    contex ={'form' : form}


    return render (request , 'users/ostads_tamrin_upload.html' , contex)



def ostads_videos_upload (request):
    form = forms.Ostads_videos_upload
    if request.method == 'POST':
        form = forms.Ostads_videos_upload(request.POST , request.FILES)
        if form.is_valid ():
            form.save()
            return HttpResponse ("video upload shod")

    contex ={'form' : form}


    return render (request , 'users/ostads_videos_upload.html' , contex)


def ostads_videos_seen (reauest , videoid):
    return render(reauest, 'users/ostads_videos_seen.html',{'video':models.Videos.objects.get(id=videoid)})



def user_login(request):
    if request.method == 'POST':
       
        username = request.POST['username']
        password = request.POST['password']
       
        user = authenticate(username=username, password=password)
        if user is not None:
            
            login(request, user)
            
            return render(request, 'users/account.html')
        else:
            
            return render(request, 'users/login.html', {'error_message': 'Incorrect username and / or password.'})
    else:
        
        return render(request, 'users/login.html')