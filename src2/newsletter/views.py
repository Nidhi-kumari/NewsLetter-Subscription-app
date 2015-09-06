from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.

def home(request):
    title="Welcome"
    
    form=SignUpForm(request.POST or None)
    context={
    "title":title,
    "form":form,
    }
    #if request.user.is_authenticated():
        #title="my title %s" %(request.user)
   # if request.method = 'POST':
    #    print request.POST  
    if form.is_valid():
        instance=form.save(commit=False)
        if not instance.full_name:
            full_name='nidhi'
        instance.save()
        print instance.email 
        print instance.timestamp 
        
        context={
        "title":"Thank you"
        }    
   
    return render(request,"home.html",context)
