import requests
from django.shortcuts import render, redirect
from .models import User, States


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        # Check if email already exists
        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': 'Email already exists'})
        else:
            # Create user
            user = User.objects.create(username=username, email=email, password=password)
            # You might want to add additional logic like sending a verification email
            return redirect('signup')  # Redirect to login page after successful signup
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Check if user with given credentials exists
        if User.objects.filter(username=username, password=password).exists():
            # Authentication successful, redirect to dashboard or home page
            return redirect('home')  # Change 'dashboard' to the appropriate URL name
        else:
            # Authentication failed, render login page with error message
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')


def Home(request):
    try:
        # Fetch COVID-19 data for India from the API
        response = requests.get('https://api.covid19india.org/data.json')
        data = response.json()

        # Extracting data for India
        india_data = data['statewise'][0]

        # Extract relevant statistics
        total_cases = india_data['confirmed']
        active_cases = india_data['active']
        recovered = india_data['recovered']
        deaths = india_data['deaths']

        context = {
            'total_cases': total_cases,
            'active_cases': active_cases,
            'recovered': recovered,
            'deaths': deaths
        }
    except Exception as e:
        # Handle any errors that occur during fetching or processing data
        context = {
            'error_message': f"Error fetching data: {str(e)}"
        }

    return render(request, 'home.html', context)


def state_data(request):
    # Retrieve all States objects from the database
    states_data = States.objects.all()

    # Pass the retrieved data to the template
    return render(request, 'viewStates.html', {'states_data': states_data})


def About(request):
    return render(request, "about.html")