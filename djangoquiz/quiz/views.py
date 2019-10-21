from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.db.models import Q
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm

# from django.core.urlresolvers import reverse
# Create your views here.
@login_required(login_url='/register/')
def home(request):

	return render(request, 'quiz/home.html')


def about(request):
	
	return render(request, 'quiz/about.html', {'title': 'About'})


def about1(request):
	obj =  Stat.objects.all()
	return render(request, 'quiz/about1.html',{'obj':obj})


def register(request):

	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			username=form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!')
			form.save()
			return redirect('quiz-register')
	else:
		form  = SignUpForm()
	return render(request, 'quiz/register.html', {'form': form})

@login_required(login_url='/register/')
def math_view(request):
	if request.method == 'GET':
		math_quiz_questions = Math.objects.all().order_by('?')
		return render(request, 'quiz/math.html', {"quizz": math_quiz_questions})

	if request.method == 'POST':
		form_data = request.POST.dict()
		user = request.user
		question_keys = filter(lambda ques: ques.isdigit(), list(form_data.keys()))
		for question_no in question_keys:
			
			if "ch_" in form_data.get(question_no):

				math_obj = Math.objects.get(si_no=question_no)
				math_quiz_ans_obj = MathQuizAnswer()
				math_quiz_ans_obj.user = user
				math_quiz_ans_obj.mat_quiz = math_obj
				math_quiz_ans_obj.answer = form_data.get(question_no)
				math_quiz_ans_obj.save()

		return redirect('quiz-math_view')


@login_required(login_url='/register/')
def stat_view(request):
	if request.method == 'GET':
		stat_quiz_questions = Stat.objects.exclude(
			_id__in=list(StatQuizAnswer.objects.values_list('stat_quiz', flat=True))
		)[:10]
		return render(request, 'quiz/stat.html', {"quizz": stat_quiz_questions})

	if request.method == 'POST':
		form_data = request.POST.dict()
		user = request.user
		question_keys = filter(lambda ques: ques.isdigit(), list(form_data.keys()))
		for question_no in question_keys:
			
			if "ch_" in form_data.get(question_no):

				stat_obj = Stat.objects.get(si_no=question_no)
				stat_quiz_ans_obj = StatQuizAnswer()
				stat_quiz_ans_obj.user = user
				stat_quiz_ans_obj.stat_quiz = stat_obj
				stat_quiz_ans_obj.answer = form_data.get(question_no)
				stat_quiz_ans_obj.save()

		return redirect('quiz-stat_view')