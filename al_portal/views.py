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
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('knowledge')  # Replace with your URL name
    else:
        form = KnowledgeForm()

    entries = Knowledge.objects.all()
    return render(request, 'knowledge.html', {'form': form, 'entries': entries})

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from BaseApp.models import UserProfile
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

def register(request):
    if request.method == 'POST':
        # Collect form data
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        graduation_year = request.POST.get('graduation-year')
        profession = request.POST.get('profession')

        # Basic Validation
        if not first_name or not last_name or not email or not password:
            # Add an error message
            return render(request, 'join.html', {'error': 'All fields are required.'})

        try:
            validate_email(email)
        except ValidationError:
            return render(request, 'join.html', {'error': 'Invalid email address.'})

        # Ensure the email is unique
        if User.objects.filter(email=email).exists():
            return render(request, 'join.html', {'error': 'Email already registered.'})

        # Create the user
        user = User.objects.create(
            username=email,  # or use a separate username field
            first_name=first_name,
            last_name=last_name,
            email=email
        )

        # Set the password
        user.set_password(password)
        user.save()  # Save the user after setting the password

        # Create associated profile
        UserProfile.objects.create(
            user=user,
            graduation_year=graduation_year,
            profession=profession
        )

        # Log the user in
        login(request, user)

        # Redirect after successful registration
        return redirect('home')  # or your desired page

    return render(request, 'join.html')




from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from BaseApp.models import UserProfile
from django.contrib.auth.models import User

def login_view(request):
    print("Login view called")  # Debug

    if request.method == 'POST':
        print("POST request received")  # Debug
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"Username: {username}, Password: {password}")  # Debug

        user = authenticate(request, username=username, password=password)
        print(f"User authenticated: {user}")  # Debug

        if user is not None:
            login(request, user)
            print("User logged in successfully")  # Debug

            # Optional: check if UserProfile exists
            try:
                profile = UserProfile.objects.get(user=user)
                print(f"UserProfile found: {profile.profession}, {profile.graduation_year}")
            except UserProfile.DoesNotExist:
                print("UserProfile not found.")

            return redirect('home')
        else:
            print("Invalid credentials")  # Debug
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'login.html')
