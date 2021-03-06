from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^editar/(?P<idTrabajador>\d+)$', views.editar_perfil, name='editar'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^ingresar$', views.ingresar, name='ingresar'),
    #url(r'^register', views.register, name='registro'),
    url(r'^register', views.registerTrabajador, name='registro'),
    url(r'^logout$', views.logout),
    url(r'^trabajador/(?P<pk>\d+)$', views.detail),
    # url(r'^detail', views.detalle_trabajador, name='detalle'),
    url(r'^detail/(?P<id>\d+)/$', views.detalle_trabajador, name='detalle'),
    # url(r'^addComment', views.add_comment),
    url(r'^addComment/(?P<idTrabajador>\d+)$', views.add_comment, name='comentar'),
    url(r'^mostrarComentarios/(?P<idTrabajador>\d+)$', views.mostrarComentarios),
    url(r'^mostrarTrabajadores/(?P<tipo>\w+)$', views.mostrarTrabajadores),
    url(r'^mostrarTrabajadores', views.mostrarTrabajadores),
    url(r'^tipoServicio/(?P<pk>\d+)$', views.getTiposDeServicio),
]
