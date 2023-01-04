from django.shortcuts import render,HttpResponse


# Create your views here.
def saludo(request):
    mensaje = "Bienvenidos a nuestro examen final de LP3 2022-II"
    return render(request,'inicio.html',
    {'mensaje': mensaje })

def alumnos(request):
    alumnos = [ 'Baldeon FIgueroa Jhon Percy' , 
                'Granados Esteban Adrian Eduardo' , 
                'Huaman Simeon Victor Raul']
    return render(request,'integrantes.html', 
    {'alumnos': alumnos,
        'titulo': 'LOS INTEGRANTES SON: '})



	

