from django.urls import path
from . import views

urlpatterns = [
	path('signup/', views.SighnUpView.as_view(), name='signup'),
]
