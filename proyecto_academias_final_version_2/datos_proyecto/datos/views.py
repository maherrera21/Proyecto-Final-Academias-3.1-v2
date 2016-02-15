# -*- encoding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import JsonResponse

from django.template import RequestContext
from datos.models import *
import json
from datos.forms import *


def index(request):
    return render(request, 'index.html')


def acerca_de(request):
    return render(request, 'acerca_de.html')

def mapa(request):
    return render(request, 'mapa.html')

def reporte(request):
    """
    """
    fetales=DefunFetal.objects.all()
    data=[]
    for p in fetales:
        data.append({'id_defun_fetal':p.id_defun_fetal, 'sexo':p.sexo, 'anio_def':p.anio_def, 'sem_gestac':p.sem_gestac}) 
    print data
    data1=json.dumps(data)
    context = {'data' :data1}
    return render(request, 'defunciones_fetales.html',context)


@csrf_exempt
def funcion_ajax(request):
    """
    """
    if request.is_ajax() == True:
        req = {}
        letra = request.POST.getlist('valor')[0]
        fetales = serializers.serialize('json', DefunFetal.objects.filter(nombre__startswith = letra ))
        req['mensaje'] = 'Correcto .... cargando datos '
        req['fetales'] = fetales 
        return JsonResponse(req, safe=False)


def sexo(request):
    
    #Obtencion de sexo
    persona=DefunFetal.objects.filter(sexo='Hombre')
    persona1=DefunFetal.objects.filter(sexo='Mujer')


    cont_Mujeres=0;
    cont_Hombres=0;

    for p in persona:
        cont_Mujeres=cont_Mujeres+1
    for p in persona1:
        cont_Hombres=cont_Hombres+1

    pa=[{'name': 'Hombre', 'data': cont_Mujeres},
        {'name': 'Mujeres', 'data': cont_Hombres}
        ]

    return render(request, 'sexo.html', {'pa': pa})

def anio_def(request):
    
    #Obtencion de anio_def
    persona=DefunFetal.objects.filter(anio_def='1997')
    persona1=DefunFetal.objects.filter(anio_def='1998')
    persona2=DefunFetal.objects.filter(anio_def='1999')
    persona3=DefunFetal.objects.filter(anio_def='2000')
    persona4=DefunFetal.objects.filter(anio_def='2001')
    persona5=DefunFetal.objects.filter(anio_def='2002')
    persona6=DefunFetal.objects.filter(anio_def='2003')
    persona7=DefunFetal.objects.filter(anio_def='2004')
    persona8=DefunFetal.objects.filter(anio_def='2005')
    persona9=DefunFetal.objects.filter(anio_def='2006')
    persona10=DefunFetal.objects.filter(anio_def='2007')
    persona11=DefunFetal.objects.filter(anio_def='2008')
    persona12=DefunFetal.objects.filter(anio_def='2009')
    persona13=DefunFetal.objects.filter(anio_def='2010')
    persona14=DefunFetal.objects.filter(anio_def='2011')
    persona15=DefunFetal.objects.filter(anio_def='2012')
    persona16=DefunFetal.objects.filter(anio_def='2013')
    persona17=DefunFetal.objects.filter(anio_def='2014')

    cont_1997=0;
    cont_1998=0;
    cont_1999=0;
    cont_2000=0;
    cont_2001=0;
    cont_2002=0;
    cont_2003=0;
    cont_2004=0;
    cont_2005=0;
    cont_2006=0;
    cont_2007=0;
    cont_2008=0;
    cont_2009=0;
    cont_2010=0;
    cont_2011=0;
    cont_2012=0;
    cont_2013=0;
    cont_2014=0;

    for p in persona:
        cont_1997=cont_1997+1
    for p in persona1:
        cont_1998=cont_1998+1
    for p in persona2:
        cont_1999=cont_1999+1
    for p in persona3:
        cont_2000=cont_2000+1
    for p in persona4:
        cont_2001=cont_2001+1
    for p in persona5:
        cont_2002=cont_2002+1
    for p in persona6:
        cont_2003=cont_2003+1
    for p in persona7:
        cont_2004=cont_2004+1
    for p in persona8:
        cont_2005=cont_2005+1
    for p in persona9:
        cont_2006=cont_2006+1
    for p in persona10:
        cont_2007=cont_2007+1
    for p in persona11:
        cont_2008=cont_2008+1
    for p in persona12:
        cont_2009=cont_2009+1
    for p in persona13:
        cont_2010=cont_2010+1
    for p in persona14:
        cont_2011=cont_2011+1
    for p in persona15:
        cont_2012=cont_2012+1
    for p in persona16:
        cont_2013=cont_2013+1
    for p in persona17:
        cont_2014=cont_2014+1

    pa=[{'name': '1997', 'data': cont_1997},
        {'name': '1998', 'data': cont_1998},
        {'name': '1999', 'data': cont_1999},
        {'name': '2000', 'data': cont_2000},
        {'name': '2001', 'data': cont_2001},
        {'name': '2002', 'data': cont_2002},
        {'name': '2003', 'data': cont_2003},
        {'name': '2004', 'data': cont_2004},
        {'name': '2005', 'data': cont_2005},
        {'name': '2006', 'data': cont_2006},
        {'name': '2007', 'data': cont_2007},
        {'name': '2008', 'data': cont_2008},
        {'name': '2009', 'data': cont_2009},
        {'name': '2010', 'data': cont_2010},
        {'name': '2011', 'data': cont_2011},
        {'name': '2012', 'data': cont_2012},
        {'name': '2013', 'data': cont_2013},
        {'name': '2014', 'data': cont_2014},
        ]

    return render(request, 'anio_def.html', {'pa': pa})
    

