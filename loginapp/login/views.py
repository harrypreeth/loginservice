from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StandardUserLoginForm
from .functions import authenticate, find_user

def user_login(request):
    # Redirect to dashboard if session exists
    if request.session.get("user") is not None:
        return redirect('dashboard')
    
    # Instantiate login form
    form = StandardUserLoginForm()
    context = {'form': form}

    # Process user login form
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authenticate user
        user = authenticate(username, password)

        # User authentication successful
        if user is not None:
            request.session["user"] = user
            return redirect('dashboard')

        # User authentication failed
        else:
            messages.info(request, "Username/Password is incorrect!")
            return render(request, "userlogin.html", context)

    # Display login form on GET request
    return render(request, "userlogin.html", context)

def user_logout(request):
    # Flush session on user logout
    request.session.flush()
    return redirect('login')

def user_dashboard(request):
    # Redirect to login if session doesn't exist
    if request.session.get("user") is None:
        return redirect('login')
    
    user = request.session.get("user")
    context = {'user': user}

    # Process find user form
    if request.method == "POST":
        find_username = request.POST.get("findUser")
        found_user = find_user(find_username)

        # Render if user is found
        if found_user is not None:
            context.update({"found_user": found_user})
            return render(request, 'userdashboard.html', context)
    
    return render(request, 'userdashboard.html', context)
