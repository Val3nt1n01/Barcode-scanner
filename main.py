import tkinter as tk
from PIL import Image, ImageTk
import os

# 1. BASE DE DATOS REGISTRADA
# Relacionamos el código de barras exacto con el nombre del libro y su imagen
REGISTRO_LIBROS = {
    "7802215512421": {
        "nombre": "Cien Años de Soledad",
        "imagen": "cien_anos.jpg"
    }
   
}

def procesar_escaneo(event=None):
    # Obtener el código que ingresó el escáner y limpiar espacios
    codigo = entrada_codigo.get().strip()
    entrada_codigo.delete(0, tk.END)  # Limpiar la casilla para el siguiente escaneo
    
    if not codigo:
        return

    # 2. VALIDAR SI EL CÓDIGO ESTÁ REGISTRADO
    if codigo in REGISTRO_LIBROS:
        libro = REGISTRO_LIBROS[codigo]
        
        # Mostrar el nombre del objeto
        lbl_resultado.config(text=f"Objeto: {libro['nombre']}", fg="green")
        
        # Cargar y redimensionar la imagen si existe
        ruta_img = libro["imagen"]
        if os.path.exists(ruta_img):
            imagen_original = Image.open(ruta_img)
            # Ajustar tamaño a 200x280 píxeles
            imagen_resized = imagen_original.resize((200, 280), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(imagen_resized)
            
            lbl_imagen.config(image=photo, text="")
            lbl_imagen.image = photo  # Mantener referencia en memoria
        else:
            lbl_imagen.config(image='', text="[Imagen no encontrada en carpeta]")
    else:
        # 3. SI NO ESTÁ REGISTRADO
        lbl_resultado.config(text="Objeto no encontrado", fg="red")
        lbl_imagen.config(image='', text="")

# 4. CONFIGURACIÓN DE LA INTERFAZ GRÁFICA (GUI)
ventana = tk.Tk()
ventana.title("Verificador de Código de Barras")
ventana.geometry("400x500")

# Indicaciones en pantalla
lbl_titulo = tk.Label(ventana, text="Escanee un código de barras:", font=("Arial", 12))
lbl_titulo.pack(pady=10)

# Entrada donde el escáner escribirá automáticamente
entrada_codigo = tk.Entry(ventana, font=("Arial", 14), justify="center")
entrada_codigo.pack(pady=5)
entrada_codigo.focus()  # Mantiene el cursor listo para recibir el escáner

# Cuando el escáner envíe "Enter", ejecutará la función procesar_escaneo
entrada_codigo.bind('<Return>', procesar_escaneo)

# Etiqueta para el texto (Nombre del libro u "Objeto no encontrado")
lbl_resultado = tk.Label(ventana, text="", font=("Arial", 14, "bold"))
lbl_resultado.pack(pady=15)

# Etiqueta donde se desplegará la imagen
lbl_imagen = tk.Label(ventana)
lbl_imagen.pack(pady=10)

# Iniciar la aplicación
ventana.mainloop()