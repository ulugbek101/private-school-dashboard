from django.urls import path, include
from django.contrib.auth.views import LogoutView

from . import views


urlpatterns = [
    path('', views.index),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', LogoutView.as_view()),

    path('social-auth/', include('social_django.urls', namespace='social')),
]
