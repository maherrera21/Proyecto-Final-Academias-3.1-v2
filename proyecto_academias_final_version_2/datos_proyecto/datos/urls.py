from django.conf.urls import patterns, url

from datos import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'funcion_ajax/$', views.funcion_ajax, name='funcion_ajax'),
    url(r'funcion_ajax2/$', views.funcion_ajax2, name='funcion_ajax2'),
    #url(r'inicio/$', views.inicio, name='inicio'),
    url(r'acerca_de/$', views.acerca_de, name='acerca_de'),
    url(r'mapa/$', views.mapa, name='mapa'),
    url(r'defunciones_fetales/$', views.reporte, name='defunciones_fetales'),
    url(r'defunciones_generales/$', views.defunciones_generales, name='defunciones_generales'),
    url(r'sexo/$', views.sexo, name='sexo'),
    url(r'anio_def/$', views.anio_def, name='anio_def'),
    url(r'hijos_nac_muertos/$', views.hijos_nac_muertos, name='hijos_nac_muertos'),
    url(r'estado_civil/$', views.estado_civil, name='estado_civil'),
    url(r'etnia/$', views.etnia, name='etnia'),
    url(r'provincia/$', views.provincia, name='provincia'),
    url(r'lugar/$', views.lugar, name='lugar'),
    url(r'sexo2/$', views.sexo2, name='sexo2'),
    url(r'anio_def_gen/$', views.anio_def_gen, name='anio_def_gen'),
    url(r'prov_general/$', views.prov_general, name='prov_general'),
    url(r'lugar_def_gen/$', views.lugar_def_gen, name='lugar_def_gen'),

)