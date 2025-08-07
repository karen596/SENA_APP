from django.http import HttpResponse
from django.template import loader
from .models import Aprendiz
from django.shortcuts import get_object_or_404


# Create your views here.

def aprendices(request):
    lista_aprendices = Aprendiz.objects.all().order_by('apellido', 'nombre')
    template = loader.get_template('lista_aprendices.html')
    
    context = {
    'lista_aprendices': lista_aprendices,
    'total_aprendices': lista_aprendices.count(),
    }
    return HttpResponse(template.render(context, request))

def inicio(request):
    # Estadísticas generales
    total_aprendices = Aprendiz.objects.count()
    template = loader.get_template('inicio.html')
    
    context = {
        'total_aprendices': total_aprendices,
        # Comentadas temporalmente hasta crear las otras apps
        # 'total_instructores': 0,
        # 'total_programas': 0,
        # 'total_cursos': 0,
        # 'cursos_activos': 0,
    }
    return HttpResponse(template.render(context, request))

def detalle_aprendiz(request, aprendiz_id):
    aprendiz = get_object_or_404(Aprendiz, id=aprendiz_id)
    template = loader.get_template('detalle_aprendiz.html')
    
    context = {
        'aprendiz': aprendiz,
    }
    
    return HttpResponse(template.render(context, request))