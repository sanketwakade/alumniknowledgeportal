from django.shortcuts import render
from django.shortcuts import render, redirect
from BaseApp.models import Knowledge
from BaseApp.forms import KnowledgeForm

# Create your views here.
def homeview(request):
    return render(request, 'index.html')

def aboutview(request):
    return render(request, 'about.html')

def knowledgeview(request):
    knowledge_list = Knowledge.objects.all()
    return render(request, 'knowledge.html', {'knowledge_list': knowledge_list})

def contactview(request):
    return render(request, 'contact.html')

def joinview(request):
    return render(request, 'join.html')

def loginview(request):
    return render(request, 'login.html')


from BaseApp.forms import KnowledgeForm
from BaseApp.models import Knowledge
from django.shortcuts import render, redirect

def knowledge_view(request):
    if request.method == 'POST':
        form = KnowledgeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('knowledge')  # Replace with your URL name
    else:
        form = KnowledgeForm()

    entries = Knowledge.objects.all()
    return render(request, 'knowledge.html', {'form': form, 'entries': entries})

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from BaseApp.forms import RegisterForm, LoginForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # change this if needed
    else:
        form = RegisterForm()
    return render(request, 'join.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')
