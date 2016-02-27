from django.shortcuts import render , render_to_response
from django.http import HttpResponse , HttpResponseRedirect
from .models import Question
from django.template import loader
from mysite import settings
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
# Create your views here.



def Login(request):
	next = request.GET.get('next','/home/')
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
	return render(request, "Polls/login.html", {'redirect_to' : next})

def Logout(request):
	logout(request)
	return HttpResponseRedirect(settings.LOGIN_URL)


@login_required
def home(request):
	return render(request, "Polls/home.html")

def Blog(request):
	return render(request, "Polls/Blog.html")

def register_user(request):
	if request.method == "POST" :
			form = UserCreationForm(request.POST)
			if form.is_valid() :
				form.save()
				return HttpResponseRedirect('/Register_Success')

	args = {}
	args.update(csrf(request))
	args['form'] = UserCreationForm()
	return render_to_response('Polls/register.html', args	)


def register_Success(request):
	return render_to_response('Polls/register_Success.html')

# def index(request) :
# 	latest_question_list = Question.objects.order_by('-pub_date')[:5]
# 	template = loader.get_template('Polls/index.html')
# 	context = {	
# 		'latest_question_list': latest_question_list,
# 	}
# 	return HttpResponse(template.render(context, request))
# def detail(request, question_id):
# 	try:
# 		question = Question.objects.get(pk=question_id)
# 	except Question.DoesNotExist:
# 		raise Http404("Question does not exist")
# 	return render(request, 'Polls/detail.html', {'question': question})

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)