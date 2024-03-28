from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,ListView,DetailView,DeleteView,TemplateView
from services.models import Client, Message, Newsletter, Contact
from services.forms import ClientForm, MessageForm, NewsletterForm


class Homepage(TemplateView):
    template_name = 'services/base.html'
    extra_context = {'title':'SkyService'}

class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('services:client_list')

class ClientUpdateView(UpdateView):
    model = Client
    fields = ('fio', 'email', 'comment',)
    success_url = reverse_lazy('services:client_list')



class ClientListView(ListView):
    model = Client

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args,**kwargs)
        context_data ['clients_list'] = Client.objects.all()
        return context_data

class ClientDetailView(DetailView):
    model = Client

class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('services:client_list')

class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('services:list_message')

class MessageUpdateView(UpdateView):
    model = Message
    fields = ('subject', 'body',)
    success_url = reverse_lazy('services:list_message')

class MessageListView(ListView):
    model = Message

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['message_list'] = Message.objects.all()
        return context_data

class MessageDetailView(DetailView):
    model = Message

class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('services:list_message')


class NewsletterCreateView(CreateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('services:list_newsletter')

class NewsletterUpdateView(UpdateView):
    model = Newsletter
    fields = ('start_time', 'end_time', 'periodicity', 'status', 'client', 'message')
    success_url = reverse_lazy('services:list_newsletter')



class NewsletterListView(ListView):
    model = Newsletter

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['newsletter_list'] = Newsletter.objects.all()
        return context_data


class NewsletterDetailView(DetailView):
    model = Newsletter


class NewsletterDeleteView(DeleteView):
    model = Newsletter
    success_url = reverse_lazy('services:list_newsletter')

class ContactTemplateView(TemplateView):
    template_name = 'services/contacts.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        contact_info = Contact.objects.all()
        context_data['contact_book'] = contact_info
        return context_data

    def post(self,request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя:{name} , номер телефона:{phone} , сообщение: {message}')
        return render(request,self.template_name)
