from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view),

    path('social-auth/', include('social_django.urls', namespace='social')),
]
