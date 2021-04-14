    # Create your models here.
from django.db import models

# Create your models here.
# Aqui vai ser criado o seu modelo do banco de dados, as classes são as tabelas do banco.

# aqui vai me fornecer os registro do banco de dados para o model Couses.
# nesse caso ele está indo p banco e procurando se na tabela name e na tabela slug, possui o que eu digitei no campo do shell:
# exemplo Courses.objects.search('python') --> Aqui eu busco dentro da minha tabela courses, oq tem escrito python nas tabelas mencionadas acima
# class CourseManager(models.Manager):
#     def search(self,query):
#         return self.get_queryset().filter(
#            models.Q(name__icontains=query) &
#            #models.Q(description__icontains=query) | 
#            models.Q(slug__icontains=query)
#             )
        
    

class Home(models.Model):
    # Legenda dos campos:
    # name = models.CharField('Nome', max_length=100)
    # name: campo que vai ficar na tabela; CharField: Campo do tipo char que será identificado na tabela;
    # ('Nome', max_length=100): quer dizer que o verbose name desse campo é "Nome" e com no maximo 100 caracteres.
    # OBS: Se não for usado o verbose name automaticamente o sistema irá atribuir como o nome da variavel, que nesse caso é "name"
    
    name = models.CharField('Nome', max_length=100)

    
    #para ter o CourseManager como gerenciador é necessário utilizar esse comando
    #objects = CourseManager()''
    
    # Aqui vai transformar o meu objeto que está as tabelas em string, e assim tirar disso:
    # Courses.object(4) para isso Logica de Programação
    def __str__(self):
        return self.name
    
    class Meta:
        # verbose name é uma forma de tornar o campo mais bonito
        # verbose name é um atributo somente usado na classe Meta, caso utilize outra classe ali, o atributo não funcionará
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['name']