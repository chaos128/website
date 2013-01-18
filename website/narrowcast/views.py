from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext, TemplateDoesNotExist

def home(request):
    """Shows the home page."""
    return render_to_response('base.html', context_instance=RequestContext(request))