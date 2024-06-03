#Importamos las librerias necesarias
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from tkinter import messagebox
import queries as qu
import pandas as pd
import numpy as np
import requests
import re
import os

class DAO:
    def __init__(self):
        pass
    
    def creacion_bbdd_tablas(self,query,nombre_BBDD=None):
     
        if nombre_BBDD is not None:
                
            conexion =mysql.connector.connect(user = 'root',password='AlumnaAdalab',host='localhost',port='3306')
            cursor =conexion.cursor()
                
            try:
               cursor.execute(query)
              
               messagebox.showinfo("Spoiler Alert!!!!","Base de datos creada correctamente") # título, mensaje 
               
            except mysql.connector.Error as err:
               messagebox.showerror("Spoiler Alert!!!!", f"Error de conexión: {err.msg}")
            
            #finally:
                #cursor.close()
                #conexion.close()
        else:
            conexion =mysql.connector.connect(user = 'root',password='AlumnaAdalab',host='localhost',port='3306',database=nombre_BBDD)
            cursor=conexion.cursor()
            try:
                cursor.execute(query)               
                
            except mysql.connector.Error as err:
                print(err)
                print("Error Code:", err.errno)
                print("SQLSTATE", err.sqlstate)
                print("Message", err.msg)
            
                          
    def cargar_datos_BBDD (self):
             
        # Cambiar a la base de datos especificada
        
        self.conexion.database = 'abc_corporation'
        
        #Metemos los datos deL CSV
        
        url =""  #Desde esta url obtenemos el csv de donde extraemos los datos.
        
        data_empresa =pd.read_csv(url)
     
        
        #data_empresa.info()
             
        #data_empresa
                
        # Sacar los df para cada una de las tablas del df principal
        
        # Sub-DataFrame para la tabla Empleados
        
        df_empleados = df_empleados[['id_employee', 'name', 'date_birth', 'gender', 'marital_status', 'number_children']]
        
        lista_empleados=[tuple(i) for i in df_empleados.values]         
        
        if self.conexion.is_connected():
            
           mycursor = self.conexion.cursor()
           
            
           sql = "INSERT INTO xxxxxxx () VALUES (%s, %s, %s, %s,%s,%s)" 

                           
           #peliculas el nombre del archivo correspondiente
           
           try:
                mycursor.executemany(sql, lista_empleados)
                self.conexion.commit()
                print(mycursor.rowcount,"empleados dados de alta")
           except mysql.connector.Error as err:
                print("Ha habido un error en la inserción")
                print(err)
