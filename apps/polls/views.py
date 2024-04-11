from django.shortcuts import redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Poll,Vote
from .forms import PollForm
from django.urls import reverse_lazy
from django.db.models import Count
from django.core.paginator import Paginator


class PollsDashboardView(LoginRequiredMixin,generic.TemplateView):
    template_name = "pages/home.html"
    login_url = "user:login"


class PollListView(LoginRequiredMixin,generic.ListView):
    model = Poll
    login_url = 'user:login'
    template_name = 'pages/poll_list.html'
    context_object_name = 'polls'
    paginate_by = 3  # Set the number of items per page
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        polls = Poll.objects.all()  # Get all polls
        paginator = Paginator(polls, self.paginate_by)
        page_number = self.request.GET.get('page')  # Get current page from URL
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context


class AlreadyVotedView(LoginRequiredMixin,generic.TemplateView):
     template_name = 'pages/already-voted.html'
     login_url = 'user:login'


class PollDetailView(LoginRequiredMixin,generic.DetailView):
    model = Poll
    login_url = 'user:login'
    template_name = 'pages/poll_detail.html'
    queryset = Poll.objects.all()
    context_object_name = 'poll'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        
        # Fetch the vote of the current user for the current poll
        try:
            vote = Vote.objects.get(user=request.user, poll_id=self.object.pk)
        except Vote.DoesNotExist:
            vote = None

        context = self.get_context_data(object=self.object, vote=vote)
        return self.render_to_response(context)
       
    def post(self, request, *args, **kwargs):
        poll = self.get_object()  # Get the poll object
        choice = request.POST.get('choice')  # Get the choice selected by the user

            # Check if the user has already voted for this poll
        if Vote.objects.filter(user=request.user, poll=poll).exists():
            # Redirect to a page indicating that the user has already voted
            return redirect('polls:already_voted')
        
        if choice:  # Ensure a choice is selected
            vote = Vote(user=request.user, poll=poll, choice=choice)  # Create a vote object
            vote.save()  # Save the vote
            
            # Redirect to the results page after voting
            return redirect('polls:poll_list')
        else:
            # Handle case where no choice is selected
            return redirect('polls:poll_detail')
    

class PollCreateView(LoginRequiredMixin, generic.CreateView):
    model = Poll
    form_class = PollForm
    template_name = 'pages/poll_create.html'
    success_url = reverse_lazy('polls:poll_list')
    login_url = 'user:login'


    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)



