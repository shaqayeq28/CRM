from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from user.forms import SignUpForm
from user.models import UserProfile


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            user_profile = UserProfile.objects.get_or_create(user=user)

            return redirect('/log-in/')

    else:
        form = SignUpForm()

    return render(request, 'user/signup.html', context={'form': form})


@login_required
def dashboard(request):
    return render(request, 'user/dashboard.html')
