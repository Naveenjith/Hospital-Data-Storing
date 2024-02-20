from django.shortcuts import redirect, render

from doctor.models import doctor1

# Create your views here.
def register(request):
    if request.method=='POST':
        obj=doctor1()
        obj.Fname=request.POST.get('Fname')
        obj.Lname=request.POST.get('Lname')
        obj.Age=request.POST.get('Age')
        obj.Adress=request.POST.get('Adress')
        obj.Email=request.POST.get('email')
        obj.Experiance=request.POST.get('Experiance')

        obj.save()
    return render(request,"doc.html")

def doctorview(request):
    obj=doctor1.objects.all()
    return render(request,'docview.html',{'data':obj})

def updatedoct(request,dk):
    obj=doctor1.objects.get(id=dk)
    if request.method=='POST':
        obj=doctor1.objects.get(id=dk)
        obj.Fname=request.POST.get('Fname')
        obj.Lname=request.POST.get('Lname')
        obj.Age=request.POST.get('Age')
        obj.Adress=request.POST.get('Adress')
        obj.Email=request.POST.get('Email')
        obj.Experiance=request.POST.get('Experiance')

        obj.save()
        return redirect('viewdoct')
    return render(request,"updatedoc.html",{'data':obj})

def deletdoc(request,dk):
    obj=doctor1.objects.get(id=dk)
    obj.delete()
    return doctorview(request)