from django.shortcuts import render

# Create your views here.
def t1(request):
    return render(request,'t1.html')
def table(request):
    return render(request,'table.html')