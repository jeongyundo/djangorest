from django.urls import path

from informationEvent import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view())
    #views의 helloapiview함수의 리스폰스를 url로 보여주는 설정
]