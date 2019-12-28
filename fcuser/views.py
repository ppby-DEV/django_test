from django.shortcuts import render, redirect
from .models import Fcuser
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from .forms import LoginForm
# Create your views here.


def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':  # 포스트일 때 포스트가 아닐 때
        form = LoginForm(request.POST)  # 폼 클래스변수를 만들 때 포스트 데이터를 넣어줌
        if form.is_valid():
            request.session['user'] = form.user_id
            # 정상적이면 session 코드가 들어가고 redirect함
            return redirect('/')
    else:
        form = LoginForm()  # 그냥 빈 클래스 변수를 만듬
    return render(request, 'login.html', {'form': form})


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')


def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    elif request.method == "POST":
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}

        if not (username and useremail and password and re_password):
            res_data['error'] = '모든 값을 입력해야합니다!'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다!'
        else:
            fcuser = Fcuser(
                username=username,
                useremail=useremail,
                password=make_password(password)
            )
            fcuser.save()

        return render(request, "register.html", res_data)
        # 가입 정보 등록후 다시 register.html로 반환(다른 화면으로 넘기면 굿)
