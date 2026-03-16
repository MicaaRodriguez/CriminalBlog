from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import CustomLoginForm

urlpatterns = [

    path("register/", views.register, name="register"),

    path("profile/", views.profile, name="profile"),

    path("about/", views.about, name="about"),

    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html",
            authentication_form=CustomLoginForm
        ),
        name="login"
    ),

    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    path("perfil/editar/", views.edit_profile, name="edit_profile"),

    path(
        "password_change/",
        auth_views.PasswordChangeView.as_view(
            template_name="registration/password_change.html"
        ),
        name="password_change"
    ),

    path(
        "password_change_done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="registration/password_change_done.html"
        ),
        name="password_change_done"
    ),

    path("user/<int:user_id>/", views.user_profile, name="user_profile"),

]