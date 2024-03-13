from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from users.forms import LoginForm, SignupForm

def login_view (request):
    if request.user.is_authenticated:
        return redirect("/blog/")

    if request.method == "POST" :
        form = LoginForm(data=request.POST)

        if form.is_valid() :
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)

            if user:
                
                login(request,user)
                return redirect("/blog")
            else:
                form.add_error(None, "아이디 및 비밀번호가 틀렸습니다. 다시 시도 해주세요")

        context = {"form" : form}
        return render(request, "users/login.html", context)
    else :
        form = LoginForm()
        context = {"form" : form}
        return render(request, "users/login.html", context)
    
def logout_view(request):
    logout(request)

    return redirect("/users/login")

def register(request):
    if request.method == "POST" :
        form = SignupForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("main")
    else :
        form = SignupForm()
    
    context = {"form" : form}
    return render(request, "users/register.html", context)
