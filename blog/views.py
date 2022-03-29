from django.shortcuts import render
from django.views.generic import TemplateView

class StudentView(TemplateView):
    template_name = 'index.html'

    def get(self,request,status=None):
        context = {

        }
        return render(request,self.template_name,context)
# Create your views here.