def hijos_nac_muertos(request):

    #Obtencion de hijos_nac_muertos
    persona=DatosMadre.objects.filter(hijos_nac_muertos='1')
    persona1=DatosMadre.objects.filter(hijos_nac_muertos='2')
    persona2=DatosMadre.objects.filter(hijos_nac_muertos='3')
    persona3=DatosMadre.objects.filter(hijos_nac_muertos='4')  

    cont_1=0;
    cont_2=0;
    cont_3=0;
    cont_4=0;

    for p in persona:
        cont_1=cont_1+1
    for p in persona1:
        cont_2=cont_2+1
    for p in persona2:
        cont_3=cont_3+1
    for p in persona3:
        cont_4=cont_4+1

    pa=[{'name': '1', 'data': cont_1},
        {'name': '2', 'data': cont_2},
        {'name': '3', 'data': cont_3},
        {'name': '4', 'data': cont_4},
        ]

    return render(request, 'hijos_nac_muertos.html', {'pa': pa})


def estado_civil(request):
    
    #Obtencion de estado_civil
    persona=DatosMadre.objects.filter(estado_civil='Casada')
    persona1=DatosMadre.objects.filter(estado_civil='Unida')
    persona2=DatosMadre.objects.filter(estado_civil='Soltera')
    persona3=DatosMadre.objects.filter(estado_civil='Viuda')
    persona4=DatosMadre.objects.filter(estado_civil='Se ignora')  

    cont_est=0;
    cont_est1=0;
    cont_est2=0;
    cont_est3=0;
    cont_est4=0;

    for p in persona:
        cont_est=cont_est+1
    for p in persona1:
        cont_est1=cont_est1+1
    for p in persona2:
        cont_est2=cont_est2+1
    for p in persona3:
        cont_est3=cont_est3+1
    for p in persona4:
        cont_est4=cont_est4+1

    pa=[{'name': 'Casada', 'data': cont_est},
        {'name': 'Unida', 'data': cont_est1},
        {'name': 'Soltera', 'data': cont_est2},
        {'name': 'Viuda', 'data': cont_est3},
        {'name': 'Se ignora', 'data': cont_est4},
        ]

    return render(request, 'estado_civil.html', {'pa': pa})


