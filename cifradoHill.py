import tkinter as tk
from tkinter import messagebox, ttk
import numpy as np

def cifrar_hill(palabra, clave):
    return procesar_hill(palabra, clave, cifrar=True)

def descifrar_hill(palabra, clave):
    return procesar_hill(palabra, clave, cifrar=False)

def procesar_hill(palabra, clave, cifrar=True):
    # Convertir la palabra a números (A=0, B=1, ..., Z=25)
    palabra = palabra.upper()
    numeros = [ord(c) - 65 for c in palabra if c.isalpha()]
    
    # Asegurarse de que la longitud de la palabra sea par
    if len(numeros) % 2 != 0:
        numeros.append(0)  # Añadir un padding si es necesario
    
    # Convertir la clave a una matriz 2x2
    clave_matriz = np.array(clave).reshape(2, 2)
    
    # Si estamos descifrando, calcular la matriz inversa
    if not cifrar:
        det = int(np.round(np.linalg.det(clave_matriz)))
        det_inv = pow(det, -1, 26)
        clave_matriz = (det_inv * np.round(det * np.linalg.inv(clave_matriz)).astype(int) % 26).astype(int)
    
    # Procesar
    resultado = []
    for i in range(0, len(numeros), 2):
        bloque = np.array(numeros[i:i+2])
        resultado_bloque = np.dot(clave_matriz, bloque) % 26
        resultado.extend(resultado_bloque)
    
    # Convertir números procesados de vuelta a letras
    return ''.join([chr(n + 65) for n in resultado])

def procesar():
    texto = entrada_texto.get()
    try:
        clave = [int(k) for k in entrada_clave.get().split(',')]
        if len(clave) != 4:
            raise ValueError("La clave debe tener 4 números")
        
        if modo.get() == "Cifrar":
            resultado = cifrar_hill(texto, clave)
            operacion = "cifrado"
        else:
            resultado = descifrar_hill(texto, clave)
            operacion = "descifrado"
        
        resultado_var.set(f"Texto {operacion}: {resultado}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cifrado y Descifrado de Hill")
ventana.geometry("350x250")

# Crear y colocar los widgets
tk.Label(ventana, text="Texto a procesar:").pack()
entrada_texto = tk.Entry(ventana, width=40)
entrada_texto.pack()

tk.Label(ventana, text="Clave (4 números separados por comas):").pack()
entrada_clave = tk.Entry(ventana, width=40)
entrada_clave.pack()

modo = tk.StringVar(value="Cifrar")
tk.Label(ventana, text="Modo:").pack()
ttk.Combobox(ventana, textvariable=modo, values=["Cifrar", "Descifrar"], state="readonly").pack()

tk.Button(ventana, text="Procesar", command=procesar).pack(pady=10)

resultado_var = tk.StringVar()
tk.Label(ventana, textvariable=resultado_var, wraplength=300).pack()

# Iniciar el loop de la interfaz gráfica
ventana.mainloop()