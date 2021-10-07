from django.http.request import HttpRequest
from django.views.generic.base import View
from django.http import HttpResponse
from django.shortcuts import render

class HelloWorld(View):
    def get(self, request):
        data ={'name':'Manuel García Negrete',
               'years':33,
               'codes':['Python', 'Java','.Net']}
        return render(request,'hello_world.html', context=data)
    
    
class Inicio(View):
      def get(self, request):
          return render(request,'index.html')
    