from django import forms
from django.http import JsonResponse
from django.core.validators import FileExtensionValidator
from django.shortcuts import render
from xml_converter.helpers import xml_to_dict

class FileForm(forms.Form):
    file = forms.FileField(label='Upload your XML file', validators=[
                               FileExtensionValidator(allowed_extensions=['xml'])])


def upload_page(request):
    if request.method == 'POST':
        xml_dict = {}
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            xml_dict = xml_to_dict(request.FILES['file'])
        return JsonResponse(xml_dict)

    form = FileForm()
    return render(request, "upload_page.html", {'form': form})
