from django.shortcuts import render

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        userRole = request.user.usertype.role
        return render(request, 'home.html', {'role': userRole})
    if not request.user.is_authenticated:
        return render(request, 'home.html', {'role': 'guest'})
    
    
    

