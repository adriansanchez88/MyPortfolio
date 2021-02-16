from django.shortcuts import render
from django.views.generic.base import TemplateView

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

class ContactPageView(TemplateView):
    template_name = "core/contact.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'título':'Mi información de contacto es:',
            'teléfono':'+34 634 147 902', 
            'email':'adriansanchez88@gmail.com'
            })