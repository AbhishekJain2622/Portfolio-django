from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='home'),
   # path('about/',views.About,name='about'),
    path('service/',views.service,name='service'),
    path('project/',views.projects,name='project'),
    path('contact/',views.mcontact,name='contact')

    #path('signup/',views.signup,name='signup'),
    #path('login/',views.handleLogin,name='handleLogin'),
    #path('logout/',views.handleLogout,name='handleLogout'),
]
