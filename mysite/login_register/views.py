from django.shortcuts import render , render_to_response
from django.http import HttpResponse , HttpResponseRedirect
from django.template import loader
from mysite import settings
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
# Create your views here.



def Login(request):
	next = request.GET.get('next','/main/home/')
	if request.method  == "POST" :
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username = username , password = password)

		if user is not None :
			if user.is_active :
				login(request, user)
				return HttpResponseRedirect(next)
			else :
				return HttpResponse("Inactive User") 
		else:
			return HttpResponseRedirect(settings.LOGIN_URL)
	return render(request, "login_register/login.html", {'redirect_to' : next})

def Logout(request):
	logout(request)
	return HttpResponseRedirect(settings.LOGIN_URL)


@login_required
def home(request):
	return render(request, "login_register/home.html")

def Blog(request):
	return render(request, "login_register/Blog.html")

def register_user(request):
	if request.method == "POST" :
			form = UserCreationForm(request.POST)
			if form.is_valid() :
				form.save()
				return HttpResponseRedirect('/main/Register_Success')

	args = {}
	args.update(csrf(request))
	args['form'] = UserCreationForm()
	return render_to_response('login_register/register.html', args	)


def register_Success(request):
	return render_to_response('login_register/register_Success.html')
