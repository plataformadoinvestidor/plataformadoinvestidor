from django.shortcuts import render

# aqui eu estou dizendo que quero pegar os cursos que estão cadastrados para vim para a minha pagina de cursos.html
from .models import Home

# Create your views here.
def home(request):
    # aqui vou puxar o meu modelo home
    # estou dizendo q a minha variavel "home" vai receber tem no meu model "home"
    home = Home.objects.all()
    # esse caminho é o caminho do diretorio aonde eu vou colocar meu template
    template_name = 'home/home.html'
    context = {
        'home': home
    }
    return render(request, template_name, context)

def planos(request):
    return render(request, 'home/planos.html')

def faq(request):
    return render(request, 'home/faq.html')

def login(request):
    return render(request, 'home/login.html')

def quemSomos(request):
    return render(request, 'home/quemsomos.html')

def contato(request):
    return render(request, 'home/contato.html')

def cadastrarUsuario(request):
    return render(request, 'home/cadastrarUsuario.html')

def painelUsuario(request):
    return render(request, 'arealogada/painelusuario.html')





# def details(request, pk):
#     home = Home.objects.get(pk=pk)
#     template_name = 'courses/details.html'
#     context ={
#         'courses': courses
#     }
#     return render(request, template_name, context)