from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Message
from .forms import MessageForm


@login_required
def inbox(request):

    messages = Message.objects.filter(
        Q(sender=request.user) | Q(receiver=request.user)
    ).order_by("-created_at")

    conversations = {}

    for message in messages:

        if message.sender == request.user:
            other_user = message.receiver
        else:
            other_user = message.sender

        if other_user.id not in conversations:

            unread = Message.objects.filter(
                sender=other_user,
                receiver=request.user,
                read=False
            ).exists()

            conversations[other_user.id] = {
                "user": other_user,
                "last_message": message,
                "unread": unread
            }

    return render(request, "messaging/inbox.html", {
        "conversations": conversations.values()
    })


@login_required
def chat(request, user_id):

    other_user = get_object_or_404(User, id=user_id)

    messages = Message.objects.filter(
        Q(sender=request.user, receiver=other_user) |
        Q(sender=other_user, receiver=request.user)
    ).order_by("created_at")

    # marcar mensajes como leídos
    Message.objects.filter(
        sender=other_user,
        receiver=request.user,
        read=False
    ).update(read=True)

    if request.method == "POST":

        content = request.POST.get("content")

        if content:
            Message.objects.create(
                sender=request.user,
                receiver=other_user,
                content=content
            )

        return redirect("chat", user_id=other_user.id)

    return render(request, "messaging/chat.html", {
        "messages": messages,
        "other_user": other_user
    })


@login_required
def send_message(request):

    if request.method == "POST":

        form = MessageForm(request.POST)

        if form.is_valid():

            message = form.save(commit=False)
            message.sender = request.user
            message.save()

            return redirect("inbox")

    else:
        form = MessageForm()

    return render(request, "messaging/enviar.html", {
        "form": form
    })


@login_required
def new_chat(request):

    users = User.objects.exclude(id=request.user.id)

    return render(request, "messaging/new_chat.html", {
        "users": users
    })