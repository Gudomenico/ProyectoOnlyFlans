from django.shortcuts import render,loader, redirect
from django.http import HttpResponse
from .models import Flan, Locales
from .forms import ContactFormModelForm, LoginForm
from .models import ContactForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        flanes = Flan.objects.filter(is_private=False)
        template = loader.get_template('index.html')
        context = {'flanes': flanes}
        return HttpResponse(template.render(context, request))
    else:
        return redirect('/bienvenido/')
        

def about(request):
    template = loader.get_template('about.html')
    context = {}
    return HttpResponse(template.render(context, request))

def secreto(request):
    locales = Locales.objects.all()
    template = loader.get_template('secreto.html')
    context = {'locales': locales}
    return HttpResponse(template.render(context, request))

def mensaje_contacto(request):
    template = loader.get_template('mensaje_contacto.html')
    context = {}
    return HttpResponse(template.render(context, request))

@login_required
def welcome(request):
    flanes = Flan.objects.all()
    template = loader.get_template('welcome.html')
    context = {'flanes': flanes}
    return HttpResponse(template.render(context, request))

def base(request):
    template = loader.get_template('base.html')
    context = {}
    return HttpResponse(template.render(context, request))

def inicio(request):
    template = loader.get_template('inicio.html')
    context = {}
    return HttpResponse(template.render(context, request))

def contacto(request):
    template = 'contacto.html'
    if request.method == "POST":
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Formulario enviado con éxito.')
            return redirect('/contacto/')
        else:
            messages.error(request, 'Hubo un error al enviar el formulario.')
    else:
        form = ContactFormModelForm()
        messages.success(request, 'Rellena el formulario para contactarnos')

    return render(request, template, {'form': form})

def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request, 'Te has registrado exitosamente. Puedes iniciar sesión ahora.')
            return redirect('/inicio_sesion/')  
        else:
            messages.error(request, 'Hubo un error al registrarte. Por favor, revisa los campos.')

    else:
        form = UserCreationForm(request.GET)

    return render(request, 'registro.html', {'form': form})


def cierre_sesion(request):
    logout(request)
    messages.success(request, "Has cerrado sesión correctamente.")
    return redirect('/')


def inicio_sesion(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Has iniciado sesión correctamente.')
                return redirect('/bienvenido/')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')  
        else:
            messages.error(request, 'Formulario inválido.')  
            for field in form:
                for error in field.errors:
                    print(f"Error en {field.name}: {error}")
    else:
        form = LoginForm(request.GET)  

    return render(request, 'inicio_sesion.html', {'form': form})