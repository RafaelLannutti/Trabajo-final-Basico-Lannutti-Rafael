from tkinter import messagebox, Label, Tk, StringVar, CENTER, ttk
import tkinter as tk
def convertir_celsius_a_fahrenheit():
    try:
        celsius = float(rectangulo_entrada.get())
        fahrenheit = celsius * 9/5 + 32
        resultado_valor.set(f"{fahrenheit:.2f}°f") 
    except ValueError:
        messagebox.showerror("Error", "Entrada no válida. Ingrese un número.")

def convertir_fahrenheit_a_celsius():
    try:
        fahrenheit = float(rectangulo_entrada.get())
        celsius = (fahrenheit - 32) * 5/9
        resultado_valor.set(f"{celsius:.2f}°C")
    except ValueError:
        messagebox.showerror("Error", "Entrada no válida. Ingrese un número.")
def no_escribas():
    return False


ventana = tk.Tk()
ventana.geometry("400x200")
ventana.config(background="lightblue")
ventana.resizable(False,False)
ventana.title("Convertidor de temperatura")


entrada_valor = StringVar()
resultado_valor =StringVar()

titulo =ttk.Label(ventana,text= "Convertidor de Temperatura", font=("Arial",20),background="lightblue")
titulo.grid(row=0,columnspan=4,padx=20,pady=10,sticky=("n"))
sub_titulo =ttk.Label(ventana,text="Ingrese su temperatura",background="lightblue",foreground="black")
sub_titulo.grid(row=1,)
rectangulo_entrada = ttk.Entry(ventana, textvariable= entrada_valor ) #rectangulo de ingreso de numeros
rectangulo_entrada.grid (row=4,column=0,ipadx=20,ipady=0)
rectangulo_salida = ttk.Entry(ventana, state="readonly")#textvariable= resultado_valor,validate="key",validatecommand= no_escribas) #Rectangulo de salida de numeros
rectangulo_salida.grid (row=4,column=2,ipadx=20,ipady=0)
boton_convertir_cel_far = ttk.Button(ventana, text="Convertir a Fahrenheit",command=convertir_celsius_a_fahrenheit) #Boton cel a Far
boton_convertir_cel_far.grid(row=5,column=0,ipadx=10,ipady=0)
boton_convertir_far_cel = ttk.Button(ventana,text = "Convertir a Celsius",command=convertir_fahrenheit_a_celsius) #Boton far a cel
boton_convertir_far_cel.grid(row=5,column=2,ipadx=10,ipady=0)



ventana.mainloop()