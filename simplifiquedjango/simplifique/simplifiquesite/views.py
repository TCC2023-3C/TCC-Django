from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Comentario
from .forms import ComentarioForm
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
    else:
        form = ComentarioForm()

    comentarios = Comentario.objects.all()

    context = {
        'formulario': form,
        'comentarios': comentarios
    }

    return render(request, './site/index.html', context)

