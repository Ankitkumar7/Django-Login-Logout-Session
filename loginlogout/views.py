from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponse
from forms import UserForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect



# Create your views here.

# #def log(request):
# 	user = authenticate(username='admin', password='ankit7693')
# 	if user is not None:
# 		return render(request,'log.html',{})
#     # A backend authenticated the credentials
# 	else:
# 		return HttpResponse("<h1>Unauthorised access</h1>")

#     # No backend authenticated the credentials

def main(request):
	if request.user.is_authenticated:
		return render(request, "index.html", {})


	else:
		return HttpResponseRedirect("http://127.0.0.1:8000/user/lib")

  
	
def log(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            new_user.is_staff = True
            new_user.save()
            
            # redirect, or however you want to get to the main view
            return HttpResponseRedirect('http://127.0.0.1:8000/user/lib')
    else:

        form = UserForm() 

    return render(request, 'main.html', {'form': form}) 

