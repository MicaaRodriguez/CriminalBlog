from django.contrib import admin
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import Case


class CaseAdminForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = "__all__"
        widgets = {
            "event_date": AdminDateWidget()
        }


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    form = CaseAdminForm
    date_hierarchy = "event_date"
    list_display = ("title", "case_type", "event_date", "created_at")
    list_filter = ("case_type", "event_date")
    search_fields = ("title", "description")