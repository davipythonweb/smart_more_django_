from phones.models import Phone
from phones.forms import PhoneModelForm

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



class PhonesListView(ListView):
    model = Phone
    template_name = 'phones.html'
    context_object_name = 'phones'
    
    def get_queryset(self):
        phones = super().get_queryset().order_by('title')
        search = self.request.GET.get('search')
        if search:
            phones = phones.filter(title__icontains=search)
        return phones
    
class PhoneDetailView(DetailView):
    model = Phone
    template_name = 'detail_phone.html'
    
@method_decorator(login_required(login_url='namespace_2:login'), name='dispatch')    
class NewPhoneCreateView(CreateView):
    model = Phone
    form_class = PhoneModelForm
    template_name = 'new_phone.html'
    success_url = '/'
    
@method_decorator(login_required(login_url='namespace_2:login'), name='dispatch')        
class PhoneUpdateView(UpdateView):
    model = Phone
    form_class = PhoneModelForm
    template_name = 'update_phone.html'
    
    def get_success_url(self):
        return reverse_lazy('phone_detail', kwargs={'pk': self.object.pk})
    

@method_decorator(login_required(login_url='namespace_2:login'), name='dispatch')    
class PhoneDeleteView(DeleteView):
    model = Phone
    template_name = 'delete_phone.html'
    success_url = '/'