from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_str, force_bytes
from django.utils.http import  urlsafe_base64_encode, urlsafe_base64_decode
from .forms import RegistrationForm
from .models import UserBase
from .token import account_activation_token
from account import token
from order.views import user_orders
# Create your views here.


@login_required
def dashboard(request):
    order = user_orders(request)
    return render(request, 'account/user/dashboard.html', { 'order': order})


def register_useraccount(request):
    if request.user.is_authenticated:
        return redirect('account:dashboard')

    if request.method=='POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            subject = 'Active your useraccount.'
            message = render_to_string('account/registration/account_activation_email.html',{
                'user':user,
                'domin':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
                })
            user.email_user(subject=subject, message=message)
            return HttpResponse('Successfully registered and sent the activation')
    else:
        registerForm = RegistrationForm()
    return render(request, 'account/registration/register.html', {'forms':registerForm})

def activate_account(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserBase.objects.get(pk=uid)
    except:
        pass
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('account:dashboard')
    else:
        return render(request, 'account/registration/activation_invalid.html')
    