from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Cars_new, User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

class CarInt(ListView):
    model=Cars_new
    template_name = "base.html"
    context_object_name = 'Cars'

class CreateView(CreateView):
    model = Cars_new
    template_name = "create.html"
    fields=['name_car', 'motor_car', 'firma_car', 'image_car', 'price']

class NewCar(DeleteView):
    model=Cars_new
    template_name = "newcar.html"
    context_object_name = 'Cars'

class EditCar(UpdateView):
    model = Cars_new
    template_name = "editcar.html"
    fields = ['name_car', 'motor_car', 'firma_car', 'image_car', 'price']

class DeleteCar(DeleteView):
    model = Cars_new
    template_name = "delete.html"
    success_url = reverse_lazy('base')
    context_object_name = 'car'  # Obyektni 'car' deb nomlaymiz

class CreateUser(CreateView):
    model = User
    template_name = 'user_form.html'
    fields = ['name', 'surname', 'age', 'phone']
    # success_url = reverse_lazy('base')



