from django.shortcuts import render,redirect
from . models import AboutMe,GraductionEducation,SchoolEducation,Contact,Project,Post,Service,Blog,Skil,Hobbie
from django.contrib import messages

# Create your views here.
def Home(request):
    work=Post.objects.all()
    post=Blog.objects.all()
    skl=Skil.objects.all()

    context={"works":work,"posts":post,"skls":skl}
    return render(request,'home.html',context)


def service(request):
    ser=Service.objects.all
    context={"sers":ser}
    return render(request,'service.html',context)


"""def mcontact(request):
    if request.method=="POST":
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fphoneno=request.POST.get('num')
        fdesc=request.POST.get('desc')
        query=Contact(name=fname,email=femail,num=fphoneno,description=fdesc)
        query.save()
        messages.success(request,"Thanks for contacting us. We will get by you Soon!")

        return redirect('/contact')

    return render(request,'contact.html')"""

"""def mcontact(request):
    if request.method == "POST":
        fname = request.POST.get('name')
        femail = request.POST.get('email')
        fphoneno = request.POST.get('num')
        fdesc = request.POST.get('desc')
        query = Contact(name=fname, email=femail, phonenumber=fphoneno, description=fdesc)
        query.save()
        messages.success(request, "Thanks for contacting us. We will get back to you soon!")

        return redirect('/contact/')

    return render(request, 'contact.html')"""


def mcontact(request):
    if request.method == "POST":
        fname = request.POST.get('name')
        femail = request.POST.get('email')
        fphoneno = request.POST.get('num')
        fdesc = request.POST.get('desc')
        
        #print(f"Name: {fname}, Email: {femail}, Phone: {fphoneno}, Description: {fdesc}")
        
        
        query = Contact(name=fname, email=femail, phonenumber=fphoneno, description=fdesc)
        query.save()
        messages.success(request, "Thanks for contacting us. We will get back to you soon!")

        return redirect('/contact/')

    return render(request, 'contact.html')

def projects(request):
    obj=Project.objects.all()
    context={"objs":obj}
    return render(request,'project.html',context)
        