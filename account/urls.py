from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm

app_name = 'account'
urlpatterns = [
    path ('login/', auth_views.LoginView.as_view(template_name='account/registration/login.html', form_class=UserLoginForm), name='login'),
    path('register/', views.register_useraccount, name='register'),
    path('activate/<slug:uidb64>/<slug:token>', views.activate_account, name='activate'),
    path('dashboard/', views.dashboard, name='dashboard')

]
