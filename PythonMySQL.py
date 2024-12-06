import tkinter as tk




#importo los modulos restantes de tkinter
from tkinter import * 

from tkinter import ttk
from tkinter import messagebox

from Clientes import * 

from Conexion import * 

class FormularioClientes:

 global base
 base = None

 global texBoxId
 texBoId = None

 global texBoxNombres
 texBoxNombres = None

 global texBoxApellidos
 texBoxApellidos = None

 global combo 
 combo = None

 global groupBox
 groupBox = None

 global tree
 tree = None

from ttkbootstrap import Style
def Formulario():
  global texBoxId
  global texBoxNombres
  global texBoxApellidos
  global combo
  global base
  global groupBox
  global tree
  global texBoxDocumento
  global texBoxFechaNacimiento
  global texBoxTelefono
  global texBoxDomicilio
  
  
  try:
    style = Style(theme="superhero")  # Cambia el tema 
    base = style.master
    base.geometry("1900x300")
    base.title("Formulario Python")


    groupBox = LabelFrame(base,text="Datos del Personal",padx=5,pady=5)
    groupBox.grid(row=0,column=0,padx=10,pady=10)

    LabelId=Label(groupBox,text="Id:",width=13,font=("arial",12)).grid(row=0,column=0)
    texBoxId = Entry(groupBox)
    texBoxId.grid(row=0,column=1)

    LabelNombres=Label(groupBox,text="Nombres:",width=13,font=("arial",12)).grid(row=1,column=0)
    texBoxNombres = Entry(groupBox)
    texBoxNombres.grid(row=1,column=1)

    LabelApellidos=Label(groupBox,text="Apellidos:",width=13,font=("arial",12)).grid(row=2,column=0)
    texBoxApellidos = Entry(groupBox)
    texBoxApellidos.grid(row=2,column=1)

    LabelSexo=Label(groupBox,text="Sexo:",width=13,font=("arial",12)).grid(row=3,column=0)
    seleccionSexo = tk.StringVar()
    combo= ttk.Combobox(groupBox,values=["Masculino","Femenino"],textvariable=seleccionSexo)
    combo.grid(row=3,column=1)
    seleccionSexo.set("Masculino")

    LabelDocumento = Label(groupBox, text="Documento:", width=13, font=("arial", 12)).grid(row=4, column=0)
    texBoxDocumento = Entry(groupBox)
    texBoxDocumento.grid(row=4, column=1)

    LabelFechaNacimiento = Label(groupBox, text="Fecha Nac.:", width=13, font=("arial", 12)).grid(row=5, column=0)
    texBoxFechaNacimiento = Entry(groupBox)
    texBoxFechaNacimiento.grid(row=5, column=1)

    LabelTelefono = Label(groupBox, text="Teléfono:", width=13, font=("arial", 12)).grid(row=6, column=0)
    texBoxTelefono = Entry(groupBox)
    texBoxTelefono.grid(row=6, column=1)

    LabelDomicilio = Label(groupBox, text="Domicilio:", width=13, font=("arial", 12)).grid(row=7, column=0)
    texBoxDomicilio = Entry(groupBox)
    texBoxDomicilio.grid(row=7, column=1)





    ButtonGuardar = ttk.Button(groupBox, text="Guardar", bootstyle="success", width=15, command=guardarRegistros)
    ButtonGuardar.grid(row=9, column=0, pady=10, padx=5)

    ButtonModificar = ttk.Button(groupBox, text="Modificar", bootstyle="info", width=15, command=modificarRegistros)
    ButtonModificar.grid(row=9, column=1, pady=10, padx=5)

    ButtonEliminar = ttk.Button(groupBox, text="Eliminar", bootstyle="danger", width=15, command=eliminarRegistros)
    ButtonEliminar.grid(row=9, column=2, pady=10, padx=5)
    groupBox = LabelFrame(base,text="Lista del Personal",padx=5,pady=5,)
    groupBox.grid(row=0,column=1,padx=5,pady=5)
    #crea un Treeview

    #CONFIGURAR LAS COLUMNAS

    tree = ttk.Treeview(groupBox, columns=("Id", "Nombres", "Apellidos", "Sexo", "Documento", "Fecha Nac.", "Teléfono", "Domicilio"),show="headings", height=5)
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="Id")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="Nombre")
    tree.column("# 3", anchor=CENTER)
    tree.heading("# 3", text="Apelldio")
    tree.column("# 4", anchor=CENTER)
    tree.heading("# 4", text="Sexo")
    tree.column("# 5", anchor=CENTER, width=120)
    tree.heading("# 5", text="Documento")
    tree.column("# 6", anchor=CENTER, width=100)
    tree.heading("# 6", text="Fecha Nac.")
    tree.column("# 7", anchor=CENTER, width=100)
    tree.heading("# 7", text="Teléfono")
    tree.column("# 8", anchor=CENTER, width=150)
    tree.heading("# 8", text="Domicilio")
    


    #agrego los datos a la tabla
    #mostra la tabla
    for row in CClientes.mostrarClientes():
      tree.insert("","end",values=row)

      #ejecutar la funcion que hace click y mostrar el resultado(entry)

      tree.bind("<<TreeviewSelect>>",seleccionarRegistro)

    tree.pack()


    base.mainloop()

  except ValueError as error:
              print("Error al mostrar la interfaz, error: {}".format(error))

