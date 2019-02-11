from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .forms import NewNewFormForm, SecureForm
from .models import NewForm, Secure
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def track_cargo(request):
    return render(request, 'track.html')

@login_required(login_url='/accounts/login/')
def new_cargo(request):
    current_user = request.user
    # if request.method == 'POST':
    #     form = NewNewFormForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         newnewformform = form.save(commit=False)
    #         newnewformform .save()
    # else:
    form = NewNewFormForm()
    return render(request, 'new_cargo.html', {"form": form})

def newcargo(request):
    SenderName = request.POST.get('SenderName')
    SenderAddress = request.POST.get('SenderAddress')
    RecieverName = request.POST.get('RecieverName')
    RecieverAddress = request.POST.get('RecieverAddress')
    referenceID = request.POST.get('referenceID')
    GoodsareFrom = request.POST.get('GoodsareFrom')
    GoodsTo = request.POST.get('GoodsTo')
    DepatureDate = request.POST.get('DepatureDate')
    Depaturetime = request.POST.get('Depaturetime')
    ArrivalDate = request.POST.get('ArrivalDate')
    ArrivalTime = request.POST.get('ArrivalTime')
    GoodsDescription = request.POST.get('GoodsDescription')
    Status = request.POST.get('Status')

    recipient=NewForm(SenderName=SenderName, SenderAddress=SenderAddress, RecieverName=RecieverName, RecieverAddress=RecieverAddress, referenceID=referenceID, GoodsareFrom=GoodsareFrom, GoodsTo=GoodsTo, DepatureDate=DepatureDate, Depaturetime=Depaturetime, ArrivalDate=ArrivalDate, ArrivalTime=ArrivalTime, GoodsDescription=GoodsDescription, Status=Status)
    recipient.save()
    data = {'success': 'Cargo Posted'}
    return JsonResponse(data)

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
        return redirect('/')
    return render(request, 'update_cargo.html', {'form': form})

def newSecure(request):
    current_user = request.user
    form = SecureForm()
    return render(request, 'new_secure.html', {"form":form})

def new_secure(request):
    DepositorName = request.POST.get('DepositorName')
    ReceiverName = request.POST.get('ReceiverName')
    TrackNo = request.POST.get('TrackNo')
    Origin = request.POST.get('Origin')
    Destination = request.POST.get('Destination')
    TypeOfShipment = request.POST.get('TypeOfShipment')
    NatureOfGoods = request.POST.get('NatureOfGoods')
    Status = request.POST.get('Status')

    recipient=Secure(DepositorName=DepositorName, ReceiverName=ReceiverName, TrackNo=TrackNo, Origin=Origin, Destination=Destination, TypeOfShipment=TypeOfShipment, NatureOfGoods=NatureOfGoods, Status=Status)
    recipient.save()
    data = {'success': 'Secure Cargo Posted'}
    return JsonResponse(data)

def secure(request):
    sec = Secure.objects.all()
    return render(request, 'secure.html',{"sec":sec})

def update_secure(request, pk):
    instance = get_object_or_404(Secure, pk=pk)
    form = SecureForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update_cargo.html', {'form': form})

def track_secure(request):
    return render(request, 'track_secure.html')


def search_secure(request):

    if 'TrackNo' in request.GET and request.GET["TrackNo"]:
        search_term = request.GET.get("TrackNo")
        secure_ref = Secure.search_by_TrackNo(search_term)
        message = f"{search_term}"

        return render(request, 'secure_result.html',{"message":message,"TrackNo":secure_ref})

    else:
        message = "You haven't searched for any term"
        return render(request, 'secure_result.html',{"message":message})
