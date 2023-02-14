#Librerías a importar:
from tkinter import *

from PdfManager import PdfManager

#Inicializando tk
root= Tk()
root.geometry("630x700+400+100")
root.title("PDF Manager")
root.configure(bg = "white")

#instanciamos el gestor.
pdf_manager = PdfManager()

#Botón Abrir Archivos.
of= Button(root, text="Abrir archivo/s", command= pdf_manager.buscarArchivos, width=40, font="arial 20", bd=4)
of.pack()

#Botón Unir Archivos.
mf= Button(root, text="Unir archivos", command= pdf_manager.unirArchivos, width=40, font="arial 20", bd=4)
mf.pack()


root.mainloop()