from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Schedule, Child
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user_type = request.POST['user_type']

        if User.objects.filter(username=username).exists():
            messages.error(request, "User already exists.")
            return redirect('signup')

        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, "Account created successfully!")

        return redirect('login')  # redirect to login after signup
    return render(request, 'signup.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.POST.get('user_type') == "parent":
                return redirect('child_form')  # Redirect to child details form
            else:
                return redirect('home')  # Teachers go to home directly (you can customize)
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')
    return render(request, 'login.html')

@login_required
def child_form(request):
    if request.method == "POST":
        name = request.POST['child_name']
        age = request.POST['age']
        grade = request.POST['grade']
        Child.objects.create(parent=request.user, child_name=name, age=age, grade=grade)
        return redirect('schedule')  # After child form, go to schedule
    return render(request, 'child_form.html')



@login_required
def schedule(request):
    child = Child.objects.filter(parent=request.user).last()  # latest child added
    if request.method == "POST":
        day = request.POST['day']
        activity = request.POST['activity']
        time = request.POST['time']
        Schedule.objects.create(child=child, day=day, activity=activity, time=time)
        return redirect('home')  # After schedule, go to home page
    return render(request, 'schedule.html')

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def grades(request):
    return render(request, 'grades.html')

def prekg(request):
    return render(request, 'grades/prekg.html')


def lkg(request):
    return render(request, 'grades/lkg.html')

def ukg(request):
    return render(request, 'grades/ukg.html')

def grade1(request):
    return render(request, 'grades/grade1.html')

def grade2(request):
    return render(request, 'grades/grade2.html')

def grade3(request):
    return render(request, 'grades/grade3.html')

def quiz(request):
    return render(request, 'activities/quiz.html')



def games(request):
    return render(request, 'activities/games.html')

def quiz_grades(request):
    return render(request, 'activities/quiz_grades.html')

def quiz_prekg(request):
    return render(request, 'activities/quiz/prekg.html')

def quiz_lkg(request):
    return render(request, 'activities/quiz/lkg.html')

def quiz_ukg(request):
    return render(request, 'activities/quiz/ukg.html')

def quiz_1(request):
    return render(request, 'activities/quiz/1.html')

def quiz_2(request):
    return render(request, 'activities/quiz/2.html')

def quiz_3(request):
    return render(request, 'activities/quiz/3.html')

def puzzle(request):
    return render(request, 'activities/puzzle.html')

def games_view(request):
    return render(request, 'activities/games.html')

def memory_game(request):
    return render(request, 'games/memory_game.html')


def math_puzzle(request):
    return render(request, 'games/math_puzzle.html')

def spelling_bee(request):
    return render(request, 'games/spelling_bee.html')

def guess_image(request):
    return render(request, 'games/guess_image.html')

def color_match(request):
    return render(request, 'games/color_match.html')

def shape_sort(request):
    return render(request, 'games/shape_sort.html')

def prekg_rhymes(request):
    return render(request, 'grades/prekg.html')