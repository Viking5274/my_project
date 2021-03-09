from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect

from .forms import UserForm, EditForm
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
    form_class = EditForm
    #queryset = PhoneBook.objects.all()

    """def get_object(self, queryset = PhoneBook.objects.all()):
        id_ = self.kwargs.get('pk')
        print("MY ID")
        print(id_)
        return get_object_or_404(PhoneBook, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)"""


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
