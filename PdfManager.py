from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger, PdfReader, PdfWriter

import os

class PdfManager:
    #Variable dir, la cual contendrá una tupla con las direcciones de los archivos en formato PDF
    rutas = ()
    num_archivos= 0

    'Clase para los métodos de gestión de PDF' #Descripción
    def __init__(self):
        pass
        
    def buscarArchivos(self):
        ruta_archivos= filedialog.askopenfilenames(initialdir="/",
                                                    title="Selecciona el archivo PDF",
                                                    filetype=(("PDF File", ".pdf"),
                                                              ("PDF File", ".PDF"),
                                                              ("All file", ".txt")))
        self.rutas = ruta_archivos
        self.num_archivos = len(ruta_archivos)
    
    def guardarArchivo(self):
        output= filedialog.asksaveasfilename(initialdir="/",
                                            title="Guardar PDF como:",
                                            defaultextension= ".pdf",
                                            filetype=(("PDF File", ".pdf"),
                                                      ("PDF File", ".PDF"),
                                                      ("All file", ".txt")))
        return output
    
    def seleccionarCarpeta(self):
        output= filedialog.askdirectory(initialdir="/",
                                            title="Seleccione la carpeta de guardado:")
        return output
        
    def unirArchivos(self):
            
        union = PdfMerger()

        if(self.num_archivos==0):
            messagebox.showinfo("Error en la unión:",  "No has abierto los archivos")
            return None
        
        #unimos las rutas
        for ruta in self.rutas:
            if(not ruta.endswith('.pdf')):
                messagebox.showinfo("Error en los archivos",  "Alguno de los archivos seleccionados no es valido.")
                return None
            else:
                union.append(PdfReader(ruta))

        ruta_de_guardado = self.guardarArchivo()

        union.write(ruta_de_guardado)
        messagebox.showinfo("Unión finalizada",  "Se han unido los archivos exitosamente.")

    def dividirArchivo(self, num_pagina):
        archivo_pdf1= PdfWriter()
        archivo_pdf2= PdfWriter()

        if(self.num_archivos!=1):
            messagebox.showinfo("Error en la Operación:",  
                                "Solo se puede dividir un PDF a la vez y actualmente tiene "+ str(self.num_archivos) +" archivos abiertos.")
            return None
        
        if(not self.rutas[0].endswith('.pdf')):
            messagebox.showinfo("Error en el archivo",  "El archivo seleccionado no es valido.")
            return None

        pdf_reader = PdfReader(self.rutas[0])

        if(len(pdf_reader.pages)<num_pagina):
            messagebox.showinfo("Error en la Operación",  "El archivo seleccionado tiene menos páginas que el número de página especificado anteriormente.")
            return None

        #Separando el PDF en dos archivos        
        for pagina in range(num_pagina):
            archivo_pdf1.add_page(pdf_reader.pages[pagina])

        for pagina in range(num_pagina, len(pdf_reader.pages)):
            archivo_pdf2.add_page(pdf_reader.pages[pagina])

        #Guardando los archivos separados:
        ruta_de_guardado = self.seleccionarCarpeta()
        nombreBase =os.path.basename(self.rutas[0])
        nombreBase = nombreBase.split('.')[0]

        with open(ruta_de_guardado + "/" + nombreBase + str(1) +".pdf", 'wb') as file1:
            archivo_pdf1.write(file1)
        with open(ruta_de_guardado + "/" + nombreBase + str(2) +".pdf", 'wb') as file2:
            archivo_pdf2.write(file2)

        messagebox.showinfo("División finalizada",  "Se ha dividido el archivo exitosamente en dos partes.")