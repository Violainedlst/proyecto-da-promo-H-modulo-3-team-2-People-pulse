#Importamos las librerias necesarias
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from tkinter import messagebox as Msg


class DAO:
    def __init__(self):
        pass
    
    def creacion_bbdd_tablas(self,query,nombre_BBDD=None):
        
        if nombre_BBDD is not None:
                
            conexion =mysql.connector.connect(user = 'root',password='AlumnaAdalab',host='localhost',port='3306')
            cursor =conexion.cursor()
                
            try:
               cursor.execute(query)        
            except mysql.connector.Error as err:
                print(err)
                print("Error Code:", err.errno)
                print("SQLSTATE", err.sqlstate)
                print("Message", err.msg)
                           
            finally:
                cursor.close()
                conexion.close()
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
                
            finally:
                cursor.close()
                conexion.close()
            
                          
    def cargar_datos_BBDD (self,query,nombre_bbdd,lista_tuplas):
        
        conexion =mysql.connector.connect(user = 'root',password='AlumnaAdalab',host='localhost',port='3306',database=nombre_bbdd)
        cursor =conexion.cursor()
        
        try:
            cursor.executemany(query,lista_tuplas)    
            conexion.commit()
            Msg.showinfo("Info", f"{cursor.rowcount} Registros insertados") # título, mensaje
            # print(cursor.rowcount, "Registros insertados")
        
        except mysql.connector.Error as err:
                print(err)
                print("Error Code:", err.errno)
                print("SQLSTATE", err.sqlstate)
                print("Message", err.msg)
                
        finally:
                cursor.close()
                conexion.close()
             
    
        