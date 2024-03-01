from django.urls import path, include
from market import views
from .views import SignupView

app_name = 'product'

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
]
