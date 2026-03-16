from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, EditProfileForm, ProfileForm
from .models import Profile


def register(request):

    if request.method == "POST":

        form = CustomUserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            birthday = form.cleaned_data.get("birthday")

            user.profile.birthday = birthday
            user.profile.save()

            login(request, user)

            return redirect("profile")

    else:

        form = CustomUserCreationForm()

    return render(request, "registration/register.html", {"form": form})


@login_required
def profile(request):

    return render(request, "accounts/profile.html")


@login_required
def edit_profile(request):

    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":

        user_form = EditProfileForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("profile")

    else:
        user_form = EditProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)

    return render(request, "accounts/edit_profile.html", {
        "user_form": user_form,
        "profile_form": profile_form
    })


def about(request):

    return render(request, "about.html")


def user_profile(request, user_id):

    user = User.objects.get(id=user_id)

    return render(request, "accounts/user_profile.html", {
        "profile_user": user
    })