from django.shortcuts import redirect, render

from patient.models import patient1

# Create your views here.
def register2(request):
    if request.method=='POST':
        obj=patient1()
        obj.Fname=request.POST.get('Fname')
        obj.Lname=request.POST.get('Lname')
        obj.Age=request.POST.get('Age')
        obj.Adress=request.POST.get('Adress')
        obj.Email=request.POST.get('email')
        obj.Disease=request.POST.get('Disease')

        obj.save()
    return render(request,'pat.html')

def patientview(request):
    obj=patient1.objects.all()
    return render(request,'patview.html',{'data':obj})

def patupdate(request,TK):
    obj=patient1.objects.get(id=TK)
    if request.method=='POST':
        obj=patient1.objects.get(id=TK)
        obj.Fname=request.POST.get('Fname')
        obj.Lname=request.POST.get('Lname')
        obj.Age=request.POST.get('Age')
        obj.Adress=request.POST.get('Adress')
        obj.Email=request.POST.get('email')
        obj.Disease=request.POST.get('Disease')
        obj.save()
        return redirect('viewpat')
    return render(request,"updatepat.html",{'datas':obj})

def deletpat(request,TK):
    obj=patient1.objects.get(id=TK)
    obj.delete()
    return patientview(request)