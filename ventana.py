from os import stat
from tkinter import * 
from tkinter import ttk,Toplevel, Frame, Label, Button
from tkinter import messagebox as Msg
from tkinter import filedialog as FileDialog
from PIL import Image, ImageTk
from conexion import  DAO
import queries as qu
import pandas as pd
import numpy as np
import convertir_int32
import subprocess
import os



class Ventana(Frame): #Clase ventana de tipo frame
    
    dao=DAO()
    
    def __init__(self, master=None):
        super().__init__(master,width=1000,height=400)
        self.master=master
        self.pack()
        self.crear_widgets() #creamos todos los controles
   
       

    def test(self):
        Msg.showinfo("Info", "Base de datos y tablas creadas correctamente") # título, mensaje
         
    def fNuevaBBDDyTablas(self):  
      
      self.dao.creacion_bbdd_tablas(qu.query_creacion_bbdd)
      self.dao.creacion_bbdd_tablas(qu.query_creacion_tabla_employees,'abc_corporation')
      self.dao.creacion_bbdd_tablas(qu.query_creacion_tabla_employees_details,'abc_corporation')
      self.dao.creacion_bbdd_tablas(qu.query_creacion_tabla_education,'abc_corporation')
      self.dao.creacion_bbdd_tablas(qu.query_creacion_tabla_salaries,'abc_corporation')
      self.dao.creacion_bbdd_tablas(qu.query_creacion_tabla_satisfaction,'abc_corporation')
      self.dao.creacion_bbdd_tablas(qu.query_creacion_tabla_cv_details,'abc_corporation')
      self.test()
    
    
    def fCargarDatos(self):
        
      csv ="HR_RAW_DATA_FINAL.csv"
      df =pd.read_csv(csv,index_col=0)
      print(df.info())
      
      
      
      '''columnas_convertidas = ["hourly_rate","work_life_balance","age","daily_rate","distance_from_home","education", "employee_number", "environment_satisfaction", "job_involvement", "job_level", "job_satisfaction", "monthly_rate", "num_companies_worked", "percent_salary_hike", "relationship_satisfaction", "stock_option_level", "training_times_last_year", "total_working_years","years_at_company", "years_since_last_promotion", "years_with_curr_manager", "year_birth"]
      for col in columnas_convertidas:
             df[col] = df[col].apply(lambda x: x.item())'''
      
      datos_tabla_employees= list(set(zip(df["employee_number"].values,df["age"].values,df["gender"].values,df["year_birth"].values,df["marital_status"].values,df["attrition"].values)))
      datos_tabla_employees_details= list(set(zip(df["employee_number"].values,df["department"].values,df["job_role"].values,df["remote_work"].values,df["distance_from_home"].values,df["overtime"].values,df["business_travel"].values,df["stock_option_level"].values)))
      datos_tabla_education= list(set(zip(df["employee_number"].values,df["education"].values,df["education_field"].values)))
      datos_tabla_salaries = list(set(zip(df["employee_number"].values,df["monthly_income"].values,df["monthly_rate"].values,df["hourly_rate"].values,df["percent_salary_hike"].values)))
      datos_tabla_satisfaction = list(set(zip(df["employee_number"].values,df["environment_satisfaction"].values,df["job_involvement"].values,df["job_satisfaction"].values,df["relationship_satisfaction"].values,df["work_life_balance"].values)))
      datos_tabla_cv_details = list(set(zip(df["employee_number"].values,df["num_companies_worked"].values,df["training_times_last_year"].values,df["total_working_years"].values,df["years_at_company"].values,df["years_since_last_promotion"].values,df["years_with_curr_manager"].values)))  
      
      self.dao.cargar_datos_BBDD(qu.query_insertar_employees,'abc_corporation',datos_tabla_employees)
      self.dao.cargar_datos_BBDD(qu.query_insertar_employees_details,'abc_corporation',datos_tabla_employees_details) 
      self.dao.cargar_datos_BBDD(qu.query_insertar_education,'abc_corporation',datos_tabla_education) 
      self.dao.cargar_datos_BBDD(qu.query_insertar_salaries,'abc_corporation',datos_tabla_salaries) 
      self.dao.cargar_datos_BBDD(qu.query_insertar_satisfaction,'abc_corporation',datos_tabla_satisfaction) 
      self.dao.cargar_datos_BBDD(qu.query_insertar_cv_details,'abc_corporation',datos_tabla_cv_details)    
         
    def fNuevo(self):  
       pass    
     
    def fCancelar(self):
       pass

    def fMantenimientoEmpleados(self):
       pass
    
    def fInformeResultados(self):
        ruta_pdf = "InformeAnalisis.pdf"  # Cambia esto por la ruta de tu archivo PDF
        try:
            if os.name == 'nt':  # Para sistemas Windows
                os.startfile(ruta_pdf)
            elif os.name == 'posix':  # Para sistemas Unix (Linux, macOS)
                subprocess.call(('open', ruta_pdf) if sys.platform == 'darwin' else ('xdg-open', ruta_pdf))
        except Exception as e:
            print(f"Error al abrir el archivo PDF: {e}")
      
        
    def fmostrar_frame_mantenimiento(self):
        # Esconder otros frames si es necesario
        for widget in self.winfo_children():
            if widget != self.frame_mantenimiento:
                widget.place_forget()
                
        # Mostrar el frame de mantenimiento de empleados
        self.frame_mantenimiento.place(x=0, width=200, height=399)
                
        
    def falta_empleado(self):
        Msg.showinfo("Alta", "Alta de empleado")
        
    def fbaja_empleado(self):
        Msg.showinfo("Baja", "Baja de empleado")
        
    def fmodificar_empleado(self):
        Msg.showinfo("Modificar", "Modificar empleado")
        
    def feliminar_empleado(self):
        Msg.showinfo("Eliminar", "Eliminar empleado")
    
    def crear_widgets(self):
       
        #primer cuadro de la izq
        frame1=Frame(self, bg="#8A86B2")
        frame1.place(x=0,y=0,width=200,height=399)
        
        #Boton Nuevo
        self.btnNuevaBBDD=Button(frame1,text="Crear BBDD y Tablas",command=self.fNuevaBBDDyTablas, bg="#3D3681", fg="white")
        self.btnNuevaBBDD.place(x=15,y=100,width=150,height=40)
        
        #Boton Nuevo
        self.btnNuevaBBDD=Button(frame1,text="Cargar Datos",command=self.fCargarDatos, bg="#3D3681", fg="white")
        self.btnNuevaBBDD.place(x=15,y=150,width=150,height=40)    
              
        #Boton Nuevo
        self.btnMantenimiento=Button(frame1,text="Mantenimiento empleados",command=self.fmostrar_frame_mantenimiento, bg="#3D3681", fg="white")
        self.btnMantenimiento.place(x=15,y=200,width=150,height=40) 
        
        #Boton Nuevo
        self.btnAnalisisDatos=Button(frame1,text="Informe Resultados ",command=self.fInformeResultados, bg="#3D3681", fg="white")
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
        
      # Frame para el mantenimiento de empleados
        self.frame_mantenimiento = Frame(self, bg="#040452")
          
        self.boton_alta = Button(self.frame_mantenimiento, text="Alta", command=self.falta_empleado, bg="#3D3681", fg="white")
        self.boton_alta.place(x=15, y=50, width=150, height=40)
        
        self.boton_baja = Button(self.frame_mantenimiento, text="Baja", command=self.fbaja_empleado, bg="#3D3681", fg="white")
        self.boton_baja.place(x=15, y=100, width=150, height=40)
        
        self.boton_modificar = Button(self.frame_mantenimiento, text="Modificar", command=self.fmodificar_empleado, bg="#3D3681", fg="white")
        self.boton_modificar.place(x=15, y=150, width=150, height=40)
        
        self.boton_eliminar = Button(self.frame_mantenimiento, text="Eliminar", command=self.feliminar_empleado, bg="#3D3681", fg="white")
        self.boton_eliminar.place(x=15, y=200, width=150, height=40) 
        
  
     