#Importamos las librerias necesarias
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import pandas as pd
import numpy as np
import requests
import re
import os

class DAO:
    def __init__(self):
        try:
         self.conexion =mysql.connector.connect(user = 'root',password='AlumnaAdalab',host='localhost',database='abc_corporation',port='3306')
         
         #print(self.conexion)
        
        except Error as ex:
            print("Error al intentar la conexión con la base de datos {0}".format(ex))
          
            
    def crear_BBDD(self):
        
            nombre_BBDD = 'abc_corporation'                 
            try:
                cursor =self.conexion.cursor()
                
                sql = "CREATE DATABASE {}".format(nombre_BBDD)
                
                #sql = "CREATE DATABASE %s"
                
                cursor.execute(sql)
                
                self.conexion.commit()
                
                print ("Base de datos creado correctamente")
                          
            except Error as ex:
                
                print("Error al crear la base de datos: {0}".format(ex))
    
    # Creamos las tablas
              
    def crear_Tablas(self):
        
        self.conexion.database = 'abc_corporation'
        
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()               
            
                # Crear la tabla si no existe
                sql = "CREATE TABLE IF NOT EXISTS XXXXXXXX ()"
                cursor.execute(sql)
                self.conexion.commit()
                print("Tabla  creada correctamente")
                               
            except Error as ex:
                print("Error al crear la tabla: {0}".format(ex))
                
                
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

