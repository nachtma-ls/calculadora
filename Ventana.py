import tkinter as tk

# Función para realizar operaciones matemáticas
def calcular():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if operacion.get() == "+":
            resultado = num1 + num2
        elif operacion.get() == "-":
            resultado = num1 - num2
        elif operacion.get() == "*":
            resultado = num1 * num2
        elif operacion.get() == "/":
            resultado = num1 / num2
        else:
            resultado = "Operación no válida"
        label_resultado.config(text=resultado)
    except:
        label_resultado.config(text="Error: números no válidos")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.iconbitmap("icono.ico")

# Crear los widgets
label_num1 = tk.Label(ventana, text="Primer número:")
entry_num1 = tk.Entry(ventana)

label_num2 = tk.Label(ventana, text="Segundo número:")
entry_num2 = tk.Entry(ventana)

label_operacion = tk.Label(ventana, text="Operación:")
operacion = tk.StringVar(value="+")
radio_suma = tk.Radiobutton(ventana, text="+", variable=operacion, value="+")
radio_resta = tk.Radiobutton(ventana, text="-", variable=operacion, value="-")
radio_multiplicacion = tk.Radiobutton(ventana, text="*", variable=operacion, value="*")
radio_division = tk.Radiobutton(ventana, text="/", variable=operacion, value="/")

boton_calcular = tk.Button(ventana, text="Calcular", command=calcular)
label_resultado = tk.Label(ventana, text="Resultado")

# Ubicar los widgets en la ventana
label_num1.grid(row=0, column=0)
entry_num1.grid(row=0, column=1)

label_num2.grid(row=1, column=0)
entry_num2.grid(row=1, column=1)

label_operacion.grid(row=2, column=0)
radio_suma.grid(row=2, column=1)
radio_resta.grid(row=2, column=2)
radio_multiplicacion.grid(row=2, column=3)
radio_division.grid(row=2, column=4)

boton_calcular.grid(row=3, column=0)
label_resultado.grid(row=3, column=1)

# Iniciar el bucle de la ventana
ventana.mainloop()