from django.urls import path, include

from rest_framework.routers import DefaultRouter

from informationEvent import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    #views의 helloapiview함수의 리스폰스를 url로 보여주는 설정
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]