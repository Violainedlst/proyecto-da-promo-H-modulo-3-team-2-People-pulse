from os import stat
from tkinter import * 
from tkinter import ttk
from tkinter import messagebox as Msg
from PIL import Image, ImageTk
from conexion import  DAO
import queries as qu
import pandas as pd
import numpy as np

class Ventana(Frame): #Clase ventana de tipo frame
    
    dao=DAO()
    
    def __init__(self, master=None):
        super().__init__(master,width=1000,height=400)
        self.master=master
        self.pack()
        self.crear_widgets() #creamos todos los controles
   
      
        
    #Todas las funciones del crud y Botonoes, Eventos Etc
    
    #Cargar Datos en el Grid
    
    

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
        
      url ="https://raw.githubusercontent.com/Violainedlst/proyecto-da-promo-H-modulo-3-team-2-People-pulse/main/HR%20RAW%20DATA%20FINAL.csv"
      df =pd.read_csv(url)
      
      datos_tabla_employees= list(set(zip(df["employee_number"].values,df["age"].values,df["gender"].values,df["year_birth"].values,df["marital_status"].values,df["attrition"].values)))
      datos_tabla_employees_details= list(set(zip(df["employee_number"].values,df["department"].values,df["job_role"].values,df["remote_work"].values,df["distance_from_home"].values,df["overtime"].values,df["business_travel"].values,df["stock_option_level"].values)))
      datos_tabla_education= list(set(zip(df["employee_number"].values,df["education"].values,df["education_field"].values)))
      datos_tabla_salaries = list(set(zip(df["employee_number"].values,df["monthly_income"].values,df["monthly_rate"].values,df["hourly_rate"].values,df["percent_salary_hike"].values)))
      datos_tabla_satisfaction = list(set(zip(df["employee_number"].values,df["environment_satisfaction"].values,df["job_involvement"].values,df["job_satisfaction"].values,df["relationship_satisfaction"].values,df["work_life_balance"].values)))
      datos_tabla_cv_details = list(set(zip(df["employee_number"].values,df["num_companies_worked"].values,df["training_times_last_year"].values,df["total_working_years"].values,df["years_at_company"].values,df["years_since_last_promotion"].values,df["years_with_curr_manager"].values)))
      self.dao.cargar_datos_BBDD(qu.query_insertar_employees,'abc_corporation',datos_tabla_employees)   
         
    def fNuevo(self):  
       pass    
     
    def fCancelar(self):
       pass

    def fMantenimientoEmpleados(self):
       pass
    
    def fAnalisisDatos(self):
       ventana_analisis=Toplevel(self, bg="#8A86B2")
       ventana_analisis.geometry("1000x400")
       
       boton1 = ttk.Button(ventana_analisis, text="boton1", command='')
        
     
    
    
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
        self.btnMantenimiento=Button(frame1,text="Mantenimiento empleados",command=self.fMantenimientoEmpleados, bg="#3D3681", fg="white")
        self.btnMantenimiento.place(x=15,y=200,width=150,height=40) 
        
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
        
  
        
         
     