from django.shortcuts import render
from .forms import SignupForm


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
    pass


def logout_view(request):
    # ユーザーのログアウト
    pass


def user_view(request):
    # ユーザーの情報を表示
    pass


def other_view(request):
    # 他のユーザーの情報を表示
    pass