def etnia(request):
    
    #Obtencion de etnia
    persona=DatosMadre.objects.filter(etnia='Mestiza')
    persona1=DatosMadre.objects.filter(etnia='Indígena')
    persona3=DatosMadre.objects.filter(etnia='Afroecuatoriana-Afrodescendiente')
    persona4=DatosMadre.objects.filter(etnia='Negra')
    persona5=DatosMadre.objects.filter(etnia='Mulata')
    persona6=DatosMadre.objects.filter(etnia='Blanca')
    persona7=DatosMadre.objects.filter(etnia='Ignorado')  

    cont_etnia=0;
    cont_etnia1=0;
    cont_etnia3=0;
    cont_etnia4=0;
    cont_etnia5=0;
    cont_etnia6=0;
    cont_etnia7=0;

    for p in persona:
        cont_etnia=cont_etnia+1
    for p in persona1:
        cont_etnia1=cont_etnia1+1
    for p in persona3:
        cont_etnia3=cont_etnia3+1
    for p in persona4:
        cont_etnia4=cont_etnia4+1
    for p in persona5:
        cont_etnia5=cont_etnia5+1
    for p in persona6:
        cont_etnia6=cont_etnia6+1
    for p in persona7:
        cont_etnia7=cont_etnia7+1

    pa=[{'name': 'Mestiza', 'data': cont_etnia},
        {'name': 'Indígena', 'data': cont_etnia1},
        {'name': 'Afroecuatoriana-Afrodescendiente', 'data': cont_etnia3},
        {'name': 'Negra', 'data': cont_etnia4},
        {'name': 'Mulata', 'data': cont_etnia5},
        {'name': 'Blanca', 'data': cont_etnia6},
        {'name': 'Ignorado', 'data': cont_etnia7},
        ]

    return render(request, 'etnia.html', {'pa': pa})


