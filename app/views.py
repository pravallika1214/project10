from django.shortcuts import render

# Create your views here.
def app_hai(request):
    d={'a':40,'b':60,'c':20}
    return render(request,'app_hai.html',d)
