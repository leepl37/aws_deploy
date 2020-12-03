from django.urls import path, include
from profile_api import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HellowViewSet,
                basename="hello-viewset"),
router.register('profile',views.UserProfileViewSet)
#queryset 있으면 basename은 필요없음. 
router.register('feed',views.UserProfileFeedViewSet)
urlpatterns = [

    path('hello-view/', views.ApiView.as_view()),
    path('login/',views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