def provincia(request):
    
    #Obtencion de provincia
    persona=DetalleDefFet.objects.filter(nombre_detalle_fet='Azuay')
    persona1=DetalleDefFet.objects.filter(nombre_detalle_fet='Bolívar')
    persona2=DetalleDefFet.objects.filter(nombre_detalle_fet='Tungurahua')
    persona3=DetalleDefFet.objects.filter(nombre_detalle_fet='Los Ríos')
    persona4=DetalleDefFet.objects.filter(nombre_detalle_fet='Cañar')
    persona5=DetalleDefFet.objects.filter(nombre_detalle_fet='Guayas')
    persona6=DetalleDefFet.objects.filter(nombre_detalle_fet='Carchi')
    persona7=DetalleDefFet.objects.filter(nombre_detalle_fet='Pichincha')
    persona8=DetalleDefFet.objects.filter(nombre_detalle_fet='Cotopaxi')
    persona9=DetalleDefFet.objects.filter(nombre_detalle_fet='Chimborazo')
    persona10=DetalleDefFet.objects.filter(nombre_detalle_fet='El Oro')
    persona11=DetalleDefFet.objects.filter(nombre_detalle_fet='Esmeraldas')
    persona12=DetalleDefFet.objects.filter(nombre_detalle_fet='Imbabura')
    persona13=DetalleDefFet.objects.filter(nombre_detalle_fet='Loja')
    persona14=DetalleDefFet.objects.filter(nombre_detalle_fet='Manabí') 
    persona15=DetalleDefFet.objects.filter(nombre_detalle_fet='Morona Santiago')
    persona16=DetalleDefFet.objects.filter(nombre_detalle_fet='Napo')
    persona17=DetalleDefFet.objects.filter(nombre_detalle_fet='Pastaza')
    persona18=DetalleDefFet.objects.filter(nombre_detalle_fet='Zamora Chinchipe')
    persona19=DetalleDefFet.objects.filter(nombre_detalle_fet='Galapagos')
    persona20=DetalleDefFet.objects.filter(nombre_detalle_fet='Sucumbíos')
    persona21=DetalleDefFet.objects.filter(nombre_detalle_fet='Santo Domingo de los Tsáchilas')
    persona22=DetalleDefFet.objects.filter(nombre_detalle_fet='Latacunga')
    persona23=DetalleDefFet.objects.filter(nombre_detalle_fet='Orellana')

    cont_provincia=0;
    cont_provincia1=0;
    cont_provincia2=0;
    cont_provincia3=0;
    cont_provincia4=0;
    cont_provincia5=0;
    cont_provincia6=0;
    cont_provincia7=0;
    cont_provincia8=0;
    cont_provincia9=0;
    cont_provincia10=0;
    cont_provincia11=0;
    cont_provincia12=0;
    cont_provincia13=0;
    cont_provincia14=0;
    cont_provincia15=0;
    cont_provincia16=0;
    cont_provincia17=0;
    cont_provincia18=0;
    cont_provincia19=0;
    cont_provincia20=0;
    cont_provincia21=0;
    cont_provincia22=0;
    cont_provincia23=0;

    for p in persona:
        cont_provincia=cont_provincia+1
    for p in persona1:
        cont_provincia1=cont_provincia1+1
    for p in persona2:
        cont_provincia2=cont_provincia2+1
    for p in persona3:
        cont_provincia3=cont_provincia3+1
    for p in persona4:
        cont_provincia4=cont_provincia4+1
    for p in persona5:
        cont_provincia5=cont_provincia5+1
    for p in persona6:
        cont_provincia6=cont_provincia6+1
    for p in persona7:
        cont_provincia7=cont_provincia7+1
    for p in persona8:
        cont_provincia8=cont_provincia8+1
    for p in persona9:
        cont_provincia9=cont_provincia9+1
    for p in persona10:
        cont_provincia10=cont_provincia10+1
    for p in persona11:
        cont_provincia11=cont_provincia11+1
    for p in persona12:
        cont_provincia12=cont_provincia12+1
    for p in persona13:
        cont_provincia13=cont_provincia13+1
    for p in persona14:
        cont_provincia14=cont_provincia14+1
    for p in persona15:
        cont_provincia15=cont_provincia15+1
    for p in persona16:
        cont_provincia16=cont_provincia16+1
    for p in persona17:
        cont_provincia17=cont_provincia17+1
    for p in persona18:
        cont_provincia18=cont_provincia18+1
    for p in persona19:
        cont_provincia19=cont_provincia19+1
    for p in persona20:
        cont_provincia20=cont_provincia20+1
    for p in persona21:
        cont_provincia21=cont_provincia21+1
    for p in persona22:
        cont_provincia22=cont_provincia22+1
    for p in persona23:
        cont_provincia23=cont_provincia23+1


    pa=[{'name': 'Azuay', 'data': cont_provincia},
        {'name': 'Bolívar', 'data': cont_provincia1},
        {'name': 'Tungurahua', 'data': cont_provincia2},
        {'name': 'Los Ríos', 'data': cont_provincia3},
        {'name': 'Cañar', 'data': cont_provincia4},
        {'name': 'Guayas', 'data': cont_provincia5},
        {'name': 'Carchi', 'data': cont_provincia6},
        {'name': 'Pichincha', 'data': cont_provincia7},
        {'name': 'Cotopaxi', 'data': cont_provincia8},
        {'name': 'Chimborazo', 'data': cont_provincia9},
        {'name': 'El Oro', 'data': cont_provincia10},
        {'name': 'Esmeraldas', 'data': cont_provincia11},
        {'name': 'Imbabura', 'data': cont_provincia12},
        {'name': 'Loja', 'data': cont_provincia13},
        {'name': 'Manabí', 'data': cont_provincia14},
        {'name': 'Morona Santiago', 'data': cont_provincia15},
        {'name': 'Napo', 'data': cont_provincia16},
        {'name': 'Pastaza', 'data': cont_provincia17},
        {'name': 'Zamora Chinchipe', 'data': cont_provincia18},
        {'name': 'Galápagos', 'data': cont_provincia19},
        {'name': 'Sucumbíos', 'data': cont_provincia20},
        {'name': 'Santo Domingo de los Tsáchilas', 'data': cont_provincia21},
        {'name': 'Latacunga', 'data': cont_provincia22},
        {'name': 'Orellana', 'data': cont_provincia23},
        ]

    return render(request, 'provincia.html', {'pa': pa})


