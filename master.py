from tkinter import *
from tkinter import ttk 
from ventana import *

def main():
    root=Tk() #crear objeto del tipo Tk
    root.wm_title("Crud Tkinter y Mysql")
    app=Ventana(root)
    app.mainloop()
    
    
if __name__ == '__main__':
    main()