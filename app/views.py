from django.shortcuts import render, get_object_or_404
from django.views.generic import FormView, ListView, DetailView, UpdateView, DeleteView, TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from . import forms

class threads(ListView):
    model = models.Threat
    template_name = 'app/views/threadsList.html'
    paginate_by = 4
    def get_queryset(self):
        return self.model.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pageTitle'] = 'Threads'
        return context

class addThread(FormView):
    template_name = 'app/views/addthread.html'
    success_url = '/threads'
    form_class = forms.ThreadForm
    def form_valid(self, form):
        form.save()
        return super(addThread, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pageTitle'] = 'Add thread'
        return context

class read(ListView):
    model = models.Threat

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)

class readDetail(DetailView):
    template_name = 'app/views/thread.html'
    model = models.Threat

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        thread = super(readDetail, self).get_object()
        queryset = models.Threat.getTestimonies(thread)
        context['pageTitle'] = 'Thread'
        context['testimonies'] = queryset
        context['num'] = models.Threat.getChoices(thread)
        context['positive'] = models.Threat.getChoices(thread, True)
        context['negative'] = models.Threat.getChoices(thread, False)
        return context

class deleteTopic(DeleteView):
    model = models.Topic
    template_name = 'app/views/deletetopic.html'
    success_url = '/topics'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pageTitle'] = 'Delete a topic'
        return context

class updateTopic(UpdateView):
    fields = '__all__'
    template_name = 'app/actions/updatetopic.html'
    model = models.Topic
    success_url = '/topics'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pageTitle'] = 'Update a topic'
        return context

class topics(ListView):
    template_name = 'app/views/topics.html'
    model = models.Topic
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pageTitle'] = 'Topics'
        return context

    def get_queryset(self):
        return self.model.objects.order_by('-id')

class addTopic(FormView):
    template_name = 'app/views/addtopic.html'
    success_url = '/topics'
    form_class = forms.TopicForm
    def form_valid(self, form):
        form.save()
        return super(addTopic, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pageTitle'] = 'Add topic'
        return context

class update(UpdateView):
    fields = '__all__'
    template_name = 'app/actions/update.html'
    model = models.Threat
    success_url = '/threads'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pageTitle'] = 'Update a thread'
        return context

class delete(DeleteView):
    model = models.Threat
    template_name = 'app/actions/delete.html'
    success_url = '/threads'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pageTitle'] = 'Delete a thread'
        return context

class authenticate(FormView):
    template_name = 'app/authenticate.html'
    model = models.Threat
    form_class = forms.TestimonyForm
    success_url = '/threads'

    def form_valid(self, form, **kwargs):
        posted_data = form.save(commit=False)
        posted_data.threat = get_object_or_404(self.model, pk=self.kwargs['pk'])
        posted_data.save()
        return super(authenticate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(authenticate, self).get_context_data(**kwargs)
        context['object'] = get_object_or_404(self.model, pk=self.kwargs['pk'])
        return context

class approve(FormView):
    template_name = 'app/actions/approve.html'
    model = models.Threat
    form_class = forms.AuthForm
    success_url = '/threads'

    def form_valid(self, form, **kwargs):
        posted_data = form.save(commit=False)
        posted_data.threat = get_object_or_404(self.model, pk=self.kwargs['pk'])
        posted_data.choice = True
        posted_data.save()
        return super(approve, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(approve, self).get_context_data(**kwargs)
        context['object'] = get_object_or_404(self.model, pk=self.kwargs['pk'])
        context['pageTitle'] = 'Approve a thread'
        return context

class reject(FormView):
    template_name = 'app/actions/reject.html'
    model = models.Threat
    form_class = forms.AuthForm
    success_url = '/threads'

    def form_valid(self, form, **kwargs):
        posted_data = form.save(commit=False)
        posted_data.threat = get_object_or_404(self.model, pk=self.kwargs['pk'])
        posted_data.choice = False
        posted_data.save()
        return super(reject, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(reject, self).get_context_data(**kwargs)
        context['object'] = get_object_or_404(self.model, pk=self.kwargs['pk'])
        context['pageTitle'] = 'Rejecting threads'
        return context

class empty(TemplateView):
    template_name = 'app/empty.html'

class defaultDashboard(TemplateView):
    template_name = 'app/defaultdashboard.html'

class community(ListView):
    model = models.Threat
    template_name = 'app/views/community.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pageTitle'] = 'Community'
        return context

class chatbot(TemplateView):
    template_name = 'app/views/chatbot.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pageTitle'] = 'Chatbot'
        return context

class stayintouch(TemplateView):
    template_name = 'app/views/stayintouch.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pageTitle'] = 'Stay in touch !'
        return context

class dashboard(TemplateView):
    template_name = 'app/views/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pageTitle'] = 'Dashboard'
        return context
