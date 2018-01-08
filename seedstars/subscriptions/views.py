from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import SubscriptionForm
from .models import Subscription


# Create your views here.
def home(request):
    return render(request, 'subscriptions/home.html')


def listings(request):
    subscriptions = Subscription.objects.all()
    paginator = Paginator(subscriptions, 25)

    page = request.GET.get('page')
    subscriptions = paginator.get_page(page)
    return render(request, 'subscriptions/list.html', {'subscriptions': subscriptions})


def add(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/list/')
    else:
        form = SubscriptionForm()

    return render(request, 'subscriptions/add.html', {'form': form})
