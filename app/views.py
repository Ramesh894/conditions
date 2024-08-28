from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':1000,'b':500,'c':3000}
    return render(request,'conditions.html',context=d)

def loop(request):
    d={'name':'ashu','mobile':[1234,6789]}
    return render(request,'loop.html',d)