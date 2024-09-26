from django.contrib import messages
from django.shortcuts import render
from django.views.generic import View


class HomeView(View):
    def get(self, request):
        context = {
            'title': 'Bosh sahifa',
        }
        return render(request, 'hilo/index.html', context)
