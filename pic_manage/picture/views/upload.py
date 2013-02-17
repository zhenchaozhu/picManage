import os
import json
import time
import datetime
import MySQLdb as mdb
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
        file_path = UPLOAD_FILE_ROOT + time.strftime("%Y%m%d%H%M%S") + '_n' + file_name
        result = save_file(file_path, file)
        if result:
            file_paths.append(file_path)
        else:
            file_paths.append(None)
    return file_paths

def save_file(file_path, file):
    if not os.path.exists(file_path):
        des = open(file_path, 'wb+')
        for chunk in file.chunks():
            des.write(chunk)
        des.close()
        create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_file_path(create_time, file_path)
        return True

def save_file_path(create_time, file_path):
    con = None
    try:
        con = mdb.connect('localhost', 'root', 'zzc', 'picture')
        cur = con.cursor()
        sql = 'insert into picture_picture(create_date, path) values("%s", "%s")'
        cur.execute(sql % (create_time, file_path))
        con.commit()
    finally:
        if con:
            con.close()