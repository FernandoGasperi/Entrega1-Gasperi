from django import forms

class CrearCursoForm(forms.Form):

    nombre = forms.CharField()
    comision = forms.IntegerField()


class CrearProfesorForm(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField(max_length=40)
    profesion = forms.CharField()


class CrearEstudianteForm(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField(max_length=40)
    