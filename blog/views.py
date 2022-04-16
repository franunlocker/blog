from multiprocessing import context
from re import template
from tokenize import Name
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Curso, Estudiante, Profesor
from django.http import HttpResponse
from django.template import loader


class FormularioView(TemplateView):
    template_name ='form.html'
    def post(self,request):
        nombre = request.POST['nombre']
        camada = request.POST['camada']        
        obj_curso= Curso(nombre=nombre, camada=camada)
        obj_curso.save()
        return render(request,self.template_name)

    def post(self,request):
        name = request.POST['name']
        lastname = request.POST['lastname']    
        age = request.POST['age']   
        email = request.POST['email']       
        obj_estudiante= Estudiante(name=name, age=age, email=email)
        obj_estudiante.save()
        return render(request,self.template_name)   

    def post(self,request):
        name = request.POST['name']
        lastname = request.POST['lastname']    
        age = request.POST['age']                
        obj_estudiante= Profesor(name=name, lastname=lastname, age=age)
        obj_estudiante.save()
        return render(request,self.template_name)       

class SearchView(TemplateView):
    template_name ='search.html'

    def post(self,request):       
        context = {
            "elements": Curso.objects.filter(camada=request.POST.get('camada'))
            
        }

        return render(request,self.template_name,context)

class StudentView(TemplateView):
    template_name = 'index.html'

    def get(self,request,status=None):
        context = {

        }
        return render(request,self.template_name,context)

""" class ListView(TemplateView):
    template_name = 'lista.html'    
    cursos = Curso.objects.all()
    print(cursos)

    def get(self,request,status=None):
        context = {
            'cursos': Curso,
        }
        return render(request,self.template_name,context)

 """
def listado_curso(request):
        template = loader.get_template('lista.html')
        cursos = Curso.objects.all()
        print(cursos)
        context = {
        'curso' : cursos,
         }
        return HttpResponse(template.render(context,request))
# Create your views here.
