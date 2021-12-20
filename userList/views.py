from django.core import paginator
from django.shortcuts import get_object_or_404, redirect, render
from .models import FullUser
from .forms import UserForm
from django.contrib import messages
from django.core.paginator import Paginator

# Lista de usuários
def listUser_view(request):
    
    fullName = request.GET.get("fullName")
    cpf = request.GET.get('cpf')
    age = request.GET.get('age')
    address = request.GET.get('address')

    users = FullUser.objects.all()
    
    if fullName is not None:
        users = users.filter(fullName__id=fullName)
    if cpf is not None:
        users = users.filter(cpf__id = cpf)
    if age is not None:
        users = users.filter(age__id=cpf)
    if address is not None:
        users = users.filter(address__id=address)
        
    
        
    context = {
        'users': users
    }
    
    return render(request, template_name='home/list.html',  context=context, status=200)

#Adicionando usuario
def addUser_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.info(request, 'Usuário adicionado com sucesso!')
            return redirect('/')
        else:
            return redirect('/')
    else:
        form = UserForm()
        context = {
            'form': form
        }
        return render(request, template_name='home/adduser.html', context=context, status=200)
    
#ver dados dos usuários

def userView(request, id):
    users = FullUser.objects.filter(id=id)
        
    
    context = {
        'users': users,
    }
    return render(request, template_name='home/users.html', context=context, status=200)