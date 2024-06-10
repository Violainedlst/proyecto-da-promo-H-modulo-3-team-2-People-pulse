from os import stat
from tkinter import * 
from tkinter import ttk,Toplevel, Frame, Label, Button
from tkinter import messagebox as Msg
from tkinter import filedialog as FileDialog
from PIL import Image, ImageTk
from Fase05_Creación_de_una_ETL.Conexion import  DAO
import Fase05_Creación_de_una_ETL.queries as qu
import pandas as pd
import numpy as np
import subprocess
import os



class Ventana(Frame): #Clase ventana de tipo frame
    
    dao=DAO()
    
    def __init__(self, master=None):
        super().__init__(master,width=1000,height=400,bg="#040452")
        self.master=master
        self.pack(expand=True, fill="both")
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
    
    def convertir_int(self,lista_tuplas):
        datos_tabla=[]
        for tupla in lista_tuplas:
            lista_intermedia=[]
            for elemento in tupla:
                try:
                   
                    lista_intermedia.append(int(elemento))
                except:
                    lista_intermedia.append(elemento)
        
            datos_tabla.append(tuple(lista_intermedia))
        return datos_tabla   
    
    def fCargarDatos(self):
        
      csv =r"D:\Repositorios Adalab\proyecto-da-promo-H-modulo-3-team-2-People-pulse\CSVs\HR_RAW_DATA_LIMPIO.csv"
      df =pd.read_csv(csv,index_col=0)
      df.fillna('n/a', inplace=True)
      
           
      datos_tabla_employees= list(df[['employee_number', 'age','gender','year_birth','marital_status','attrition']].itertuples(index=False, name=None))     
      datos_tabla_employees_details= list(df[["employee_number","department","job_role","remote_work","distance_from_home","overtime","business_travel","stock_option_level"]].itertuples(index=False, name=None))
      datos_tabla_education= list(df[["employee_number","education","education_field"]].itertuples(index=False, name=None))
      datos_tabla_salaries = list(df[["employee_number","monthly_income","monthly_rate","hourly_rate","percent_salary_hike"]].itertuples(index=False, name=None))
      datos_tabla_satisfaction = list(df[["employee_number","environment_satisfaction","job_involvement","job_satisfaction","relationship_satisfaction","work_life_balance"]].itertuples(index=False, name=None))
      datos_tabla_cv_details = list(df[["employee_number","num_companies_worked","training_times_last_year","total_working_years","years_at_company","years_since_last_promotion","years_with_curr_manager"]].itertuples(index=False, name=None))
        
      datos_tabla_employees=self.convertir_int(datos_tabla_employees)
      datos_tabla_employees_details=self.convertir_int(datos_tabla_employees_details)
      datos_tabla_education=self.convertir_int(datos_tabla_education)
      datos_tabla_salaries=self.convertir_int(datos_tabla_salaries)
      datos_tabla_satisfaction=self.convertir_int(datos_tabla_satisfaction)
      datos_tabla_cv_details=self.convertir_int(datos_tabla_cv_details)
      
      self.dao.cargar_datos_BBDD(qu.query_insertar_employees,'abc_corporation',datos_tabla_employees)
      self.dao.cargar_datos_BBDD(qu.query_insertar_employees_details,'abc_corporation',datos_tabla_employees_details) 
      self.dao.cargar_datos_BBDD(qu.query_insertar_education,'abc_corporation',datos_tabla_education) 
      self.dao.cargar_datos_BBDD(qu.query_insertar_salaries,'abc_corporation',datos_tabla_salaries) 
      self.dao.cargar_datos_BBDD(qu.query_insertar_satisfaction,'abc_corporation',datos_tabla_satisfaction) 
      self.dao.cargar_datos_BBDD(qu.query_insertar_cv_details,'abc_corporation',datos_tabla_cv_details)
         
             
    def fInformeResultadospdf(self):
        ruta_pdf = r"Fase06_Reporte_Resultados\InformeAnalisisAbcCorporation.pdf"  # Cambia esto por la ruta de tu archivo PDF
        try:
            if os.name == 'nt':  # Para sistemas Windows
                os.startfile(ruta_pdf)
            elif os.name == 'posix':  # Para sistemas Unix (Linux, macOS)
                subprocess.call(('open', ruta_pdf) if sys.platform == 'darwin' else ('xdg-open', ruta_pdf))
        except Exception as e:
            print(f"Error al abrir el archivo PDF: {e}")
            
    def fInformeResultadosppt (self):
        ruta_pptx = r"Fase06_Reporte_Resultados\ManualdeUsuario.pptx"  # Cambia esto por la ruta de tu archivo PDF
        try:
            if os.name == 'nt':  # Para sistemas Windows
                os.startfile(ruta_pptx)
            elif os.name == 'posix':  # Para sistemas Unix (Linux, macOS)
                subprocess.call(('open', ruta_pptx) if sys.platform == 'darwin' else ('xdg-open', ruta_pptx))
        except Exception as e:
            print(f"Error al abrir el archivo PPT: {e}")
      
    # Falta implementación, se hará en versión 2.0      
    
    '''def fmostrar_frame_mantenimiento(self):
        # Esconder otros frames si es necesario
        for widget in self.winfo_children():
            if widget != self.frame_mantenimiento:
                widget.place_forget()
                
        # Mostrar el frame de mantenimiento de empleados
        self.frame_mantenimiento.place(x=0, width=200, height=399)
                
    
    def falta_empleado(self):
        self.dao.mantenimiento_empleados(qu.query_insertar_employees,'abc_corporation',employees)
        
    def fbaja_empleado(self):
        Msg.showinfo("Baja", "Baja de empleado")
        self.dao.mantenimiento_empleados(qu.query_baja_employees,'abc_corporation',employees)
        
    def fmodificar_empleado(self):
        Msg.showinfo("Modificar", "Modificar empleado")
        self.dao.mantenimiento_empleados(qu.query_modificar_employees,'abc_corporation',employees)
        
    def feliminar_empleado(self):
        self.dao.mantenimiento_empleados(qu.query_borrar_employees,'abc_corporation',employees)
        Msg.showinfo("Eliminar", "Eliminar empleado")'''
        
    # FIN FALTA IMPLENTACION
    
    def crear_widgets(self):
       
        #primer cuadro de la izq
        frame1=Frame(self, bg="#040452")
        #frame1.place(x=0,y=0)
        frame1.pack(side="top", fill="y")
        
        # Frame para botones en horizontal
        botones_frame = Frame(frame1, bg="#040452")
        botones_frame.pack(side="top", padx=20)
        
        #Boton Nueva BBDD
        self.btnNuevaBBDD=Button(frame1,text="Crear BBDD y Tablas",command=self.fNuevaBBDDyTablas, bg="#3D3681", fg="white")
        self.btnNuevaBBDD.pack(side="left", padx=10, pady=60)
        
        
        #Boton CargarDatos
        self.btnCargarDatos=Button(frame1,text="Cargar Datos",command=self.fCargarDatos, bg="#3D3681", fg="white")
        self.btnCargarDatos.pack(side="left", padx=10, pady=10)
        
        #Boton AnalisisDeDatos
        self.btnAnalisisDatos=Button(frame1,text="Informe Resultados ",command=self.fInformeResultadospdf, bg="#3D3681", fg="white")
        self.btnAnalisisDatos.pack(side="left", padx=10, pady=10)
        
        #Boton ManualUsuario
        self.btnManual=Button(frame1,text="Manual de Usuario ",command=self.fInformeResultadosppt, bg="#3D3681", fg="white")
        self.btnManual.pack(side="left", padx=10, pady=10)
              
        #Boton Nuevo, falta implementar en la versión 2.0
        
        #self.btnMantenimiento=Button(frame1,text="Mantenimiento empleados",command=self.fmostrar_frame_mantenimiento, bg="#3D3681", fg="white")
        #self.btnMantenimiento.place(x=15,y=200,width=150,height=40) 
        
        #FIN DE FALTA IMPLEMENTACION.
              
        #El frame 2 con la imagen de la empresa
        
        #frame2=Frame(self, bg="#040452")
        #frame2.pack(side="right", expand=True, fill="both")
        #frame2.place(x=200,width=800,height=399)
         
        # Cargar la imagen
        self.image_path=r"images\logo_ABC.png"
        self.image = Image.open(self.image_path)
        self.photo = ImageTk.PhotoImage(self.image)
        
        # Crear un label para la imagen y centrarlo
        self.logo_label = Label(self, image=self.photo,bg="#040452")
        self.logo_label.place(relx=0.5, rely=0.5, anchor="center")
        
        '''self.logo_label.pack(expand=True)
        self.logo_label.pack_propagate(False)
        self.logo_label.update_idletasks()
        self.logo_label.pack(anchor="center")'''
        
      # Frame para el mantenimiento de empleados, se implementará en la versión 2.0
        '''self.frame_mantenimiento = Frame(self, bg="#040452")
          
        self.boton_alta = Button(self.frame_mantenimiento, text="Alta", command=self.falta_empleado, bg="#3D3681", fg="white")
        self.boton_alta.place(x=15, y=50, width=150, height=40)
        
        self.boton_baja = Button(self.frame_mantenimiento, text="Baja", command=self.fbaja_empleado, bg="#3D3681", fg="white")
        self.boton_baja.place(x=15, y=100, width=150, height=40)
        
        self.boton_modificar = Button(self.frame_mantenimiento, text="Modificar", command=self.fmodificar_empleado, bg="#3D3681", fg="white")
        self.boton_modificar.place(x=15, y=150, width=150, height=40)'''
       
     