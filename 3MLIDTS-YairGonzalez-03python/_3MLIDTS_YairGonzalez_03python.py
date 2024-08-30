## 3MLIDTS-YairGonzalez-03Python
### Formulario de registro 
## almacenamiento en TXT sin validación
import tkinter as tk
from tkinter import messagebox
### Definición de funciones
def limpiar_campos():
    tbNombre.delete(0,tk.END)
    tbApellidos.delete(0,tk.END)
    tbEdad.delete(0,tk.END)
    tbEstatura.delete(0,tk.END)
    tbTelefono.delete(0,tk.END)
    var_genero.set(0)
def borrar_fun():
    limpiar_campos()
def guardar_valores():
    #Obtener valores desde los entrys
    nombres= tbNombre.get()
    apellidos = tbApellidos.get()
    edad = tbEdad.get()
    estatura = tbEstatura.get()
    telefono= tbTelefono.get()
    ### Obtener el genero de los RadioButtons
    genero =""
    if var_genero.get()==1:
        genero= "Hombre"
    elif var_genero.get()==2:
        genero="Mujer"
    ### Generar la cadena de caracteres
    datos = "Nombres: "+ nombres +"\n"+"Apellidos: "+ apellidos +"\n"+"Edad: "+ edad +"años\n"+"Estatura: "+ estatura +"\n"+"Telefonos :"+ telefono +"\n"+"Genero: "+genero+"\n"
    ## Guardar los datos en el archivo TXT
    with open("C:\\Users\\ygbal\\Source\\Repos\\3N2024Datos.txt", "a") as archivo:
        archivo.write(datos+"\n\n")
    ###Mostrar mensaje de confirmacón
    messagebox.showinfo("Información", "Datos guardados con éxito: \n\n"+datos)
    borrar_fun()

## Creación de Vetana
ventana = tk.Tk()
ventana.geometry("520x500")
ventana.title("Formulario Vr.01")
#Crear variable para el RadioButton
var_genero = tk.IntVar()

## Creación de etiquetas y campos de entrada
lbNombre= tk.Label(ventana, text="Nombres :")
## Pack es el tercer metodo de ordenamiento de elementos graficos en python 
#(1er- Place, 2do - Grid)
# Ordenamiento por lista de aparicion
lbNombre.pack()
tbNombre = tk.Entry()
tbNombre.pack()
lbApellidos= tk.Label(ventana, text="Apellidos :")
lbApellidos.pack()
tbApellidos = tk.Entry()
tbApellidos.pack()
lbTelefono= tk.Label(ventana, text="Telefono :")
lbTelefono.pack()
tbTelefono = tk.Entry()
tbTelefono.pack()
lbEdad= tk.Label(ventana, text="Edad :")
lbEdad.pack()
tbEdad = tk.Entry()
tbEdad.pack()
lbEstatura= tk.Label(ventana, text="Estatura :")
lbEstatura.pack()
tbEstatura = tk.Entry()
tbEstatura.pack()
lbGenero=tk.Label(ventana, text="Genero")
lbGenero.pack()
rbHombre=tk.Radiobutton(ventana, text="Hombre", variable=var_genero, value=1)
rbHombre.pack()
rbMujer=tk.Radiobutton(ventana, text="Mujer", variable=var_genero, value=2)
rbMujer.pack()
##Creación de Botones
btnBorrar = tk.Button(ventana, text = "Borrar valores", command=borrar_fun)
btnBorrar.pack()
btnGuardar = tk.Button(ventana, text = "Guardar", command=guardar_valores)
btnGuardar.pack()
## Ejecución de ventana
ventana.mainloop()