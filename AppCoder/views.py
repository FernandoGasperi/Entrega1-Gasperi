from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso, Profesor, Estudiante
from .forms import CrearCursoForm, CrearProfesorForm, CrearEstudianteForm

# Create your views here.
def mostrar_curso(request):
    curso = Curso(nombre='Python', comision='34635')

    saludo = f'Hola a la todos, este es el curso de {curso.nombre}, con numero de comision: {curso.comision}'

    return HttpResponse(saludo)
    #return render(request, '', {'nombre': curso.nombre, 'comision': curso.comision})

def mostrar_index(request):

    return render(request, 'index.html')


def mostrar_referencias(request):

    return render(request, 'referencias.html')


def mostrar_repaso(request):

    return render(request, 'repaso.html')


def crear_curso(request):

    if request.method == "POST":
        
        formulario = CrearCursoForm(request.POST)
        if formulario.is_valid():
            
            formulario_limpio = formulario.cleaned_data
        
            curso = Curso (nombre=formulario_limpio["nombre"], comision=formulario_limpio["comision"])
        
            curso.save()

            return render(request, "index.html")

    else:
        formulario = CrearCursoForm()


    return render(request, 'crear_curso.html', {'formulario':formulario})


def crear_profesor(request):

    if request.method == "POST":

        formulario = CrearProfesorForm(request.POST)
        if formulario.is_valid():
            
            formulario_limpio = formulario.cleaned_data
        
            profesor = Profesor (nombre=formulario_limpio["nombre"], apellido=formulario_limpio["apellido"],email=formulario_limpio["email"], profesion=formulario_limpio["profesion"])
        
            profesor.save()

            return render(request, "index.html")
        
    else:
        formulario = CrearProfesorForm()


    return render(request, "crear_profesor.html",{'formulario': formulario})



def crear_estudiante(request):

    if request.method == "POST":
        
        formulario = CrearEstudianteForm(request.POST)
        if formulario.is_valid():
            
            formulario_limpio = formulario.cleaned_data
        
            estudiante=Estudiante(nombre=formulario_limpio["nombre"],apellido=formulario_limpio["apellido"],email=formulario_limpio["email"])
        
            estudiante.save()

            return render(request, "index.html")

    else:
        formulario = CrearEstudianteForm()


    return render(request, 'crear_estudiante.html', {'formulario':formulario})



def buscar_comision(request):

    if request.GET.get("comision", False):
        comision = request.GET["comision"]
        cursos = Curso.objects.filter(comision__icontains=comision)

        return render(request, "buscar_comision.html", {'cursos': cursos})

    else:
        respuesta = "No hay datos"


    return render(request, "buscar_comision.html",{"respuesta" : respuesta})




def buscar_profesor(request):

    if request.GET.get("email", False):
        email = request.GET["email"]
        profesors = Profesor.objects.filter(email__icontains=email)

        return render(request, "buscar_profesor.html",{'profesors': profesors})

    else:
        respuesta = "No hay datos"


    return render(request, "buscar_profesor.html",{"respuesta": respuesta})



def buscar_estudiante(request):

    if request.GET.get("apellido", False):
        apellido = request.GET["apellido"]
        estudiantes = Estudiante.objects.filter(apellido__icontains=apellido)

        return render(request, "buscar_estudiante.html",{'estudiantes': estudiantes})

    else:
        respuesta = "No hay Estudiante"


    return render(request, "buscar_estudiante.html",{"respuesta": respuesta})