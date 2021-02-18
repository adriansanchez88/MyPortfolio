from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import TemplateView
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'nombre':'Adrián Sánchez Nievares', 
            'profesión':'Ingeniero Informático'
            })

class AboutPageView(TemplateView):
    template_name = "core/about.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'título':'Conóceme un poco', 
            'subtítulo1':'Ingeniero Informático',
            'subtítulo1_info':'Graduado de la Universidad de las Ciencias Informáticas.',
            'subtítulo2':'Desarrollador Web',
            'subtítulo2_info':'Actualmente me desempeño como desarrollador web, específicamente en el lenguaje de programación Python con su framework Django.',
            'subtítulo3':'Mis Proyectos',
            'subtítulo3_info':'He desarrollado algunos proyectos utilizando diversas tecnologías, manteniendo siempre las buenas prácticas de programación.',
            })

def contacto(request):
    form = ContactForm()
    contexto = {
            'título':'Mi información de contacto',
            'teléfono':'+34 634 147 902', 
            'email':'adriansanchez88@gmail.com',
            'form':form
            }
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            nombre = datos.get('nombre')
            email = datos.get('email')
            asunto = datos.get('asunto')
            mensaje = datos.get('mensaje')
            try:
                send_mail(
                    "Mi Portafolio: " + asunto,
                    "De {} <{}>\n\nEscribió:\n\n{}".format(nombre, email, mensaje),
                    settings.EMAIL_HOST_USER,
                    ['adriansanchez88@gmail.com'],
                    fail_silently= False,
                )
                return redirect(reverse('contact')+'?ok')
            except:
                return redirect(reverse('contact')+'?fail')
    return render(request, 'core/contact.html', contexto)