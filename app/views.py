from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .forms import NewNewFormForm
from .models import NewForm
from django.db import transaction
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')

def track_cargo(request):
    return render(request, 'track.html')

@login_required(login_url='/accounts/login/')
def new_cargo(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewNewFormForm(request.POST, request.FILES)
        if form.is_valid():
            newnewformform = form.save(commit=False)
            newnewformform .save()
    else:
        form = NewNewFormForm()
    return render(request, 'new_cargo.html', {"form": form})

def search_results(request):

    if 'referenceID' in request.GET and request.GET["referenceID"]:
        search_term = request.GET.get("referenceID")
        searched_ref = NewForm.search_by_referenceID(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"referenceID":searched_ref})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def cargo_list(request ):
    scoty = NewForm.objects.all()
    print(scoty)
    return render(request,'cargo.html',{"scoty":scoty})

def service(request):
    return render(request, 'service.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def update_cargo(request, pk):
    instance = get_object_or_404(NewForm, pk=pk)
    form = NewNewFormForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('next_view')
    return render(request, 'update_cargo.html', {'form': form})
