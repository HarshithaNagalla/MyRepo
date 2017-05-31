from django.http import HttpResponse
from django.shortcuts import render
import os
from django.conf import settings
from forms import *
from wsgiref.util import FileWrapper
import mimetypes
from sparkpost import SparkPost
import base64
import csv


def upload_file(file):
        upload_file_path = settings.MEDIA_ROOT + file.name
        with open(upload_file_path, 'w') as upload:
                for chunk in file.chunks():
                        upload.write(chunk)

        return upload_file_path


# Create your views here.

def upload_form(request):
	form = image_upload_form()
        return render(request, 'upload_image.html', {"form":form})

def convert_image(request):
	print "hi"
	form = image_upload_form(data=request.POST, files=request.FILES)
	if form.is_valid():
		print "valid"
                image_form = form.save(commit=False)
		image_form.FirstName = request.POST.get('FirstName', '')
		image_form.LastName = request.POST.get('LastName', '')
		image_form.EmailAddress = request.POST.get('EmailAddress', '')
		image_form.Phone = request.POST.get('Phone', '')
                image_form.path = upload_file(request.FILES["path"])
		image_form.save()
		image = image_form.path
		image = image.name
		query = "convert "+image+" -resize 200x230! -quality 100 "+settings.MEDIA_ROOT+"image.jpg"
		os.system(query)
		print image
		
		wrapper = FileWrapper(open(settings.MEDIA_ROOT+"image.jpg"))  # img.file returns full path to the image
		content_type = mimetypes.guess_type(settings.MEDIA_ROOT+"image.jpg")
		response = HttpResponse(wrapper,content_type=content_type)
                response['Content-Disposition'] = 'attachment; filename="image.jpg"'
                response['Set-Cookie'] = "fileDownload=true; path=/"
		os.system("rm -f "+ image)
		return response
	else:
                print form.errors
	return render(request, 'success.html')

def success(request):
        return render(request, 'success.html')

def download_leads(request):
        return render(request, 'download_leads.html')

def download(request):
        all_entries = image_upload.objects.all()
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment;filename=export.csv'
        writer = csv.writer(response)
	writer.writerow(["FirstName", "LastName", "EmailAddress","Phone"])
        for obj in all_entries:
                writer.writerow([obj.FirstName,obj.LastName, obj.EmailAddress, obj.Phone])
        image_upload.objects.all().delete()

        return response




















