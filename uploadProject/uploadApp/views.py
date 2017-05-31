from django.shortcuts import render
from models import *
from forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings


# Helper functions
def upload_file(file, dir):
        upload_file_path = settings.MEDIA_ROOT + dir + '/' + file.name
        with open(upload_file_path, 'w') as upload:
                for chunk in file.chunks():
                        upload.write(chunk)

        return upload_file_path

# Create your views here.
def name(request):
	form = FilesForm()
        return render(request, 'uploadFile.html', {"form":form})

def upload(request):
	form = FilesForm(request.POST, request.FILES)
	
	if form.is_valid():
		files_obj = form.save(commit=False)
		files_obj.file_path_one = upload_file(request.FILES["file_path_one"], "csvs")
                files_obj.save()
		return HttpResponseRedirect('/uploadApp/success/')
	else:
		return HttpResponseRedirect('/uploadApp/retry/')

def success(request):
	return render(request, 'success.html')

def tryAgain(request):
        return render(request, 'tryAgain.html')

def viewNames(request):
        return render(request, 'success.html')


