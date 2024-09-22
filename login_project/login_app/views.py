from django.shortcuts import redirect, render
from .forms import SignupForm, LoginForm
from django.contrib.auth import login, logout


def signup_view(request):
    # ユーザーアカウントの登録
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SignupForm()
    param = {"form": form}
    return render(request, "login_app/signup.html", param)


def login_view(request):
    # ユーザーのログイン
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                return redirect(to="/login_app/")
    else:
        form = LoginForm()
    param = {"form": form}
    return render(request, "login_app/login.html", param)


def logout_view(request):
    # ユーザーのログアウト
    logout(request)
    return render(request, "login_app/logout.html")


def user_view(request):
    # ユーザーの情報を表示
    pass


def other_view(request):
    # 他のユーザーの情報を表示
    pass