def lugar(request):
    
    #Obtencion de lugar de defunción
    persona=DetalleDefFet.objects.filter(nombre_detalle_fet='Hospital, Clínica o Consultorio Privado')
    persona1=DetalleDefFet.objects.filter(nombre_detalle_fet='Establecimiento del Ministerio de Salud')
    persona2=DetalleDefFet.objects.filter(nombre_detalle_fet='Casa')
    persona3=DetalleDefFet.objects.filter(nombre_detalle_fet='Hospital')
    persona4=DetalleDefFet.objects.filter(nombre_detalle_fet='Establecimiento de la Junta de Beneficencia')
    persona5=DetalleDefFet.objects.filter(nombre_detalle_fet='Otro Establecimiento Público')  

    cont_lugar=0;
    cont_lugar1=0;
    cont_lugar2=0;
    cont_lugar3=0;
    cont_lugar4=0;
    cont_lugar5=0;

    for p in persona:
        cont_lugar=cont_lugar+1
    for p in persona1:
        cont_lugar1=cont_lugar1+1
    for p in persona2:
        cont_lugar2=cont_lugar2+1
    for p in persona3:
        cont_lugar3=cont_lugar3+1
    for p in persona4:
        cont_lugar4=cont_lugar4+1
    for p in persona5:
        cont_lugar5=cont_lugar5+1

    pa=[{'name': 'Hospital, Clínica o Consultorio Privado', 'data': cont_lugar},
        {'name': 'Establecimiento del Ministerio de Salud', 'data': cont_lugar1},
        {'name': 'Casa', 'data': cont_lugar2},
        {'name': 'Hospital', 'data': cont_lugar3},
        {'name': 'Establecimiento de la Junta de Beneficencia', 'data': cont_lugar4},
        {'name': 'Otro Establecimiento Público', 'data': cont_lugar5},
        ]

    return render(request, 'lugar_defunción.html', {'pa': pa})


def defunciones_generales(request):
    """
    """

    generales = DefunGeneral.objects.all()
    context = {'generales' : generales}
    return render(request, 'defunciones_generales.html', context)


@csrf_exempt
def funcion_ajax2(request):
    """
    """
    if request.is_ajax() == True:
        req = {}
        defun_generales = request.POST.getlist('valor')[0]
        generales = serializers.serialize('json', DefunGeneral.objects.filter(nombre__startswith = defunciones_generales))
        req['mensaje'] = 'Correcto .... cargando datos '
        req['defun_generales'] = defun_generales 
        return JsonResponse(req, safe=False)

def sexo2(request):
    
    #Obtencion de sexo defunciones generales
    persona=DefunGeneral.objects.filter(sexo='Hombre')
    persona1=DefunGeneral.objects.filter(sexo='Mujer')


    cont_Mujeres=0;
    cont_Hombres=0;

    for p in persona:
        cont_Mujeres=cont_Mujeres+1
    for p in persona1:
        cont_Hombres=cont_Hombres+1

    pa=[{'name': 'Hombre', 'data': cont_Mujeres},
        {'name': 'Mujeres', 'data': cont_Hombres}
        ]

    return render(request, 'sexo2.html', {'pa': pa})

