from django.shortcuts import render,HttpResponse

# Create your views here.
def portfolio(request):
    return render(request,"src/portfolio.html")
def about(request):
    return render(request,"src/about.html")
def contact(request):
    return render(request,"src/contact.html")