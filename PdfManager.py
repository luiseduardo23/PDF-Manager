from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger, PdfReader

class PdfManager:
    #Variable dir, la cual contendrá una tupla con las direcciones de los archivos en formato PDF
    rutas = ()

    'Clase para los métodos de gestión de PDF' #Descripción
    def __init__(self):
        pass

    def abrirPDF(self):
        return None
        
    def buscarArchivos(self):
        ruta_archivos= filedialog.askopenfilenames(initialdir="/",
                                                    title="Selecciona el archivo PDF",
                                                    filetype=(("PDF File", ".pdf"),
                                                              ("PDF File", ".PDF"),
                                                              ("All file", ".txt")))
        self.rutas = ruta_archivos
    
    def guardarArchivo(self):
        output= filedialog.asksaveasfilename(initialdir="/",
                                            title="Guardar PDF como:",
                                            defaultextension= ".pdf",
                                            filetype=(("PDF File", ".pdf"),
                                                      ("PDF File", ".PDF"),
                                                      ("All file", ".txt")))
        return output
        
    def unirArchivos(self):
        
        union = PdfMerger()

        if(self.rutas==() or self.rutas==""):
            messagebox.showinfo("Error en la unión:",  "No has abierto los archivos")
            return None
        
        #unimos las rutas
        for ruta in self.rutas:
            if(not ruta.endswith('.pdf')):
                messagebox.showinfo("Error en los archivos",  "Alguno de los archivos seleccionados no es valido")
                return None
            else:
                union.append(PdfReader(ruta))

        ruta_de_guardado = self.guardarArchivo()

        union.write(ruta_de_guardado)
        messagebox.showinfo("Unión finalizada",  "Se han unido los archivos exitosamente.")