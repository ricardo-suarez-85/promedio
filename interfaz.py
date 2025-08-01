import tkinter as tk
from tkinter import messagebox

def calcular_promedio():
    try:
        nombre = entry_nombre.get()
        mate = float(entry_mate.get())
        espanol = float(entry_espanol.get())
        historia = float(entry_historia.get())
        compu = float(entry_compu.get())

        promedio = (mate + espanol + historia + compu) / 4
        resultado = round(promedio, 1)

        if promedio >= 6:
            mensaje = f"¡Felicidades {nombre}, aprobaste con {resultado}!"
        else:
            mensaje = f"Lo siento {nombre}, reprobaste con {resultado}."

        messagebox.showinfo("Resultado", mensaje)

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa calificaciones válidas (números).")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Promedio Escolar")
ventana.geometry("800x600")

ventana.configure(bg="#000000") 


label_style = {"bg": "#000000", "fg": "#00BFFF", "font": ("Arial", 12)}
entry_style = {"bg": "#1c1c1c", "fg": "green", "insertbackground": "white", "font": ("Arial", 12)}

# Widgets
tk.Label(ventana, text="Nombre:", **label_style).pack(pady=5)
entry_nombre = tk.Entry(ventana, **entry_style)
entry_nombre.pack()

tk.Label(ventana, text="¿Cual es tu calificación en Matemáticas?:").pack()
entry_mate = tk.Entry(ventana)
entry_mate.pack()

tk.Label(ventana, text="¿Cual es tu calificación en Español?:").pack()
entry_espanol = tk.Entry(ventana)
entry_espanol.pack()

tk.Label(ventana, text="¿Cual es tu calificación en Historia?:").pack()
entry_historia = tk.Entry(ventana)
entry_historia.pack()

tk.Label(ventana, text="¿Cul es tu calificación en Computación?:").pack()
entry_compu = tk.Entry(ventana)
entry_compu.pack()

tk.Button(ventana, text="Calcular Promedio", command=calcular_promedio).pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()
