from django.urls import path
from . import views

urlpatterns = [

    path("pages/", views.case_list, name="case_list"),

    path("pages/<int:case_id>/", views.case_detail, name="case_detail"),

    path("pages/create/", views.CaseCreateView.as_view(), name="case_create"),

    path("pages/<int:pk>/update/", views.CaseUpdateView.as_view(), name="case_update"),

    path("pages/<int:pk>/delete/", views.CaseDeleteView.as_view(), name="case_delete"),

]