import os
import json
from django.http import HttpResponse
from pic_manage.settings import UPLOAD_FILE_ROOT
def upload_files(request):
    files = request.FILES
    context = {
        'paths': get_file_paths(files)
    }
    return HttpResponse(json.dumps({
        'status': 0,
        'data': context
    }))
def get_file_paths(files):
    file_paths = []
    for file in files.values():
        file_name = file.name
        file_path = UPLOAD_FILE_ROOT + file_name
        result = save_file(file_path, file)
        if result:
            file_paths.append(file_path)
        else:
            file_paths.append(False)
    return file_paths
def save_file(file_path, file):
    if not os.path.exists(file_path):
        destination = open(file_path, 'wb+')
        for chunk in file.chunks():
            destination.write(chunk)
        destination.close()
        return true

