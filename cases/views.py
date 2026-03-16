from django.shortcuts import render, get_object_or_404, redirect
from .models import Case
from comments.models import Comment

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


def case_list(request):

    cases = Case.objects.all()

    query = request.GET.get("q")
    case_type = request.GET.get("type")

    if query:
        cases = cases.filter(title__icontains=query)

    if case_type:
        cases = cases.filter(case_type=case_type)

    context = {
        "cases": cases,
        "query": query,
        "selected_type": case_type
    }

    return render(request, "cases/case_list.html", context)


def case_detail(request, case_id):

    case = get_object_or_404(Case, id=case_id)
    comments = Comment.objects.filter(case=case)

    if request.method == "POST":

        text = request.POST.get("text")

        Comment.objects.create(
            case=case,
            user=request.user,
            text=text
        )

        return redirect('case_detail', case_id=case.id)

    return render(request, 'cases/case_detail.html', {
        'case': case,
        'comments': comments
    })


# LISTAR CASOS
class CaseListView(ListView):
    model = Case
    template_name = "cases/case_list.html"
    context_object_name = "cases"


# CREAR CASO
class CaseCreateView(LoginRequiredMixin, CreateView):
    model = Case
    fields = ["title", "description", "image", "case_type", "event_date"]
    template_name = "cases/case_form.html"
    success_url = reverse_lazy("case_list")


# EDITAR CASO
class CaseUpdateView(LoginRequiredMixin, UpdateView):
    model = Case
    fields = ["title", "description", "image", "case_type", "event_date"]
    template_name = "cases/case_form.html"
    success_url = reverse_lazy("case_list")


# BORRAR CASO
class CaseDeleteView(LoginRequiredMixin, DeleteView):
    model = Case
    template_name = "cases/case_confirm_delete.html"
    success_url = reverse_lazy("case_list")