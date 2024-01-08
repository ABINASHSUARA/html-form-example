from django.shortcuts import render

# Create your views here.
def htmlform(request):
    return render(request,'htmlform.html')

def htmlform1(request):
    return render(request,'htmlform1.html')