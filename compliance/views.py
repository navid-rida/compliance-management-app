from django.shortcuts import render,redirect
from django.http import Http404
from .models import Branches
#from .models import BranchesForm
from .forms import BranchesForm




def index(request):
    branch_list = Branches.objects.all()
    context = {'branch_list': branch_list}
    return render(request, 'compliance/showbranch.html', context)

def createbranch(request):
    #branch = Branches()
    if request.method == 'POST':
        form = BranchesForm(request.POST)
        if form.is_valid():
            branch = form.save(commit=False)
            branch.save()
            return redirect('index')
    else:
        form = BranchesForm()
    return render(request, 'compliance/createbranch.html', {'form' : form})
