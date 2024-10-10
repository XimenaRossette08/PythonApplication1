
###Formulario de registro 
## almacenamiento en TXT sin validación 
import tkinter as tk 
from tkinter import messagebox
import re ## Libreria de Expresiones Regulares
import mysql.connector #para conectar mysql 
### Definicion de funciones 

def insertarRegistro(nombres, apellidos, edad, estatura, telefono, genero):
    try: 
        conexion = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root", 
            password="", 
            database="programacion"
        ) 
        cursor = conexion.cursor()
        
        query = "INSERT INTO registros (nombre, apellidos, edad, estatura, telefono, genero) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (nombres, apellidos, edad, estatura, telefono, genero)
        
        cursor.execute(query, valores)
        conexion.commit()
        cursor.close()
        conexion.close()
        messagebox.showinfo("Informacion", "Datos guardados en la base de datos con exito.")
    except mysql.connector.Error as err: 
        messagebox.showerror("Error", f"Error al insertar los datos: {err}") 
        
def limpiar_campos():
    tbNombre.delete(0,tk.END)
    tbApellidos.delete(0,tk.END)
    tbEdad.delete(0,tk.END)
    tbEstatura.delete(0,tk.END)
    tbTelefono.delete(0,tk.END)
    var_genero.set(0)
    
def es_entero_valido(valor):
    try: 
        int(valor)
        return True
    except ValueError: 
        return False
    
def es_decimal_valido(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False 

def es_entero_valido_de_10_digitos(valor):
    return valor.isdigit()and len (valor) == 10


def es_texto_valido (valor):
    return bool(re.match("^[a-zA-Z\s]+$", valor))
def borrar_fun():
    limpiar_campos()
def guardar_valores():
 #Obtener valores desde los entrys 
 nombres= tbNombre.get()
 apellidos = tbApellidos.get()
 edad = tbEdad.get()
 estatura = tbEstatura.get()
 telefono = tbTelefono.get()

 genero = ""
 if var_genero.get() == 1:
        genero = "Hombre"
 elif var_genero.get() == 2:
        genero = "Mujer"
       
    # Validación de formatos 
 if (es_entero_valido(edad) and 
        es_decimal_valido(estatura) and 
        es_entero_valido_de_10_digitos(telefono) and 
        es_texto_valido(nombres) and 
        es_texto_valido(apellidos)):
        
        # Generar cadena de caracteres
        datos = "Nombres: " + nombres + "\n" + "Apellidos: " + apellidos +"\n" + "Edad: " + edad +"\n" "Estatura: " + estatura +"\n" +"Telefono: " + telefono + "\n" + "Genero: " + genero + "\n"
    
        # Guardar los datos en el archivo TXT
        with open("Python.txt", "a") as archivo:
            archivo.write(datos + "\n\n")
            insertarRegistro(nombres, apellidos, edad, estatura, telefono, genero)
            messagebox.showinfo("Informacion", "Datos guardados con exito: \n\n" + datos)
            limpiar_campos()
 else: 
        # Mensaje de error en caso de validación fallida
        messagebox.showinfo("ERROR", "Los datos contienen formatos no validos:\n\n")
    
 tbNombre.delete(0,tk.END)
 tbApellidos.delete(0,tk.END)
 tbEdad.delete(0,tk.END)
 tbEstatura.delete(0,tk.END) 
 tbTelefono.delete(0,tk.END)
 var_genero.set(0)
 
##Creacion de ventana
ventana = tk.Tk()
ventana.geometry("520x500")
ventana.title("Formulario Vr.01")
#Crear variable para el RadioButton 
var_genero = tk.IntVar()

##Creacion de etiquetas y campos de entrada
lbNombre = tk.Label(ventana, text= "Nombres: ")
lbNombre.pack()
tbNombre = tk.Entry()
tbNombre.pack()
lbApellidos = tk.Label(ventana, text= "Apellidos: ")
lbApellidos.pack()
tbApellidos = tk.Entry()
tbApellidos.pack()
lbTelefono = tk.Label(ventana, text= "Telefono: ")
lbTelefono.pack()
tbTelefono = tk.Entry()
tbTelefono.pack()
lbEdad = tk.Label(ventana, text= "Edad: ")
lbEdad.pack()
tbEdad = tk.Entry()
tbEdad.pack()
lbEstatura = tk.Label(ventana, text= "Estatura: ")
lbEstatura.pack()
tbEstatura = tk.Entry()
tbEstatura.pack()
lbGenero = tk.Label(ventana, text= "Genero")
lbGenero.pack()
rbHombre=tk.Radiobutton(ventana, text="Hombre", variable=var_genero, value=1)
rbHombre.pack()
rbMujer=tk.Radiobutton(ventana, text="Mujer", variable=var_genero, value=2)
rbMujer.pack()
#Creacion de Botones 
btnBorrar = tk.Button(ventana, text = "Borrar valores", command= borrar_fun)
btnBorrar.pack()
btnGuardar = tk.Button(ventana, text = "Guardar", command= guardar_valores)
btnGuardar.pack()
#Ejecucion de ventana 
ventana.mainloop()

