from django.shortcuts import redirect, render
from django.views.decorators import csrf
from .models import Cliente,Producto,Compra
from .forms import ClienteForm,ProductoForm,CustomUserCreationForm, CompraForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import permission_required
from django.contrib import messages

def index(request):
    return render (request, 'index.html')

def quienessomos(request):
    return render(request, 'quienessomos.html')

def galeria(request):
    return render(request, 'galeria.html')

def formulario(request):
    return render (request, 'formulario.html')

def apiferiados(request):
    return render(request, 'apiferiados.html')

def apiclientes(request):
    return render(request, 'apiclientes.html')

def mensaje(request):
    return render(request, 'mensaje.html')

@permission_required('app.add_cliente')
def mostrar(request):
    clientes= Cliente.objects.all()
    datos={
        'clientes': clientes
    }
    return render(request, 'mostrar.html',datos)

@permission_required('app.add_producto')
def mostrar2(request):
    productos= Producto.objects.all()
    datos={
        'productos': productos
    }
    return render(request, 'mostrar2.html',datos)

def mostrar3(request):
    compras= Compra.objects.all()
    datos={
        'compras': compras
    }
    return render(request, 'mostrar3.html',datos)

def forms_clientes(request):
    if request.method=='POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect('mostrar')
    else:
        cliente_form= ClienteForm()
    return render(request, 'forms_clientes.html', {'cliente_form': cliente_form})


def form_mod_cliente(request, id):
    cliente = Cliente.objects.get(rut=id)
    datos ={
        'form': ClienteForm(instance=cliente)
    }
    if request.method=='POST':
        formulario = ClienteForm(data = request.POST, instance=cliente)
        if formulario.is_valid: 
            formulario.save()
            return redirect('mostrar')
    return render(request, 'form_mod_cliente.html', datos)


def form_del_cliente(request, id):
    cliente = Cliente.objects.get(rut=id)
    cliente.delete()
    return redirect('mostrar')

def forms_productos(request):
    if request.method=='POST':
        producto_form = ProductoForm(request.POST, files=request.FILES)
        if producto_form.is_valid():
            producto_form.save()
            return redirect('mostrar2')
    else:
        producto_form= ProductoForm()
    return render(request, 'forms_productos.html', {'producto_form': producto_form})


def form_mod_producto(request, id):
    producto = Producto.objects.get(idprod=id)
    datos ={
        'form': ProductoForm(instance=producto)
    }
    if request.method=='POST':
        formulario = ProductoForm(data = request.POST, files=request.FILES,instance=producto)
        if formulario.is_valid: 
            formulario.save()
            return redirect('mostrar2')
    return render(request, 'form_mod_producto.html', datos)

def form_del_producto(request, id):
    producto = Producto.objects.get(idprod=id)
    producto.delete()
    return redirect('mostrar2')

def forms_compras(request):
    if request.method=='POST':
        compra_form = CompraForm(request.POST)
        if compra_form.is_valid():
            compra_form.save()
            return redirect('galeria')
    else:
        compra_form= CompraForm()
    return render(request, 'forms_compras.html', {'compra_form': compra_form})

def form_mod_compra(request, id):
    compra = Compra.objects.get(idorden=id)
    datos ={
        'form': CompraForm(instance=compra)
    }
    if request.method=='POST':
        formulario = CompraForm(data = request.POST, files=request.FILES,instance=compra)
        if formulario.is_valid: 
            formulario.save()
            return redirect('mostrar3')
    return render(request, 'form_mod_compra.html', datos)

def form_del_compra(request, id):
    compra = Compra.objects.get(idorden=id)
    compra.delete()
    return redirect('mostrar3')


def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente!")
            #redirigir al home
            return redirect(to="index")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)

# Create your views here.
