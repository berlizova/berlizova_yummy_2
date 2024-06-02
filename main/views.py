from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import DishCategory, Gallery, Staff, Events, Contacts
from .forms import ReservationForm
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = DishCategory.objects.filter(is_visible=True)
        gallery = Gallery.objects.all()
        staff = Staff.objects.filter(is_visible=True)
        events = Events.objects.all()
        contact = Contacts.objects.first()
        form = ReservationForm()

        context['title_menu'] = 'Check Our <span>Yummy Menu</span>'
        context['title_gallery'] = 'Check <span>Our Gallery</span>'
        context['title_events'] = 'Share <span>Your Moments</span> In Our Restaurant'
        context['title_chefs'] = 'Our <span>Professional</span> Chefs'
        context['title_contacts'] = 'Need Help? <span>Contact Us</span>'
        context['title_contacts_address'] = 'Our Address'
        context['title_contact_email'] = 'Email'
        context['title_contact_phone'] = 'Call Us'
        context['title_contact_time'] = 'Opening Hours'
        context['categories'] = categories
        context['gallery'] = gallery
        context['chefs'] = staff
        context['events'] = events
        context['contact'] = contact
        context['form'] = form

        return context

    def post(self, request, *args, **kwargs):
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your reservation successful')
            return redirect('/')  # Redirect to home page
        else:
            return self.get(request, *args, **kwargs)


def manager(request):
    # Your manager view logic here
    pass