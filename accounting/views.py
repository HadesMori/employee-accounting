from django.http import HttpResponse, HttpResponseRedirect # type: ignore
from django.shortcuts import get_object_or_404 # type: ignore
from django.urls import reverse # type: ignore
from django.views.generic import ListView, TemplateView, UpdateView, View, DetailView # type: ignore
from .models import *
from .forms import *

class MainView(ListView):
    template_name = "index.html"
    model = Employee
    context_object_name = "employees"

    def get_queryset(self):
        queryset = super().get_queryset()
        sort_by = self.request.GET.get('sort_by')
        if sort_by:
            if sort_by == 'last_name':
                queryset = queryset.order_by('last_name')
            elif sort_by == 'first_name':
                queryset = queryset.order_by('first_name')
            elif sort_by == 'salary':
                queryset = queryset.order_by('salary')
            elif sort_by == 'position':
                queryset = queryset.order_by('position')
        return queryset

class AddEmployeeView(TemplateView):
    template_name = "add-employee.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        form = EmployeeForm()
        context['form'] = form
        return context
    
    def post(self, request):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.save()
            return HttpResponseRedirect(reverse("add-employee-page"))
        
class UpdateView(UpdateView):
    template_name = "update-employee.html"
    model = Employee

    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    fields = [ 
        "first_name", 
        "last_name",
        "position",
        "salary",
    ] 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        form = EmployeeForm()
        context['form'] = form
        return context
        
    def post(self, request, slug):
        # Retrieve the existing employee object based on the slug
        employee = get_object_or_404(Employee, slug=slug)
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()  # This will update the existing object with the form data
            return HttpResponseRedirect(reverse("add-employee-page"))

class DeleteEmployeeView(View):
    def post(self, request, slug):
        # Retrieve the existing employee object based on the slug
        employee = get_object_or_404(Employee, slug=slug)
        employee.delete()  # Видалення працівника з бази даних
        return HttpResponseRedirect(reverse("main-page"))
    
class EmployeeView(DetailView):
    template_name = "employee.html"
    model = Employee
    context_object_name = "employee"