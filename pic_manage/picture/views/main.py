import logging
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
def homepage_view(request):
    content = {}
    content.update(csrf(request))
    return render_to_response('main.html', content)