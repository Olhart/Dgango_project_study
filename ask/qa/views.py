from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

def test(request, *args, **kwargs):
    print('We are in test')
    return HttpResponse(f"<h1>Ok</h1>")
 
def test_req(request, *args, **kwargs):
    if len(kwargs['tag']) < 3:
        print("We are found nothing")
        raise Http404()
    if len(kwargs['tag']) > 3:
        print('We are in test_req')
        return redirect('home', permanent=True)
    for t in request.GET.keys():   
        return HttpResponse(f"<h1>Ok</h1><p>{request.GET[t]} {kwargs['tag']}</p>")
    return HttpResponse('Not tag')

def NotFound(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")