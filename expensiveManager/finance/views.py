
from django.db import transaction
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, request

from finance.models import Transaction
def home(request):

    transaction = Transaction.objects.all()
    entrer = sum(t.amount for t in transaction if t.type == 'entree')
    sortie = sum(t.amount for t in transaction if t.type == 'sorti')
    