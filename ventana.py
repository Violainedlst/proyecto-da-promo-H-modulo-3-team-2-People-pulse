from os import stat
from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from conexion import  DAO
import queries as qu

class Ventana(Frame): #Clase ventana de tipo frame
    
    dao=DAO()
    
    def __init__(self, master=None):
        super().__init__(master,width=1000,height=400)
        self.master=master
        self.pack()
        self.crear_widgets() #creamos todos los controles
   
      
        
    #Todas las funciones del crud y Botonoes, Eventos Etc
    
    #Cargar Datos en el Grid

    def abrir_ventana_secundaria(self):
        # Crear una ventana secundaria.
        ventana_secundaria = Toplevel()
        ventana_secundaria.title("Spolier Alert!!!")
        ventana_secundaria.config(width=300, height=200)
        
        
        # Crear un botón dentro de la ventana secundaria
        # para cerrar la misma.
        boton_aceptar = ttk.Button(
            ventana_secundaria,
            text="Aceptar", 
            command=ventana_secundaria.destroy
        )
        boton_aceptar.place(x=75, y=75)
        ventana_secundaria.focus()

       
    def fNuevaBBDDyTablas(self):  
      
      self.dao.creacion_bbdd_tablas(qu.query_creacion_bbdd)
          
    def fNuevo(self):  
       pass    
     
    def fCancelar(self):
       pass

    def fMantenimientoEmpleados(self):
       pass
    
    def fAnalisisDatos(self):
        top = Toplevel()
        top.title("Analisis de datos")
        top.geometry("1000x400")
        #primer cuadro de la izq
        frame3=Toplevel(self, bg="#8A86B2")
     
    
    
    def crear_widgets(self):
        #primer cuadro de la izq
        frame1=Frame(self, bg="#8A86B2")
        frame1.place(x=0,y=0,width=200,height=399)
        
        #Boton Nuevo
        self.btnNuevaBBDD=Button(frame1,text="Crear BBDD y Tablas",command=self.fNuevaBBDDyTablas, bg="#3D3681", fg="white")
        self.btnNuevaBBDD.place(x=15,y=100,width=150,height=40)    
              
        #Boton Nuevo
        self.btnMantenimiento=Button(frame1,text="Mantenimiento empleados",command=self.fMantenimientoEmpleados, bg="#3D3681", fg="white")
        self.btnMantenimiento.place(x=15,y=175,width=150,height=40) 
        
        #Boton Nuevo
        self.btnAnalisisDatos=Button(frame1,text="Analisis de datos",command=self.fAnalisisDatos, bg="#3D3681", fg="white")
        self.btnAnalisisDatos.place(x=15,y=250,width=150,height=40) 
        

        #el frame 2 con la imagen de la empresa
        
        frame2=Frame(self, bg="#040452")
        frame2.place(x=200,width=800,height=399)
        
         # Cargar la imagen
        self.image = Image.open("logo_ABC.png")
        self.photo = ImageTk.PhotoImage(self.image)
        
        # Crear un label para la imagen y centrarlo
        self.logo_label = Label(self, image=self.photo)
        self.logo_label.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        