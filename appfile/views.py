from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import QuoteSerializer
from .models import Quote
from django.shortcuts import render, redirect
from .forms import AdminCreationForm

import random


class QuoteDetailView(generics.RetrieveAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

    def get(self, request, *args, **kwargs):
        count = Quote.objects.count()
        random_index = random.randint(0, count - 1)
        quote = Quote.objects.all()[random_index]
        serializer = self.get_serializer(quote)
        return Response(serializer.data)
