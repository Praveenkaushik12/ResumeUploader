from django.shortcuts import render,HttpResponse
from .forms import ResumeForm
from django.views import View
from .models import ResumeData
from django.views.generic import TemplateView

# Create your views here.
class HomeView(View):
    def get(self,request):
        form=ResumeForm()
        candidates=ResumeData.objects.all()
        return render(request,'resume/home.html',{'form':form,'candidates':candidates})
    
    def post(self,request):
        if request.method=='POST':
            fm=ResumeForm(request.POST,request.FILES)
            if fm.is_valid():
                fm.save()
            return HttpResponse("Submitted!")
        
class Candidate(View):
    def get(self,request,id):
        candidate=ResumeData.objects.get(pk=id)
        return render(request,'resume/candidate.html',{'candidate':candidate})