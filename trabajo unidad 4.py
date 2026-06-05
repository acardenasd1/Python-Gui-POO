#Aqui solucioné un error que me daba, al ejecutar cualquier libreria de python, en este caso Tkinter
import os
os.environ['TCL_LIBRARY']='C:/Users/Anibal/AppData/Local/Programs/Python/Python313/tcl/tcl8.6'
os.environ['TK_LIBRARY']='C:/Users/Anibal/AppData/Local/Programs/Python/Python313/tcl/tcl8.6'

from tkinter import *

class vehiculo:
    def __init__(self, tipo, nombre, marca):
        self.tipo = tipo
        self.nombre = nombre
        self.marca = marca
    def cilindraje(self):
        pass
    def velocidadMaxima(self):
        pass
    def precio(self):
        pass
class Mt09(vehiculo):
    def cilindraje(self):
        return 'Cilindraje: 890 cc'
    def velocidadMaxima(self):
        return 'Velocidad Maxima: 250 Km/h'
    def precio(self):
        return 'Precio: 57.500.000 Millones'
class HondaCivic(vehiculo):
    def cilindraje(self):
        return 'Cilindraje: 1996 cc'
    def velocidadMaxima(self):
        return 'Velocidad Maxima: 272 Km/h'
    def precio(self):
        return 'Precio: 240.000.000 Millones'
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Vehículos")
        self.root.geometry("800x800")
   
        self.moto = Mt09("Moto", "MT-09", "Yamaha")
        self.auto = HondaCivic("Auto", "Civic", "Honda")

        self.img_moto = PhotoImage(file="C:/Users/Anibal/Desktop/MT-09.png")
        self.img_auto = PhotoImage(file="C:/Users/Anibal/Desktop/Civic.png")

        self.boton_moto = Button(self.root, text="Mostrar MT-09", command=self.mostrarMt)
        self.boton_moto.pack(pady=10)

        self.boton_auto = Button(self.root, text="Mostrar Honda Civic", command=self.mostrarCivic)
        self.boton_auto.pack(pady=10)

        self.info_label = Label(self.root, text="", justify=LEFT)
        self.info_label.pack(pady=10)

        self.img_label = Label(self.root)
        self.img_label.pack()

    def mostrarMt(self):
        info = f"{self.moto.nombre} ({self.moto.tipo}):\n{self.moto.cilindraje()}\n{self.moto.velocidadMaxima()}\n{self.moto.precio()}"
        self.info_label.config(text=info)
        self.img_label.config(image=self.img_moto)

    def mostrarCivic(self):
        info = f"{self.auto.nombre} ({self.auto.tipo}):\n{self.auto.cilindraje()}\n{self.auto.velocidadMaxima()}\n{self.auto.precio()}"
        self.info_label.config(text=info)
        self.img_label.config(image=self.img_auto)

root = Tk()
app = App(root)
root.resizable(False, False)
root.iconbitmap("C:/Users/Anibal/Desktop/logo.ico")
root.mainloop()
