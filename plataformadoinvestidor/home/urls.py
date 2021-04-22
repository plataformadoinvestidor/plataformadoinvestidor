from django.contrib import admin
from django.urls import path
from django.urls import include, path, re_path
from home.views import home, planos, faq, login, quemSomos, contato, cadastrarUsuario, painelUsuario, extratoBH
#from courses.views import courses, details

# Configurar minhas URLs para acessar a pagina
admin.autodiscover()
urlpatterns = [
    # Aqui eu coloco a URL que quero puxar, qual views model que vou utilizar
    # expressão regex para falar q aceita qualquer informação q 
    re_path(r'^$', home, name='home'),
    #re_path(r'^$', planos, name='planos'),
    re_path(r'^planos/$', planos, name='planos'),
    re_path(r'^faq/$', faq , name='faq'),
    re_path(r'^login/$', login , name='login'),
    re_path(r'^quemSomos/$', quemSomos , name='quemsomos'), 
    re_path(r'^contato/$', contato , name='contato'),
    re_path(r'^cadastrarUsuario/$', cadastrarUsuario , name='cadastrarUsuario'),
    re_path(r'^painelusuario/$', painelUsuario , name='painelusuario'),
    re_path(r'^extratoBH/$', extratoBH , name='extratoBH'),
    
    
    
    
    
    # expressão regular que vai pegar calcular valor inteiro, no nosso caso vai pegar pelo ID de cada curso
    #re_path(r'^(?P<pk>\d+)/$', details, name='details'),
    

]
