from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django! My Name is Mr Sugeng Riyanto")