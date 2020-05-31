from django.urls import path
from surveys_app import views
from surveys_app.forms import StepOneForm, StepTwoForm, StepThreeForm

app_name = 'surveys_app'

# named_contact_forms = (
#     ('contactdata', StepOneForm),
#     ('leavemessage', StepTwoForm),
# )

urlpatterns = [
    path('surveys/', views.SurveysListView.as_view(), name='surveys'),
    path('survey/<int:pk>/', views.SurveyDetailView.as_view(), name='survey'),
    path('hello/<int:pk>/', views.HelloView.as_view(), name='hello'),
    path('add_survey/', views.FormWizardView.as_view([StepOneForm, StepTwoForm, StepThreeForm]), name='add_survey'),



]