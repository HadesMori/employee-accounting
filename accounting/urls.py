from django.urls import path #type: ignore
from .views import *

urlpatterns = [
    path("", MainView.as_view(), name="main-page"),
    path("add", AddEmployeeView.as_view(), name="add-employee-page"),
    path("update\<slug:slug>", UpdateView.as_view(), name="update-employee-page"),
    path("delete\<slug:slug>", DeleteEmployeeView.as_view(), name="delete-employee"),
    path("employee\<slug:slug>", EmployeeView.as_view(), name="employee-page"),
]