from django.shortcuts import render, redirect
from inscrire_etudiant.forms import StudentsForm
from inscrire_etudiant.models import Students


# Create your views here.
def std(request):
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
             try:
                 form.save()
                 return redirect('/view')
             except:
                 pass
    else:
        form = StudentsForm()
    return render(request,'index.html',{'form':form})

def view(request):
    inscrire_etudiant = Students.objects.all()
    return render(request,"view.html",{'inscrire_etudiant':inscrire_etudiant})

def delete(request, id):
    inscrire_etudiant = Students.objects.get(id=id)
    inscrire_etudiant.delete()
    return redirect("/view")