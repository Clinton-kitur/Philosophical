from django.urls import path
from . import views

urlpatterns = [
    path('quotes/<int:pk>/', views.QuoteDetailView.as_view(), name='quote_detail'),
]