def anio_def_gen(request):
    
    #Obtencion de anio defunción general
    persona=DefunGeneral.objects.filter(anio_def='1997')
    persona1=DefunGeneral.objects.filter(anio_def='1998')
    persona2=DefunGeneral.objects.filter(anio_def='1999')
    persona3=DefunGeneral.objects.filter(anio_def='2000')
    persona4=DefunGeneral.objects.filter(anio_def='2001')
    persona5=DefunGeneral.objects.filter(anio_def='2002')
    persona6=DefunGeneral.objects.filter(anio_def='2003')
    persona7=DefunGeneral.objects.filter(anio_def='2004')
    persona8=DefunGeneral.objects.filter(anio_def='2005')
    persona9=DefunGeneral.objects.filter(anio_def='2006')
    persona10=DefunGeneral.objects.filter(anio_def='2007')
    persona11=DefunGeneral.objects.filter(anio_def='2008')
    persona12=DefunGeneral.objects.filter(anio_def='2009')
    persona13=DefunGeneral.objects.filter(anio_def='2010')
    persona14=DefunGeneral.objects.filter(anio_def='2011')
    persona15=DefunGeneral.objects.filter(anio_def='2012')
    persona16=DefunGeneral.objects.filter(anio_def='2013')
    persona17=DefunGeneral.objects.filter(anio_def='2014')

    cont_1997=0;
    cont_1998=0;
    cont_1999=0;
    cont_2000=0;
    cont_2001=0;
    cont_2002=0;
    cont_2003=0;
    cont_2004=0;
    cont_2005=0;
    cont_2006=0;
    cont_2007=0;
    cont_2008=0;
    cont_2009=0;
    cont_2010=0;
    cont_2011=0;
    cont_2012=0;
    cont_2013=0;
    cont_2014=0;

    for p in persona:
        cont_1997=cont_1997+1
    for p in persona1:
        cont_1998=cont_1998+1
    for p in persona2:
        cont_1999=cont_1999+1
    for p in persona3:
        cont_2000=cont_2000+1
    for p in persona4:
        cont_2001=cont_2001+1
    for p in persona5:
        cont_2002=cont_2002+1
    for p in persona6:
        cont_2003=cont_2003+1
    for p in persona7:
        cont_2004=cont_2004+1
    for p in persona8:
        cont_2005=cont_2005+1
    for p in persona9:
        cont_2006=cont_2006+1
    for p in persona10:
        cont_2007=cont_2007+1
    for p in persona11:
        cont_2008=cont_2008+1
    for p in persona12:
        cont_2009=cont_2009+1
    for p in persona13:
        cont_2010=cont_2010+1
    for p in persona14:
        cont_2011=cont_2011+1
    for p in persona15:
        cont_2012=cont_2012+1
    for p in persona16:
        cont_2013=cont_2013+1
    for p in persona17:
        cont_2014=cont_2014+1

    pa=[{'name': '1997', 'data': cont_1997},
        {'name': '1998', 'data': cont_1998},
        {'name': '1999', 'data': cont_1999},
        {'name': '2000', 'data': cont_2000},
        {'name': '2001', 'data': cont_2001},
        {'name': '2002', 'data': cont_2002},
        {'name': '2003', 'data': cont_2003},
        {'name': '2004', 'data': cont_2004},
        {'name': '2005', 'data': cont_2005},
        {'name': '2006', 'data': cont_2006},
        {'name': '2007', 'data': cont_2007},
        {'name': '2008', 'data': cont_2008},
        {'name': '2009', 'data': cont_2009},
        {'name': '2010', 'data': cont_2010},
        {'name': '2011', 'data': cont_2011},
        {'name': '2012', 'data': cont_2012},
        {'name': '2013', 'data': cont_2013},
        {'name': '2014', 'data': cont_2014},
        ]

    return render(request, 'anio_def_gen.html', {'pa': pa})

