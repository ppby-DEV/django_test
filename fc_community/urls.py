"""fc_community URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from fcuser.views import home

urlpatterns = [
    path('admin/', admin.site.urls),  # ==>admin에 사용되는 애는 admin에 있는 url만 사용하겠다.
    path('fcuser/', include('fcuser.urls')),
    # ==>fcuser아래로 오는 모든 url들은 fcuser 안에 있는 url에서 관리 함
    path('board/', include('board.urls')),
    path('', home),
]


# admin 안에 여러가기 url들이 정의되어 있고 (관리자 페이지에서도 사용하는
# url들이 정의가 되어 있음) --> 프로젝트에서 admin하위로 지정
# 즉, path('admin/', admin.site.urls) --> 어드민 하위에 있는 것들은 다
# admin.site.urls 여기로 연결하겠다
# 주소 뒤에다 admin을 붙히면 장고 관리자 도구를 사용할 수 있다.
# 장고에서 기본적으로 제공
