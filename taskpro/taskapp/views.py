from django.shortcuts import render

# Create your views here.
def table(request):
    return render(request, 'table.html')
def form(request):
    return render(request, 'form.html')
def image(request):
    return render(request, 'image.html')
def mylocation(request):
    return render(request, 'mylocation.html')
def video(request):
    return render(request, 'video.html')
