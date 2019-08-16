from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from accounts.models import Profile

# Create your views here.
def login_user(request):
    if request.user.is_authenticated:
        return redirect("index")

    context = {'success':False, 'error':False, 'message':''}
    if request.method == 'POST':
        username = request.POST.get("username","")
        password = request.POST.get("password","")
        telephone= request.POST.get("telephone")
        if len(username) > 0 and len(password) > 0 :
            print(username, password)
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active :
                login(request, user)
                return redirect("index")
            else:
                context['error'] = True
                context['message'] = "nom d'utilisateur ou mot de passe incorrect"   
        else:
            context['error'] = True
            context['message'] = "Vous devrez remplir tous les champs."
    print(context)
    return render(request, "registration/login.html", context)

def register_user(request):
    if request.user.is_authenticated:
        return redirect("index")
        
    context = {'success':False, 'error':False, 'message':''}
    if request.method == 'POST':

        username = request.POST.get("username","")
        password = request.POST.get("password","")
        confirmation = request.POST.get("confirmation","")

        if len(username) > 0 and len(password) > 0 and len(confirmation) > 0 :

            if str(password) == str(confirmation) :
                if not User.objects.filter(username=username).exists():
                    new_user = User.objects.create_user(username=username, password=password)
                    new_user.is_active = True
                    new_user.save()
                    new_profile = Profile()
                    new_profile.user = new_user
                    new_profile.save()
                    context['success'] = True
                    context['message'] = "Votre compte a ete creer avec succes."
                else:
                    context['error'] = True
                    context['message'] = "Ce nom d'utilisteur existe deja."
            else:
                context['error'] = True
                context['message'] = "Vos deux mots de passe ne correspondent pas."
        else:
            context['error'] = True
            context['message'] = "Vous devrez remplir tous les champs."

    return render(request, "registration/registration.html", context)

def logout_user(request):
    logout(request)
    return redirect("index")