def prov_general(request):
    
    #Obtencion de provincia de defunciones generales
    persona=DetalleDefGen.objects.filter(nombre_detalle_gen='Azuay')
    persona1=DetalleDefGen.objects.filter(nombre_detalle_gen='Bolívar')
    persona2=DetalleDefGen.objects.filter(nombre_detalle_gen='Tungurahua')
    persona3=DetalleDefGen.objects.filter(nombre_detalle_gen='Los Ríos')
    persona4=DetalleDefGen.objects.filter(nombre_detalle_gen='Cañar')
    persona5=DetalleDefGen.objects.filter(nombre_detalle_gen='Guayas')
    persona6=DetalleDefGen.objects.filter(nombre_detalle_gen='Carchi')
    persona7=DetalleDefGen.objects.filter(nombre_detalle_gen='Pichincha')
    persona8=DetalleDefGen.objects.filter(nombre_detalle_gen='Cotopaxi')
    persona9=DetalleDefGen.objects.filter(nombre_detalle_gen='Chimborazo')
    persona10=DetalleDefGen.objects.filter(nombre_detalle_gen='El Oro')
    persona11=DetalleDefGen.objects.filter(nombre_detalle_gen='Esmeraldas')
    persona12=DetalleDefGen.objects.filter(nombre_detalle_gen='Imbabura')
    persona13=DetalleDefGen.objects.filter(nombre_detalle_gen='Loja')
    persona14=DetalleDefGen.objects.filter(nombre_detalle_gen='Manabí') 
    persona15=DetalleDefGen.objects.filter(nombre_detalle_gen='Morona Santiago')
    persona16=DetalleDefGen.objects.filter(nombre_detalle_gen='Napo')
    persona17=DetalleDefGen.objects.filter(nombre_detalle_gen='Pastaza')
    persona18=DetalleDefGen.objects.filter(nombre_detalle_gen='Zamora Chinchipe')
    persona19=DetalleDefGen.objects.filter(nombre_detalle_gen='Galápagos')
    persona20=DetalleDefGen.objects.filter(nombre_detalle_gen='Sucumbíos')
    persona21=DetalleDefGen.objects.filter(nombre_detalle_gen='Santo Domingo de los Tsáchilas')
    persona22=DetalleDefGen.objects.filter(nombre_detalle_gen='Latacunga')
    persona23=DetalleDefGen.objects.filter(nombre_detalle_gen='Orellana')

    cont_provincia=0;
    cont_provincia1=0;
    cont_provincia2=0;
    cont_provincia3=0;
    cont_provincia4=0;
    cont_provincia5=0;
    cont_provincia6=0;
    cont_provincia7=0;
    cont_provincia8=0;
    cont_provincia9=0;
    cont_provincia10=0;
    cont_provincia11=0;
    cont_provincia12=0;
    cont_provincia13=0;
    cont_provincia14=0;
    cont_provincia15=0;
    cont_provincia16=0;
    cont_provincia17=0;
    cont_provincia18=0;
    cont_provincia19=0;
    cont_provincia20=0;
    cont_provincia21=0;
    cont_provincia22=0;
    cont_provincia23=0;

    for p in persona:
        cont_provincia=cont_provincia+1
    for p in persona1:
        cont_provincia1=cont_provincia1+1
    for p in persona2:
        cont_provincia2=cont_provincia2+1
    for p in persona3:
        cont_provincia3=cont_provincia3+1
    for p in persona4:
        cont_provincia4=cont_provincia4+1
    for p in persona5:
        cont_provincia5=cont_provincia5+1
    for p in persona6:
        cont_provincia6=cont_provincia6+1
    for p in persona7:
        cont_provincia7=cont_provincia7+1
    for p in persona8:
        cont_provincia8=cont_provincia8+1
    for p in persona9:
        cont_provincia9=cont_provincia9+1
    for p in persona10:
        cont_provincia10=cont_provincia10+1
    for p in persona11:
        cont_provincia11=cont_provincia11+1
    for p in persona12:
        cont_provincia12=cont_provincia12+1
    for p in persona13:
        cont_provincia13=cont_provincia13+1
    for p in persona14:
        cont_provincia14=cont_provincia14+1
    for p in persona15:
        cont_provincia15=cont_provincia15+1
    for p in persona16:
        cont_provincia16=cont_provincia16+1
    for p in persona17:
        cont_provincia17=cont_provincia17+1
    for p in persona18:
        cont_provincia18=cont_provincia18+1
    for p in persona19:
        cont_provincia19=cont_provincia19+1
    for p in persona20:
        cont_provincia20=cont_provincia20+1
    for p in persona21:
        cont_provincia21=cont_provincia21+1
    for p in persona22:
        cont_provincia22=cont_provincia22+1
    for p in persona23:
        cont_provincia23=cont_provincia23+1


    pa=[{'name': 'Azuay', 'data': cont_provincia},
        {'name': 'Bolívar', 'data': cont_provincia1},
        {'name': 'Tungurahua', 'data': cont_provincia2},
        {'name': 'Los Ríos', 'data': cont_provincia3},
        {'name': 'Cañar', 'data': cont_provincia4},
        {'name': 'Guayas', 'data': cont_provincia5},
        {'name': 'Carchi', 'data': cont_provincia6},
        {'name': 'Pichincha', 'data': cont_provincia7},
        {'name': 'Cotopaxi', 'data': cont_provincia8},
        {'name': 'Chimborazo', 'data': cont_provincia9},
        {'name': 'El Oro', 'data': cont_provincia10},
        {'name': 'Esmeraldas', 'data': cont_provincia11},
        {'name': 'Imbabura', 'data': cont_provincia12},
        {'name': 'Loja', 'data': cont_provincia13},
        {'name': 'Manabí', 'data': cont_provincia14},
        {'name': 'Morona Santiago', 'data': cont_provincia15},
        {'name': 'Napo', 'data': cont_provincia16},
        {'name': 'Pastaza', 'data': cont_provincia17},
        {'name': 'Zamora Chinchipe', 'data': cont_provincia18},
        {'name': 'Galápagos', 'data': cont_provincia19},
        {'name': 'Sucumbíos', 'data': cont_provincia20},
        {'name': 'Santo Domingo de los Tsáchilas', 'data': cont_provincia21},
        {'name': 'Latacunga', 'data': cont_provincia22},
        {'name': 'Orellana', 'data': cont_provincia23},
        ]

    return render(request, 'prov_general.html', {'pa': pa})

