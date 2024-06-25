from django.shortcuts import render
from .forms import inputForm
from django.http import HttpResponse
from .models import Data


def Form_Input(request):
    if request.method == 'POST':
        Details = inputForm(request.POST)
        if Details.is_valid():
            try:
                Details.save()
                context = {'my_form': inputForm()}
                return render(request, 'index.html', context)
            except Exception as e:
                Details.add_error(
                    'ID', 'AN ENTRY WITH THIS ID ALREADY EXITS.')
                context = {'my_form': Details}
                return render(request, 'index.html', context)
        else:
            context = {'my_form': Details}
            return render(request, 'index.html', context)
    else:
        context = {'my_form': inputForm()}
        return render(request, 'index.html', context)


def get_data(request):
    details = Data.objects.all().values()
    print(details[0]['Name'])
    context = {}
    context['details'] = details
    return render(request, 'display.html', context)
