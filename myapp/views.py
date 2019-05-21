from django.shortcuts import render
from django.http import HttpResponse
from wig.wig import wig
import json

# Create your views here.

def home(request):
    w = wig(url='github.com')
    w.run()
    results = w.get_results()
    return HttpResponse(json.dumps(results));