def lugar_def_gen(request):
    
    #Obtencion de lugar de defunción general
    persona=DetalleDefGen.objects.filter(nombre_detalle_gen='Establecimiento del Ministerio de Salud')
    persona1=DetalleDefGen.objects.filter(nombre_detalle_gen='Hospital, Clínica o Consultorio Privado')
    persona2=DetalleDefGen.objects.filter(nombre_detalle_gen='Establecimiento de la Junta de Beneficencia')
    persona3=DetalleDefGen.objects.filter(nombre_detalle_gen='Otro Establecimiento Público')
    persona4=DetalleDefGen.objects.filter(nombre_detalle_gen='Casa')
    persona5=DetalleDefGen.objects.filter(nombre_detalle_gen='Establecimiento del IESS') 
    persona6=DetalleDefGen.objects.filter(nombre_detalle_gen='Otro') 
    persona7=DetalleDefGen.objects.filter(nombre_detalle_gen='Otro Establecimiento del Estado')

    cont_lugar=0;
    cont_lugar1=0;
    cont_lugar2=0;
    cont_lugar3=0;
    cont_lugar4=0;
    cont_lugar5=0;
    cont_lugar6=0;
    cont_lugar7=0;

    for p in persona:
        cont_lugar=cont_lugar+1
    for p in persona1:
        cont_lugar1=cont_lugar1+1
    for p in persona2:
        cont_lugar2=cont_lugar2+1
    for p in persona3:
        cont_lugar3=cont_lugar3+1
    for p in persona4:
        cont_lugar4=cont_lugar4+1
    for p in persona5:
        cont_lugar5=cont_lugar5+1
    for p in persona6:
        cont_lugar6=cont_lugar6+1
    for p in persona7:
        cont_lugar7=cont_lugar7+1

    pa=[{'name': 'Establecimiento del Ministerio de Salud', 'data': cont_lugar},
        {'name': 'Hospital, Clínica o Consultorio Privado', 'data': cont_lugar1},
        {'name': 'Establecimiento de la Junta de Beneficencia', 'data': cont_lugar2},
        {'name': 'Otro Establecimiento Público', 'data': cont_lugar3},
        {'name': 'Casa', 'data': cont_lugar4},
        {'name': 'Establecimiento del IESS', 'data': cont_lugar5},
        {'name': 'Otro', 'data': cont_lugar6},
        {'name': 'Otro Establecimiento del Estado', 'data': cont_lugar7},
        ]

    return render(request, 'lugar_def_gen.html', {'pa': pa})