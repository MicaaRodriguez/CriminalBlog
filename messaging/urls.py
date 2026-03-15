from django.urls import path
from . import views

urlpatterns = [

    path("inbox/", views.inbox, name="inbox"),

    path("chat/<int:user_id>/", views.chat, name="chat"),

    path("new/", views.new_chat, name="new_chat"),

]