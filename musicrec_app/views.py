from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from musicrec_app.rec import get_recommendations  
from django.views.decorators.csrf import csrf_exempt

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            messages.success(request, "Registration successful! You are now logged in.")
            return redirect("home")  
        else:
            messages.error(request, "Registration failed. Please fix the errors below.")  

    else:
        form = UserCreationForm()
    
    return render(request, "musicrec_app/reg.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")  
        else:
            messages.error(request, "Invalid username or password.")  

    return render(request, "musicrec_app/login.html")

def logout_view(request):
    logout(request)  
    return redirect("login")  

def home_view(request):
    return render(request, 'musicrec_app/home.html')

def recommend_view(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query', '').strip()
        
        if not search_query:
            return render(request, 'musicrec_app/recommendations.html', {'error': "Please enter a valid search term."})
          
        recommendations = get_recommendations(search_query)

        return render(request, 'musicrec_app/recommendations.html', {
            'recommendations': recommendations if recommendations else [],
            'error': "No recommendations found. Try a different song." if not recommendations else None
        })
    
    return render(request, 'musicrec_app/recommendations.html') 
