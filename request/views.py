from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from .models import Request
from .forms import NewRequestForm

# Create your views here.
def dashboard(request):
    return render(request, 'request/dashboard.html')



class CreateRequest(LoginRequiredMixin, CreateView):
    model = Request
    fields = ['content', 'assign_to']
    # return redirect ('outgoing')
    def get_success_url(self):
        return reverse('outgoing')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.author_dept = self.request.user.profile.department
        form.instance.editor = self.request.user
        return super().form_valid(form)

class RequestDetail(LoginRequiredMixin, DetailView):
    model = Request
    fields = ['content', 'author_group', 'assign_to', 'ref_code']
    template_name = 'request/request_detail.html'

class RequestUpdateView(LoginRequiredMixin,UpdateView):
    model = Request
    fields = ['status', 'content']


class RequestStatusUpdateView(LoginRequiredMixin,UpdateView):
    model = Request
    fields = ['status']

    def form_valid(self, form):
        form.instance.editor = self.request.user
        form.instance.time_edited = timezone.now()
        return super().form_valid(form)



class RequestDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Request

    def get_success_url(self):
        return reverse('dashboard')

    def test_func(self):
        request = self.get_object()
        if self.request.user == request.author:
            return True
        return False


#OUTGOING Requests
#Pending
@login_required
def out_requests(request):
    context = {
    'outgoing': Request.objects.filter(author_dept=request.user.profile.department).order_by('-date_posted').filter(status='Pending')
    }
    return render(request, 'request/outgoing.html', context)

#Progress
@login_required
def out_requests_in_progress(request):
    context = {
    'out_in_progress': Request.objects.filter(author_dept=request.user.profile.department).filter(status='Progress')
    }
    return render(request, 'request/outprogress.html', context)

#Completed Requests
@login_required
def out_complete(request):
    context = {
    'out_complete': Request.objects.filter(author_dept=request.user.profile.department).filter(status='Complete')
    }
    return render(request, 'request/complete.html', context)

#INCOMING REQUESTS
#Incoming - Pending
@login_required
def in_requests(request):
    context = {
    'incoming': Request.objects.filter(assign_to=request.user.profile.department).filter(status='Pending')
    }
    return render(request, 'request/incoming.html', context)

#Incoming - In Progress
@login_required
def in_requests_progress(request):
    context = {
    'in_requests_in_progress': Request.objects.filter(assign_to=request.user.profile.department).filter(status='Progress')
    }
    return render(request, 'request/in_inprogress.html', context)

#Incoming - Complete
@login_required
def in_requests_complete(request):
    context = {
    'in_requests_complete': Request.objects.filter(assign_to=request.user.profile.department).filter(status='Complete')
    }
    return render(request, 'request/in_complete.html', context)
