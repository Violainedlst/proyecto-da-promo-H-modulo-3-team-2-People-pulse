from tkinter import *
from tkinter import ttk 
from ventana import *

#Inicializamos nuestra primera ventana

def main():
    root=Tk() #crear objeto del tipo Tk
    root.wm_title("ABC Corporation")
    app=Ventana(root) #Creamos una clase de tipo ventana.
    app.mainloop()
   
    
if __name__ == '__main__':
    main()