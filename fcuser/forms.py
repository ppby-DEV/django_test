from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password


class LoginForm(forms.Form):
    username = forms.CharField(error_messages={
        'required': '아이디를 입력하세요.'},
        max_length=32, label="사용자 이름")
    password = forms.CharField(error_messages={
        'required': '비밀번호를 입력하세요.'
    }, widget=forms.PasswordInput, label="비밀번호")

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                fcuser = Fcuser.objects.get(username=username)
            except Fcuser.DoesNotExist:
                self.add_error('username', '등록되지 않은 사용자입니다.')
                return
                # 메세지만 출력하고 리턴해서 나옴 밑에는 확인하지 않음
            if not check_password(password, fcuser.password):
                self.add_error('password', '비밀번호가 틀렸습니다.')
            else:
                self.user_id = fcuser.id