def guardarRegistros():
  
     global texBoxNombres, texBoxApellidos, combo, groupBox
     global texBoxDocumento, texBoxFechaNacimiento, texBoxTelefono, texBoxDomicilio


     try:
         #verificar si los wdgets estan inicializados 
         if not all([texBoxNombres, texBoxApellidos, combo, texBoxDocumento, texBoxFechaNacimiento, texBoxTelefono, texBoxDomicilio]):
             print("Los widgets no estan inicializados")
             return
         
         nombres = texBoxNombres.get()
         apellidos = texBoxApellidos.get()
         sexo = combo.get()
         documento = texBoxDocumento.get()
         fecha_nacimiento = texBoxFechaNacimiento.get()
         telefono = texBoxTelefono.get()
         domicilio = texBoxDomicilio.get()

         es_valido, mensaje_error = validarDomicilio(domicilio)
         if not es_valido:
            messagebox.showerror("Error", mensaje_error)
            return

         if not documento.isdigit():
            messagebox.showerror("Error", "El campo 'Documento' solo debe contener números.")
            return
         if not telefono.isdigit():
            messagebox.showerror("Error", "El campo 'Teléfono' solo debe contener números.")
            return

         CClientes.ingresarClientes(nombres,apellidos,sexo, documento, fecha_nacimiento, telefono, domicilio)
         messagebox.showinfo("Informacion","Los datos fueron guardados")

         actualizarTreeView()

         #limpio los campos
         texBoxNombres.delete(0,END)
         texBoxApellidos.delete(0,END)
         texBoxDocumento.delete(0, END)
         texBoxFechaNacimiento.delete(0, END)
         texBoxTelefono.delete(0, END)
         texBoxDomicilio.delete(0, END)

     except ValueError as error:
         print("Error al ingresar los datos: {}".format(error))
def actualizarTreeView():
    global tree 
    try:
        #borro todos los elemntos actuales del treeView
        tree.delete(*tree.get_children())
        #obtener los nuevos datos que deseamos mostrar
        #insertar los neuvos datos del treeView
        for row in CClientes.mostrarClientes():
         tree.insert("","end",values=row)
    except ValueError as error:
        print("Error al actualizar la tabla:{}".format(error))
        

def seleccionarRegistro(event):
    try: 
        #obtener el id del elemento seleccionado 
        itemSeleccionado = tree.focus()
        if itemSeleccionado:
            #obtengo los valores por columna 
            values = tree.item(itemSeleccionado)["values"]
            #establecer los valores en los widgets Entry 

            texBoxId.delete(0,END)
            texBoxId.insert(0,values[0])
            texBoxNombres.delete(0,END)
            texBoxNombres.insert(0,values[1])
            texBoxApellidos.delete(0,END)
            texBoxApellidos.insert(0,values[2])
            combo.set(values[3])
            texBoxDocumento.delete(0, END)
            texBoxDocumento.insert(0, values[4])

            texBoxFechaNacimiento.delete(0, END)
            texBoxFechaNacimiento.insert(0, values[5])

            texBoxTelefono.delete(0, END)
            texBoxTelefono.insert(0, values[6])

            texBoxDomicilio.delete(0, END)
            texBoxDomicilio.insert(0, values[7])

    except ValueError as error:
        print ("Error al selecionar registro{}".format(error))

   
    
def modificarRegistros():
  
     global texBoxId,texBoxNombres, texBoxApellidos, combo, groupBox
     global texBoxDocumento, texBoxFechaNacimiento, texBoxTelefono, texBoxDomicilio


     try:
         #verificar si los wdgets estan inicializados 
        if not all([texBoxId, texBoxNombres, texBoxApellidos, combo, texBoxDocumento, texBoxFechaNacimiento, texBoxTelefono, texBoxDomicilio]):
          print("Los widgets no estan inicializados")
          return
         
        idUsuario = texBoxId.get()
        nombres = texBoxNombres.get()
        apellidos = texBoxApellidos.get()
        sexo = combo.get()
        documento = texBoxDocumento.get()
        fecha_nacimiento = texBoxFechaNacimiento.get()
        telefono = texBoxTelefono.get()
        domicilio = texBoxDomicilio.get()

        CClientes.modificarClientes(idUsuario,nombres,apellidos,sexo, documento, fecha_nacimiento, telefono, domicilio)
        messagebox.showinfo("Informacion","Los datos fueron actualizados")

        actualizarTreeView()

         #limpio los campos
        texBoxId.delete(0,END)
        texBoxNombres.delete(0,END)
        texBoxApellidos.delete(0,END)
        texBoxDocumento.delete(0, END)
        texBoxFechaNacimiento.delete(0, END)
        texBoxTelefono.delete(0, END)
        texBoxDomicilio.delete(0, END)

     except ValueError as error:
         print("Error al modificar los datos: {}".format(error))


def eliminarRegistros():
  
     global texBoxId,texBoxNombres, texBoxApellidos


     try:
         #verificar si los wdgets estan inicializados 
         if texBoxId is None :
             print("Los widgets no estan inicializados")
             return
         
         idUsuario = texBoxId.get()
        
         CClientes.eliminarClientes(idUsuario)
         messagebox.showinfo("Informacion","Los datos fueron eliminados")

         actualizarTreeView()

         #limpio los campos
         texBoxId.delete(0,END)
         texBoxNombres.delete(0,END)
         texBoxApellidos.delete(0,END)

     except ValueError as error:
         print("Error al eliminar los datos: {}".format(error))
def validarDomicilio(domicilio):
    palabras = domicilio.split()  # Divide el texto en palabras
    cantidad_palabras = len(palabras)
    cantidad_numeros = sum(c.isdigit() for c in domicilio)  # Cuenta solo los números

    if cantidad_palabras > 30:
        return False, "El domicilio no puede tener más de 30 palabras."
    if cantidad_numeros > 10:
        return False, "El domicilio no puede tener más de 10 números."

    return True, ""
from ttkbootstrap import Style

style = Style(theme="superhero")  # Temas disponibles: flatly, darkly, superhero, etc.
base = style.master
from ttkbootstrap import Style


Formulario()  