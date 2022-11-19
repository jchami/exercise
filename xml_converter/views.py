from django import forms
from django.http import JsonResponse
from django.shortcuts import render
from xml_converter.helpers import xml_to_dict


class FileForm(forms.Form):
    file = forms.FileField(label='Upload your XML file')


def upload_page(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            xml_file = request.FILES['file']
            if xml_file.name[-4:] != '.xml':
                return render(request, "upload_page.html", {
                    'error': 'Please submit a valid XML file.',
                    'form': form
                })

            xml_dict = xml_to_dict(xml_file)
            if xml_dict == None:
                return render(request, "upload_page.html", {
                    'error': 'Failed to parse provided XML file.',
                    'form': form
                })
            return JsonResponse(xml_dict)

    form = FileForm()
    return render(request, "upload_page.html", {'form': form})
