from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Survey, Pages
from .forms import StepOneForm, StepTwoForm, StepThreeForm, PageForm
from formtools.wizard.views import SessionWizardView


# Create your views here.
# def hello(request):
#     if request.method == 'GET':
#         form = HelloForm()
#         return render(request, 'surveys_app/hello.html', context={'form': form})
#     else:
#         form = HelloForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('surveys:survey'))
#         else:
#             return render(request, 'surveys_app/hello.html', context={'form': form})


# ListView
class SurveysListView(LoginRequiredMixin, ListView):
    model = Survey
    template_name = 'surveys_app/surveys.html'


# FormWizardView
class FormWizardView(LoginRequiredMixin, SessionWizardView):
    template_name = "surveys_app/add_survey.html"
    form_list = [StepOneForm, StepTwoForm, StepThreeForm]

    def done(self, form_list, **kwargs):
        data = {k: v for form in form_list for k, v in form.cleaned_data.items()}
        Survey.objects.create(**data)
        # return render(self.request, 'surveys_app/done.html', {
        #     'form_data': [form.cleaned_data for form in form_list],
        # })
        return HttpResponseRedirect(reverse("surveys:surveys"))


# SurveyDetailView
class SurveyDetailView(LoginRequiredMixin,  DetailView):
    model = Survey
    template_name = 'surveys_app/survey.html'


class SurveyAddPageView(LoginRequiredMixin, DetailView):
    model = Survey
    template_name = 'surveys_app/add_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PageForm
        return context


class SurveyAddPageCreateView(LoginRequiredMixin, CreateView):
    model = Pages
    template_name = 'surveys_app/add_page.html'
    success_url = '/'
    form_class = PageForm

    def post(self, request, *args, **kwargs):
        self.survey_pk = kwargs['pk']
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        survey = get_object_or_404(Survey, pk=self.survey_pk)
        form.instance.survey = survey
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('surveys:survey', kwargs={'pk': self.survey_pk})


class HelloUpdateView(LoginRequiredMixin,  UpdateView):
    model = Survey
    fields = ['hello_title', 'hello_text', ]
    template_name = 'surveys_app/hello.html'
    success_url = reverse_lazy('')

    def post(self, request, *args, **kwargs):
        self.survey_id = kwargs['pk']
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('surveys:survey', kwargs={'pk': self.survey_id})


class InfoUpdateView(LoginRequiredMixin,  UpdateView):
    model = Survey
    fields = ['info_title', 'info_text', ]
    template_name = 'surveys_app/info.html'
    success_url = reverse_lazy('')

    def post(self, request, *args, **kwargs):
        self.survey_id = kwargs['pk']
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('surveys:survey', kwargs={'pk': self.survey_id})


class ByeUpdateView(LoginRequiredMixin,  UpdateView):
    model = Survey
    fields = ['bye_title', 'bye_text', ]
    template_name = 'surveys_app/bye.html'
    success_url = reverse_lazy('')

    def post(self, request, *args, **kwargs):
        self.survey_id = kwargs['pk']
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('surveys:survey', kwargs={'pk': self.survey_id})








