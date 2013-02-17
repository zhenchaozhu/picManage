import json
from django.http import HttpResponse
from pic_manage.picture.models import Picture
def api_get_pics(request):
    page = request.GET.get('page', 0)
    page = int(page)
    path = Picture.get_path(page)
    return HttpResponse(json.dumps({
        'status': 0,
        'content': path
    }))

