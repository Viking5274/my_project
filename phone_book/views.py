from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import UserForm
from .models import PhoneBook


class HomeView(ListView):
    model = PhoneBook
    template_name = 'phone_book/home.html'
    ordering = ['name']


class UserDetail(DetailView):
    model = PhoneBook
    template_name = 'phone_book/details.html'


class AddUser(CreateView):
    model = PhoneBook
    template_name = 'phone_book/add_user.html'
    form_class = UserForm


class UpdateUser(UpdateView):
    model = PhoneBook
    template_name = 'phone_book/update_user.html'
    form_class = UserForm


class DeleteUser(DeleteView):
    model = PhoneBook
    template_name = 'phone_book/delete_user.html'
    success_url = reverse_lazy('home')


class SearchResultsView(ListView):
    model = PhoneBook
    template_name = 'phone_book/search_result.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = PhoneBook.objects.filter(
            Q(name__icontains=query) | Q(surname__icontains=query) | Q(phone__icontains=query)
        )
        return object_list
