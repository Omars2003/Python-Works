from django.urls import path
from django.views.generic import TemplateView

import myapp.views
urlpatterns = [
    path('hello/', myapp.views.hello, name='hello'),
    path('connection/', TemplateView.as_view(template_name='loggedin.html')),
    path('login/', myapp.views.LoginForm, name='login'),

]
