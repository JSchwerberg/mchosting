from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from hosting.models import MinecraftPlan, MinecraftFeature

# Create your views here.
def index(request):

    return HttpResponse("Hello, world.  You're at the index.")
