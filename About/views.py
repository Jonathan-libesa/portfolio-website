from django.shortcuts import render
from steel.models import*
# Create your views here.



def aboutpage(request):
	
	about=About.objects.all()
	context={'about':about}
	return render(request,'about/about us.html',context)